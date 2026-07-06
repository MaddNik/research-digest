#!/usr/bin/env node
/* Vault publisher (v2, multi-key): builds the passkey-gated /vault/ section
   from a PRIVATE workspace directory that must never be committed to git.

   Usage:
     PASSKEY_OWNER='...' PASSKEY_COLLAB='...' node automation/vault-publish.mjs <workspace-dir>

   Workspace layout (plaintext, keep outside the repo):
     index.json    manifest:
                   { "audiences": { "<aud>": { "env": "PASSKEY_..." }, ... },
                     "sections": [ { "name", "desc",
                       "docs": [ { "slug", "file", "title", "desc", "date",
                                   "audiences": ["owner", ...] } ] } ] }
     <doc>.html    inner HTML (header + sections) for each document

   Output (ciphertext only, safe to commit):
     vault/index.html           gate + one encrypted index view per audience
     vault/<slug>/index.html    gate + encrypted document

   Crypto (LUKS-style key slots):
   - Each payload body is encrypted ONCE under a random 256-bit content key
     (AES-256-GCM, random IV).
   - Per audience allowed on that payload, a key slot {salt, iv, wrap} wraps
     the content key: wrap = AES-GCM(PBKDF2-SHA256(passkey, salt, 600000),
     contentKey). The browser tries each slot with the entered passphrase; a
     GCM-authenticated unwrap yields the content key.
   - The index page carries a separate encrypted view per audience, rendered
     only from that audience's document list, so a keyholder cannot see even
     the titles of documents outside their audience.
   - Passkeys are only ever KDF inputs; they appear nowhere in the output.
     Re-run with new env values to rotate keys. Decoy slots could be added for
     padding if slot-count metadata ever matters. */
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';

const ITER = 600000;
const REPO = path.dirname(path.dirname(new URL(import.meta.url).pathname));
const BASE = '/research-digest/vault/';

const ws = process.argv[2];
if (!ws) {
  console.error("usage: PASSKEY_<AUD>='...' node automation/vault-publish.mjs <workspace-dir>");
  process.exit(1);
}

const manifest = JSON.parse(fs.readFileSync(path.join(ws, 'index.json'), 'utf8'));
const audiences = manifest.audiences || {};
const passkeys = {};
for (const [name, cfg] of Object.entries(audiences)) {
  const pw = process.env[cfg.env];
  if (!pw) { console.error(`missing env ${cfg.env} for audience "${name}"`); process.exit(1); }
  passkeys[name] = pw;
}

function wrapSlot(passkey, contentKey) {
  const salt = crypto.randomBytes(16);
  const iv = crypto.randomBytes(12);
  const kek = crypto.pbkdf2Sync(passkey, salt, ITER, 32, 'sha256');
  const c = crypto.createCipheriv('aes-256-gcm', kek, iv);
  const wrap = Buffer.concat([c.update(contentKey), c.final(), c.getAuthTag()]);
  return { salt: salt.toString('base64'), iv: iv.toString('base64'), wrap: wrap.toString('base64') };
}

/* one unit = one body encrypted under a fresh content key + slots for the
   audiences allowed to read it */
function makeUnit(plaintext, audNames) {
  const contentKey = crypto.randomBytes(32);
  const iv = crypto.randomBytes(12);
  const c = crypto.createCipheriv('aes-256-gcm', contentKey, iv);
  const ct = Buffer.concat([c.update(plaintext, 'utf8'), c.final(), c.getAuthTag()]);
  return {
    slots: audNames.map(a => wrapSlot(passkeys[a], contentKey)),
    body: { iv: iv.toString('base64'), ct: ct.toString('base64') },
  };
}

function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

function shell({ title, payload, isIndex }) {
  const backBar = isIndex
    ? `<a href="#" id="lock" hidden>Lock vault</a>`
    : `<a href="${BASE}">&#8592; Back to Vault</a><a href="#" id="lock" hidden>Lock vault</a>`;
  return `<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>${esc(title)}</title>
<style>
:root{--bg:#0f1115;--surface:#181b20;--ink:#e6e8eb;--muted:#9aa0a8;--line:#2a2f37;--accent:#6ea8fe}
*{box-sizing:border-box}
html{color-scheme:dark}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}
#rt-bar{position:sticky;top:0;z-index:9999;display:flex;flex-wrap:wrap;gap:1.2rem;align-items:center;padding:.6rem 1.1rem;background:#15151a;border-bottom:1px solid #333;font:600 14px/1.4 system-ui,-apple-system,sans-serif}
#rt-bar a{color:#8ab4f8;text-decoration:none}
#rt-bar a:hover{text-decoration:underline}
.doc{max-width:820px;margin:40px auto;background:var(--surface);padding:48px 56px;border:1px solid var(--line);border-radius:8px}
header h1{margin:0 0 4px;font-size:28px;color:#fff}
.meta{color:var(--muted);font-size:13px;margin:0 0 24px}
section{margin:0 0 28px}
section h2{font-size:20px;color:#fff;border-bottom:1px solid var(--line);padding-bottom:6px}
a{color:var(--accent)}
code{background:#0b0d11;border:1px solid var(--line);border-radius:4px;padding:1px 5px;font-size:14px}
ul.vault-list{list-style:none;padding:0;margin:0}
ul.vault-list li{padding:12px 0;border-bottom:1px solid var(--line)}
ul.vault-list a{font-weight:600;font-size:16.5px;text-decoration:none}
ul.vault-list a:hover{text-decoration:underline}
ul.vault-list .d{color:var(--muted);font-size:13.5px;margin-top:2px}
p.vault-empty{color:var(--muted)}
#gate{max-width:420px;margin:18vh auto;background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:34px 38px;text-align:center}
#gate h1{font-size:19px;color:#fff;margin:0 0 6px}
#gate p{color:var(--muted);font-size:13.5px;margin:0 0 18px}
#pw{width:100%;padding:9px 12px;border-radius:6px;border:1px solid var(--line);background:#0b0d11;color:var(--ink);font-size:15px}
#go{margin-top:12px;width:100%;padding:9px 12px;border-radius:6px;border:1px solid var(--accent);background:transparent;color:var(--accent);font-size:15px;cursor:pointer}
#go:hover{background:rgba(110,168,254,.12)}
#err{color:#e07070;font-size:13px;margin-top:10px;min-height:1.2em}
@media (max-width:640px){.doc{margin:0;border-radius:0;padding:28px 20px}}
</style>
</head>
<body>
<div id="rt-bar">${backBar}</div>
<div id="gate">
  <h1>Vault</h1>
  <p>Enter your vault passkey. Decryption happens entirely in your browser.</p>
  <input id="pw" type="password" autocomplete="off" autofocus>
  <button id="go" type="button">Unlock</button>
  <div id="err"></div>
</div>
<main class="doc" id="content" hidden></main>
<script id="payload" type="application/json">${payload}</script>
<script>
(function () {
  var meta = JSON.parse(document.getElementById('payload').textContent);
  var CACHE = 'rt_vault_pass';
  function b64(s) { var bin = atob(s), a = new Uint8Array(bin.length); for (var i = 0; i < bin.length; i++) a[i] = bin.charCodeAt(i); return a; }
  async function kdf(pw, salt) {
    var base = await crypto.subtle.importKey('raw', new TextEncoder().encode(pw), 'PBKDF2', false, ['deriveKey']);
    return crypto.subtle.deriveKey({ name: 'PBKDF2', salt: salt, iterations: meta.iter, hash: 'SHA-256' },
      base, { name: 'AES-GCM', length: 256 }, false, ['decrypt']);
  }
  /* try every slot of every unit; return the first body that decrypts */
  async function tryDecrypt(pw) {
    for (var u = 0; u < meta.units.length; u++) {
      var unit = meta.units[u];
      for (var s = 0; s < unit.slots.length; s++) {
        var slot = unit.slots[s];
        try {
          var kek = await kdf(pw, b64(slot.salt));
          var raw = await crypto.subtle.decrypt({ name: 'AES-GCM', iv: b64(slot.iv) }, kek, b64(slot.wrap));
          var contentKey = await crypto.subtle.importKey('raw', raw, { name: 'AES-GCM' }, false, ['decrypt']);
          var pt = await crypto.subtle.decrypt({ name: 'AES-GCM', iv: b64(unit.body.iv) }, contentKey, b64(unit.body.ct));
          return new TextDecoder().decode(pt);
        } catch (e) { /* wrong slot for this key; keep trying */ }
      }
    }
    throw new Error('no slot matched');
  }
  function reveal(html) {
    document.getElementById('content').innerHTML = html;
    document.getElementById('content').hidden = false;
    var g = document.getElementById('gate'); if (g) g.remove();
    var l = document.getElementById('lock'); if (l) l.hidden = false;
  }
  async function unlock() {
    var err = document.getElementById('err');
    err.textContent = '';
    var pw = document.getElementById('pw').value;
    if (!pw) return;
    document.getElementById('go').disabled = true;
    try {
      var html = await tryDecrypt(pw);
      try { sessionStorage.setItem(CACHE, pw); } catch (e) {}
      reveal(html);
    } catch (e) {
      err.textContent = 'Wrong passkey.';
    }
    var go = document.getElementById('go'); if (go) go.disabled = false;
  }
  document.getElementById('go').addEventListener('click', unlock);
  document.getElementById('pw').addEventListener('keydown', function (e) { if (e.key === 'Enter') unlock(); });
  document.getElementById('lock').addEventListener('click', function (e) {
    e.preventDefault();
    try { sessionStorage.removeItem(CACHE); } catch (err) {}
    location.reload();
  });
  /* auto-unlock from the per-tab session cache */
  (async function () {
    var cached = null;
    try { cached = sessionStorage.getItem(CACHE); } catch (e) {}
    if (!cached) return;
    try { reveal(await tryDecrypt(cached)); }
    catch (e) { /* this page has no slot for the cached key; leave the gate */ }
  })();
})();
</script>
</body></html>
`;
}

/* documents: one unit each, slots for the doc's audiences */
let count = 0;
const audDocs = {};
for (const a of Object.keys(audiences)) audDocs[a] = [];
for (const sec of manifest.sections) {
  for (const doc of sec.docs) {
    const auds = doc.audiences || [];
    if (!auds.length) { console.error(`doc ${doc.slug} has no audiences`); process.exit(1); }
    for (const a of auds) {
      if (!(a in passkeys)) { console.error(`doc ${doc.slug}: unknown audience "${a}"`); process.exit(1); }
      audDocs[a].push({ sec, doc });
    }
    const inner = fs.readFileSync(path.join(ws, doc.file), 'utf8');
    const payload = JSON.stringify({ v: 2, iter: ITER, units: [makeUnit(inner, auds)] });
    const out = path.join(REPO, 'vault', doc.slug, 'index.html');
    fs.mkdirSync(path.dirname(out), { recursive: true });
    fs.writeFileSync(out, shell({ title: 'Vault document', payload, isIndex: false }));
    count++;
    console.log(`doc  : vault/${doc.slug}/index.html  [${auds.join(', ')}]`);
  }
}

/* index: one unit per audience, each rendering only that audience's docs */
function renderIndexView(audName) {
  let html = `<header><h1>Vault</h1><p class="meta">Private documents &middot; unlocked for this tab &middot; use Lock to re-gate</p></header>`;
  const mine = audDocs[audName];
  if (!mine.length) {
    html += `<section><p class="vault-empty">No documents have been shared with this key yet.</p></section>`;
    return html;
  }
  const bySec = new Map();
  for (const { sec, doc } of mine) {
    if (!bySec.has(sec.name)) bySec.set(sec.name, { sec, docs: [] });
    bySec.get(sec.name).docs.push(doc);
  }
  for (const { sec, docs } of bySec.values()) {
    html += `<section><h2>${esc(sec.name)}</h2>`;
    if (sec.desc) html += `<p class="d" style="color:#9aa0a8;font-size:14px">${esc(sec.desc)}</p>`;
    html += `<ul class="vault-list">`;
    for (const doc of docs) {
      html += `<li><a href="${BASE}${encodeURIComponent(doc.slug)}/">${esc(doc.title)}</a>` +
        `<div class="d">${esc(doc.desc || '')}${doc.date ? ' &middot; ' + esc(doc.date) : ''}</div></li>`;
    }
    html += `</ul></section>`;
  }
  return html;
}

const units = Object.keys(audiences).map(a => makeUnit(renderIndexView(a), [a]));
const idxPayload = JSON.stringify({ v: 2, iter: ITER, units });
const idxOut = path.join(REPO, 'vault', 'index.html');
fs.mkdirSync(path.dirname(idxOut), { recursive: true });
fs.writeFileSync(idxOut, shell({ title: 'Vault', payload: idxPayload, isIndex: true }));
console.log('index: vault/index.html  [' + Object.keys(audiences).join(', ') + ' views]');
console.log(`published ${count} document(s) + index, ${Object.keys(audiences).length} audience(s), ${ITER} KDF iterations`);
