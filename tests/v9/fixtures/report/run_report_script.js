'use strict';
// Runs report.html's script under Node on a minimal DOM, drives its controls, and prints a JSON summary.
//
// Why: the report's interactive parts are plain DOM code; this executes them in tests (no browser, no network) so a
// typo or a data shape the script does not expect fails a test. The DOM here never parses HTML: innerHTML,
// outerHTML, insertAdjacentHTML and document.write throw, so a script that turned data into markup would fail.
//
// It also records where focus lands after a focused control is activated, and what the print view holds between
// beforeprint and afterprint.
//
// Usage: node run_report_script.js report.html  ->  {"errors": [...], "start": {...}, "focus": {...}, "printed": {...},
//                                                    "text": "...", ...}

const fs = require('fs');
const vm = require('vm');

const HTML_NS = 'http://www.w3.org/1999/xhtml';
const errors = [];
const docListeners = {};
const created = {};

class Node {
  constructor() { this.parentNode = null; this.childNodes = []; }
  get textContent() { return this.childNodes.map(c => c.textContent).join(''); }
  set textContent(value) {
    this.replaceChildren();
    if (value !== null && value !== undefined && value !== '') this.appendChild(new Text(String(value)));
  }
  appendChild(node) {
    if (!(node instanceof Node)) throw new TypeError('appendChild expects a Node');
    if (node.parentNode) node.parentNode.removeChild(node);
    node.parentNode = this;
    this.childNodes.push(node);
    return node;
  }
  removeChild(node) {
    const i = this.childNodes.indexOf(node);
    if (i >= 0) this.childNodes.splice(i, 1);
    node.parentNode = null;
    return node;
  }
  append(...nodes) { for (const n of nodes) this.appendChild(typeof n === 'string' ? new Text(n) : n); }
  replaceChildren(...nodes) {
    for (const c of this.childNodes) c.parentNode = null;
    this.childNodes = [];
    this.append(...nodes);
  }
}

class Text extends Node {
  constructor(data) { super(); this.data = String(data); }
  get textContent() { return this.data; }
  set textContent(value) { this.data = String(value); }
}

const kebab = key => String(key).replace(/[A-Z]/g, c => '-' + c.toLowerCase());

class Element extends Node {
  constructor(tag, ns) {
    super();
    this.localName = String(tag).toLowerCase();
    this.tagName = this.localName.toUpperCase();
    this.namespaceURI = ns || HTML_NS;
    this.attributes = new Map();
    this.listeners = {};
    this.style = {};
    this.open = false;
    this.disabled = false;
    this.checked = false;
    this._value = '';
    created[this.localName] = (created[this.localName] || 0) + 1;
  }
  get children() { return this.childNodes.filter(c => c instanceof Element); }
  setAttribute(key, value) { this.attributes.set(String(key), String(value)); }
  getAttribute(key) { return this.attributes.has(key) ? this.attributes.get(key) : null; }
  hasAttribute(key) { return this.attributes.has(key); }
  removeAttribute(key) { this.attributes.delete(key); }
  get id() { return this.getAttribute('id') || ''; }
  get classList() {
    const list = () => (this.getAttribute('class') || '').split(/\s+/).filter(Boolean);
    const set = items => this.setAttribute('class', items.join(' '));
    return {
      contains: c => list().includes(c),
      add: (...cs) => set([...new Set(list().concat(cs))]),
      remove: (...cs) => set(list().filter(x => !cs.includes(x))),
      toggle: (c, force) => {
        const want = force === undefined ? !list().includes(c) : Boolean(force);
        set(want ? [...new Set(list().concat(c))] : list().filter(x => x !== c));
        return want;
      },
      replace: (a, b) => {
        if (!list().includes(a)) return false;
        set(list().map(x => (x === a ? b : x)));
        return true;
      }
    };
  }
  get dataset() {
    return new Proxy({}, {
      get: (t, key) => { const v = this.getAttribute('data-' + kebab(key)); return v === null ? undefined : v; },
      set: (t, key, value) => { this.setAttribute('data-' + kebab(key), value); return true; },
      deleteProperty: (t, key) => { this.removeAttribute('data-' + kebab(key)); return true; }
    });
  }
  get hidden() { return this.hasAttribute('hidden'); }
  set hidden(value) { if (value) this.setAttribute('hidden', ''); else this.removeAttribute('hidden'); }
  get value() { return this._value; }
  set value(v) { this._value = String(v); }
  get innerHTML() { throw new Error('innerHTML read'); }
  set innerHTML(v) { throw new Error('innerHTML written: data must never become markup'); }
  get outerHTML() { throw new Error('outerHTML read'); }
  set outerHTML(v) { throw new Error('outerHTML written'); }
  insertAdjacentHTML() { throw new Error('insertAdjacentHTML used'); }
  addEventListener(type, fn) { (this.listeners[type] = this.listeners[type] || []).push(fn); }
  dispatch(type, extra) {
    const ev = Object.assign({type, target: this, currentTarget: this, defaultPrevented: false,
      preventDefault() { this.defaultPrevented = true; }}, extra || {});
    for (let node = this; node; node = node.parentNode) {
      for (const fn of (node.listeners && node.listeners[type]) || []) { ev.currentTarget = node; fn(ev); }
    }
    for (const fn of docListeners[type] || []) { ev.currentTarget = document; fn(ev); }
    return ev;
  }
  matches(selector) { return matches(this, selector); }
  closest(selector) {
    for (let n = this; n instanceof Element; n = n.parentNode) if (matches(n, selector)) return n;
    return null;
  }
  contains(node) {
    for (let n = node; n; n = n.parentNode) if (n === this) return true;
    return false;
  }
  get isConnected() { return documentElement.contains(this); }
  querySelectorAll(selector) { return descendants(this).filter(e => matches(e, selector)); }
  querySelector(selector) { return this.querySelectorAll(selector)[0] || null; }
  focus() { document.activeElement = this; }
  scrollIntoView() {}
  getComputedTextLength() { return this.textContent.length * 7; }
}

function descendants(root) {
  const out = [];
  const walk = n => { for (const c of n.childNodes) if (c instanceof Element) { out.push(c); walk(c); } };
  walk(root);
  return out;
}

function compound(text) {
  const out = {tag: null, id: null, classes: [], attrs: []};
  const re = /^([a-zA-Z][\w-]*)|#([\w-]+)|\.([\w-]+)|\[([\w-]+)(?:="([^"]*)")?\]/g;
  let m;
  while ((m = re.exec(text)) !== null) {
    if (m[1]) out.tag = m[1].toLowerCase();
    else if (m[2]) out.id = m[2];
    else if (m[3]) out.classes.push(m[3]);
    else if (m[4]) out.attrs.push([m[4], m[5]]);
  }
  return out;
}

function matchCompound(el, c) {
  if (c.tag && el.localName !== c.tag) return false;
  if (c.id && el.id !== c.id) return false;
  if (c.classes.some(x => !el.classList.contains(x))) return false;
  return c.attrs.every(([k, v]) => el.hasAttribute(k) && (v === undefined || el.getAttribute(k) === v));
}

function matches(el, selector) {
  return selector.split(',').some(alt => {
    const parts = alt.replace(/>/g, ' ').trim().split(/\s+/).map(compound);
    if (!matchCompound(el, parts[parts.length - 1])) return false;
    let node = el.parentNode;
    for (let i = parts.length - 2; i >= 0; i -= 1) {
      while (node instanceof Element && !matchCompound(node, parts[i])) node = node.parentNode;
      if (!(node instanceof Element)) return false;
      node = node.parentNode;
    }
    return true;
  });
}

// --- the page: the template's elements that carry ids, with their initial values ---------------------------------
const html = fs.readFileSync(process.argv[2], 'utf8');
const scripts = [...html.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/g)];
const dataScript = scripts.find(m => /id="v2m-data"/.test(m[1]));
const appScript = scripts.find(m => !/type=/.test(m[1]));
const documentElement = new Element('html');
documentElement.setAttribute('class', (html.match(/<html[^>]*class="([^"]*)"/) || [])[1] || '');
const body = new Element('body');
documentElement.appendChild(body);
const markup = html.replace(/<noscript>[\s\S]*?<\/noscript>/g, '').replace(/<script[\s\S]*?<\/script>/g, '');
for (const m of markup.matchAll(/<(\w+)([^>]*?)\sid="([^"]+)"([^>]*)>/g)) {
  const el = new Element(m[1]);
  el.setAttribute('id', m[3]);
  const rest = m[2] + ' ' + m[4];
  for (const a of rest.matchAll(/([\w-]+)="([^"]*)"/g)) el.setAttribute(a[1], a[2]);
  if (/\schecked(\s|$)/.test(rest)) el.checked = true;
  if (el.hasAttribute('value')) el.value = el.getAttribute('value');
  if (m[1] === 'select') {
    const after = markup.slice(m.index);
    el.value = (after.match(/<option value="([^"]*)"/) || [])[1] || '';
  }
  if (m[3] === 'v2m-data') continue;
  body.appendChild(el);
}
const data = new Element('script');
data.setAttribute('id', 'v2m-data');
data.textContent = dataScript[2];
body.appendChild(data);

const document = {
  documentElement, body, activeElement: null,
  getElementById: id => descendants(documentElement).find(e => e.id === id) || null,
  createElement: tag => new Element(tag),
  createElementNS: (ns, tag) => new Element(tag, ns),
  createTextNode: text => new Text(text),
  querySelectorAll: selector => descendants(documentElement).filter(e => matches(e, selector)),
  querySelector: selector => descendants(documentElement).find(e => matches(e, selector)) || null,
  addEventListener: (type, fn) => { (docListeners[type] = docListeners[type] || []).push(fn); },
  write: () => { throw new Error('document.write used'); }
};
const windowListeners = {};
let printed = null;     // what #print-claims held between beforeprint and afterprint (what paper would show)
const window = {
  addEventListener: (type, fn) => { (windowListeners[type] = windowListeners[type] || []).push(fn); },
  print: () => {
    for (const fn of windowListeners.beforeprint || []) fn();
    const box = document.getElementById('print-claims');
    printed = {claims: box ? box.querySelectorAll('.print-claim').length : 0,
      evidence_items: box ? box.querySelectorAll('.evidence-item').length : 0,
      details_open: document.querySelectorAll('details').every(d => d.open),
      text: box ? box.textContent : ''};
    for (const fn of windowListeners.afterprint || []) fn();
    printed.emptied_after = box ? box.childNodes.length === 0 : true;
  }
};
const sandbox = {
  document, window, Node, Element, Text,
  CSS: {escape: value => String(value).replace(/["\\]/g, '\\$&')},
  console: {error: (...a) => errors.push(a.map(String).join(' ')), warn: () => {}, log: () => {}}
};

function step(name, fn) {
  try { fn(); } catch (err) { errors.push(name + ': ' + (err && err.stack ? err.stack : String(err))); }
}

const $ = id => document.getElementById(id);
const text = id => ($(id) ? $(id).textContent : '');
let start = null;
step('script', () => vm.runInNewContext(appScript[2], sandbox, {filename: 'report-script.js'}));
step('initial counts', () => {
  start = {
    chips: $('mechanism-graph').querySelectorAll('.chip').length,
    nodes: $('mechanism-graph').querySelectorAll('.node').length,
    claim_buttons: $('claim-buttons').querySelectorAll('button').length,
    hypothesis_rows: $('hypothesis-table').querySelectorAll('tbody tr').length,
    events: $('event-list').querySelectorAll('li').length,
    inventory_rows: $('inventory-body').querySelectorAll('tbody tr').length,
    inventory_tables: $('inventory-body').querySelectorAll('table').length,
    inventory_shown: $('inventory-body').querySelectorAll('tbody tr').filter(tr => !tr.hidden).length,
    other_evidence_rows: $('evidence-table').querySelectorAll('tbody tr').length,
    archive_items: $('archive-list').querySelectorAll('.archive-item').length,
    selected: (descendants($('claim-buttons')).find(b => b.getAttribute('aria-pressed') === 'true') || {})
      .textContent || null
  };
});
const inspected = {};
step('select every claim', () => {
  for (const b of $('claim-buttons').querySelectorAll('button')) {
    const id = b.getAttribute('data-claim');
    b.dispatch('click');
    inspected[id] = {claim: text('claim-inspector'), evidence: text('evidence-inspector')};
  }
});
const versions = {};
step('step through versions', () => {
  const range = $('version');
  range.value = '0';
  range.dispatch('input');
  versions[0] = $('mechanism-graph').querySelectorAll('.chip').length;
  const max = Number(range.max);          // the script sets the property, as a browser reflects it
  for (let v = 1; v <= max; v += 1) {
    $('step-next').dispatch('click');
    versions[v] = $('mechanism-graph').querySelectorAll('.chip').length;
  }
  $('step-back').dispatch('click');
  $('step-latest').dispatch('click');
});
step('keyboard on a chip', () => {
  const chip = $('mechanism-graph').querySelector('.chip');
  if (chip) chip.dispatch('keydown', {key: 'Enter'});
});
step('highlight hypotheses', () => {
  for (const b of $('hypothesis-table').querySelectorAll('[data-highlight]')) {
    const id = b.getAttribute('data-highlight');
    const again = () => $('hypothesis-table').querySelector('[data-highlight="' + id + '"]');
    again().dispatch('click');
  }
});
// Where keyboard focus lands after a focused control is activated (Enter or Space on a button fires click).
const describe = el => (el ? {
  id: el.getAttribute('data-claim') || el.getAttribute('data-highlight') || el.id || null, tag: el.localName,
  connected: el.isConnected,
  within: ['claim-buttons', 'hypothesis-table', 'mechanism-graph'].find(box => el.closest('#' + box)) || null} : null);
const focus = {};
step('focus after activation', () => {
  const activate = el => { el.focus(); el.dispatch('click'); return describe(document.activeElement); };
  const buttons = $('claim-buttons').querySelectorAll('button');
  const button = buttons[1] || buttons[0];
  if (button) focus.claim_button = {clicked: button.getAttribute('data-claim'), now: activate(button)};
  const chip = $('mechanism-graph').querySelector('.chip');
  if (chip) focus.chip = {clicked: chip.getAttribute('data-claim'), now: activate(chip)};
  const hl = $('hypothesis-table').querySelector('[data-highlight]');
  if (hl) focus.highlight = {clicked: hl.getAttribute('data-highlight'), now: activate(hl)};
  const link = $('hypothesis-table').querySelector('[data-select]');
  if (link) focus.claim_link = {clicked: link.getAttribute('data-select'), now: activate(link)};
});
step('filters and toggles', () => {
  for (const v of ['rejected', 'deferred', 'superseded', 'claims', 'all']) {
    $('archive-filter').value = v;
    $('archive-filter').dispatch('change');
  }
  for (const v of ['decisions', 'evidence', 'tools', 'refusals', 'log', 'all']) {
    $('event-filter').value = v;
    $('event-filter').dispatch('change');
  }
  $('show-archived').checked = false; $('show-archived').dispatch('change');
  $('show-archived').checked = true; $('show-archived').dispatch('change');
  for (let i = 0; i < 3; i += 1) $('theme-toggle').dispatch('click');
  $('print-report').dispatch('click');
  const search = $('inventory-search');
  if (search) {
    search.value = 'zzz-no-such-group';
    search.dispatch('input');
    search.value = '';
    search.dispatch('input');
  }
  const all = $('inventory-all');
  if (all) { all.checked = true; all.dispatch('change'); }
  const goto = $('event-list').querySelector('[data-version]');
  if (goto) { goto.focus(); goto.dispatch('click'); focus.show_version = describe(document.activeElement); }
});
process.stdout.write(JSON.stringify({
  errors, start, versions, inspected, created, focus, printed,
  inventory_all_shown: $('inventory-body').querySelectorAll('tbody tr').filter(tr => !tr.hidden).length,
  theme: documentElement.getAttribute('data-theme'),
  html_class: documentElement.getAttribute('class'),
  text: body.textContent
}));
