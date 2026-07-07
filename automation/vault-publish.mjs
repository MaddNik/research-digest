#!/usr/bin/env node
/* Vault publisher (v2, multi-key + per-article share links): builds the
   passkey-gated /vault/ section from a PRIVATE workspace directory that must
   never be committed to git.

   Usage:
     PASSKEY_OWNER='...' PASSKEY_COLLAB='...' node automation/vault-publish.mjs <workspace-dir>

   Workspace layout (plaintext, keep outside the repo):
     index.json    manifest:
                   { "audiences": { "<aud>": { "env": "PASSKEY_...",
                                               "canShare": true|false }, ... },
                     "sections": [ { "name", "desc",
                       "docs": [ { "slug", "file", "title", "desc", "date",
                                   "audiences": ["owner", ...] } ] } ] }
     <doc>.html    inner HTML (header + sections) for each document

   Output (ciphertext only, safe to commit):
     vault/index.html           gate + one encrypted index view per audience
     vault/<slug>/index.html    gate + encrypted document

   Crypto (LUKS-style key slots):
   - Each payload body is encrypted ONCE under a random 256-bit content key
     (AES-256-GCM, random IV). Per audience allowed on that payload, a key slot
     {salt, iv, wrap} wraps the content key under PBKDF2-SHA256(passkey, salt,
     600000). The browser tries each slot with the entered passphrase; an
     authenticated unwrap yields the content key.
   - The index carries a separate encrypted view per audience so a keyholder
     cannot see even the titles of documents outside their audience.

   Per-article share links (capability URLs):
   - An audience with "canShare": true gets, in its (encrypted) index view, the
     raw per-document content key embedded on a Share button. Since that index
     view is itself encrypted under the audience's passkey, the embedded keys
     are protected by that passkey. The button builds a link of the form
     <origin>/research-digest/vault/<slug>/#k=<base64url-content-key>. A
     recipient opening that link decrypts that ONE document directly from the
     key in the URL fragment - no passkey, no other access. Fragments are never
     sent to the server, so the key is not logged. Revoke a link by
     re-publishing that document (fresh content key). */
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

function b64url(buf) {
  return buf.toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

function wrapSlot(passkey, contentKey) {
  const salt = crypto.randomBytes(16);
  const iv = crypto.randomBytes(12);
  const kek = crypto.pbkdf2Sync(passkey, salt, ITER, 32, 'sha256');
  const c = crypto.createCipheriv('aes-256-gcm', kek, iv);
  const wrap = Buffer.concat([c.update(contentKey), c.final(), c.getAuthTag()]);
  return { salt: salt.toString('base64'), iv: iv.toString('base64'), wrap: wrap.toString('base64') };
}

function encBody(plaintext, contentKey) {
  const iv = crypto.randomBytes(12);
  const c = crypto.createCipheriv('aes-256-gcm', contentKey, iv);
  const ct = Buffer.concat([c.update(plaintext, 'utf8'), c.final(), c.getAuthTag()]);
  return { iv: iv.toString('base64'), ct: ct.toString('base64') };
}

/* one unit = one body encrypted under a content key + slots for the audiences
   allowed to read it. contentKey may be supplied (docs) or generated (index). */
function makeUnit(plaintext, audNames, contentKey) {
  const ck = contentKey || crypto.randomBytes(32);
  return { slots: audNames.map(a => wrapSlot(passkeys[a], ck)), body: encBody(plaintext, ck) };
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
ul.vault-list a.doc-link{font-weight:600;font-size:16.5px;text-decoration:none}
ul.vault-list a.doc-link:hover{text-decoration:underline}
ul.vault-list .d{color:var(--muted);font-size:13.5px;margin-top:2px}
p.vault-empty{color:var(--muted)}
.share-btn{margin-left:10px;padding:2px 10px;font-size:12.5px;border-radius:6px;border:1px solid var(--accent);background:transparent;color:var(--accent);cursor:pointer;vertical-align:2px}
.share-btn:hover{background:rgba(110,168,254,.12)}
.share-out{margin-top:8px}
.share-out[hidden]{display:none}
.share-out input{width:100%;padding:7px 10px;border-radius:6px;border:1px solid var(--line);background:#0b0d11;color:var(--ink);font-size:12.5px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.share-note{color:var(--muted);font-size:12px;margin-top:4px}
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
  var IS_INDEX = ${isIndex ? 'true' : 'false'};
  var meta = JSON.parse(document.getElementById('payload').textContent);
  var CACHE = 'rt_vault_pass';
  function b64(s) { s = s.replace(/-/g, '+').replace(/_/g, '/'); while (s.length % 4) s += '='; var bin = atob(s), a = new Uint8Array(bin.length); for (var i = 0; i < bin.length; i++) a[i] = bin.charCodeAt(i); return a; }
  async function kdf(pw, salt) {
    var base = await crypto.subtle.importKey('raw', new TextEncoder().encode(pw), 'PBKDF2', false, ['deriveKey']);
    return crypto.subtle.deriveKey({ name: 'PBKDF2', salt: salt, iterations: meta.iter, hash: 'SHA-256' },
      base, { name: 'AES-GCM', length: 256 }, false, ['decrypt']);
  }
  async function decBody(body, contentKey) {
    var pt = await crypto.subtle.decrypt({ name: 'AES-GCM', iv: b64(body.iv) }, contentKey, b64(body.ct));
    return new TextDecoder().decode(pt);
  }
  /* passkey path: try every slot of every unit; return the first body that decrypts */
  async function tryDecrypt(pw) {
    for (var u = 0; u < meta.units.length; u++) {
      var unit = meta.units[u];
      for (var s = 0; s < unit.slots.length; s++) {
        var slot = unit.slots[s];
        try {
          var kek = await kdf(pw, b64(slot.salt));
          var raw = await crypto.subtle.decrypt({ name: 'AES-GCM', iv: b64(slot.iv) }, kek, b64(slot.wrap));
          var contentKey = await crypto.subtle.importKey('raw', raw, { name: 'AES-GCM' }, false, ['decrypt']);
          return await decBody(unit.body, contentKey);
        } catch (e) { /* wrong slot for this key; keep trying */ }
      }
    }
    throw new Error('no slot matched');
  }
  /* share-link path (document pages only): decrypt this doc's single body
     directly from a content key carried in the URL fragment (#k=...) */
  async function tryShareLink() {
    var m = location.hash.match(/[#&]k=([^&]+)/);
    if (!m || IS_INDEX || !meta.units.length) return null;
    var raw = b64(decodeURIComponent(m[1]));
    var contentKey = await crypto.subtle.importKey('raw', raw, { name: 'AES-GCM' }, false, ['decrypt']);
    return await decBody(meta.units[0].body, contentKey);
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
  /* Share buttons in an owner index view: mint a capability URL for one doc */
  document.addEventListener('click', function (e) {
    var btn = e.target.closest ? e.target.closest('.share-btn') : null;
    if (!btn) return;
    e.preventDefault();
    var url = location.origin + btn.getAttribute('data-url') + '#k=' + btn.getAttribute('data-k');
    var li = btn.closest('li');
    var out = li ? li.querySelector('.share-out') : null;
    if (!out) return;
    var input = out.querySelector('input');
    var note = out.querySelector('.share-note');
    input.value = url;
    out.hidden = false;
    input.focus(); input.select();
    note.textContent = 'Anyone with this link can read this one article — nothing else in the vault.';
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(function () {
        note.textContent = 'Link copied — anyone with it can read this one article, nothing else.';
      }).catch(function () {});
    }
  });
  /* auto-unlock: first a share link, then the per-tab passkey cache */
  (async function () {
    try { var h = await tryShareLink(); if (h != null) { reveal(h); return; } } catch (e) {}
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

/* documents: one unit each; keep each doc's content key for share links */
let count = 0;
const audDocs = {};
const docKeys = {};
for (const a of Object.keys(audiences)) audDocs[a] = [];
for (const sec of manifest.sections) {
  for (const doc of sec.docs) {
    const auds = doc.audiences || [];
    if (!auds.length) { console.error(`doc ${doc.slug} has no audiences`); process.exit(1); }
    for (const a of auds) {
      if (!(a in passkeys)) { console.error(`doc ${doc.slug}: unknown audience "${a}"`); process.exit(1); }
      audDocs[a].push({ sec, doc });
    }
    const ck = crypto.randomBytes(32);
    docKeys[doc.slug] = b64url(ck);
    const inner = fs.readFileSync(path.join(ws, doc.file), 'utf8');
    const payload = JSON.stringify({ v: 2, iter: ITER, units: [makeUnit(inner, auds, ck)] });
    const out = path.join(REPO, 'vault', doc.slug, 'index.html');
    fs.mkdirSync(path.dirname(out), { recursive: true });
    fs.writeFileSync(out, shell({ title: 'Vault document', payload, isIndex: false }));
    count++;
    console.log(`doc  : vault/${doc.slug}/index.html  [${auds.join(', ')}]`);
  }
}

/* index: one unit per audience, each rendering only that audience's docs;
   audiences with canShare get per-entry Share buttons carrying the content key */
function renderIndexView(audName) {
  const canShare = !!(audiences[audName] && audiences[audName].canShare);
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
      const url = `${BASE}${encodeURIComponent(doc.slug)}/`;
      html += `<li><a class="doc-link" href="${url}">${esc(doc.title)}</a>`;
      if (canShare) {
        html += `<button type="button" class="share-btn" data-url="${url}" data-k="${docKeys[doc.slug]}">Share link</button>`;
      }
      html += `<div class="d">${esc(doc.desc || '')}${doc.date ? ' &middot; ' + esc(doc.date) : ''}</div>`;
      if (canShare) {
        html += `<div class="share-out" hidden><input readonly onclick="this.select()"><div class="share-note"></div></div>`;
      }
      html += `</li>`;
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
