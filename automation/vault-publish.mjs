#!/usr/bin/env node
/* Vault publisher: builds the passkey-gated /vault/ section from a PRIVATE
   workspace directory that must never be committed to git.

   Usage:
     PASSKEY='...' node automation/vault-publish.mjs <workspace-dir>

   Workspace layout (plaintext, keep outside the repo):
     index.json           manifest: { "sections": [ { "name", "desc",
                          "docs": [ { "slug", "file", "title", "desc", "date" } ] } ] }
     <doc>.html           inner HTML (header + sections) for each document

   Output (ciphertext only, safe to commit):
     vault/index.html             gate + encrypted index of all documents
     vault/<slug>/index.html      gate + encrypted document

   Crypto: AES-256-GCM; key = PBKDF2-SHA256(passkey, random 16B salt, 600000
   iterations); random 12B IV; ciphertext||tag base64. The passkey is only ever
   a KDF input - it appears nowhere in the output. Wrong passkey = GCM auth
   failure. Re-run with a new PASSKEY to rotate every page at once. */
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';

const ITER = 600000;
const REPO = path.dirname(path.dirname(new URL(import.meta.url).pathname));
const BASE = '/research-digest/vault/';

const ws = process.argv[2];
const passkey = process.env.PASSKEY;
if (!ws || !passkey) {
  console.error("usage: PASSKEY='...' node automation/vault-publish.mjs <workspace-dir>");
  process.exit(1);
}

const manifest = JSON.parse(fs.readFileSync(path.join(ws, 'index.json'), 'utf8'));

function encrypt(plaintext) {
  const salt = crypto.randomBytes(16);
  const iv = crypto.randomBytes(12);
  const key = crypto.pbkdf2Sync(passkey, salt, ITER, 32, 'sha256');
  const c = crypto.createCipheriv('aes-256-gcm', key, iv);
  const ct = Buffer.concat([c.update(plaintext, 'utf8'), c.final(), c.getAuthTag()]);
  return JSON.stringify({ v: 1, kdf: 'PBKDF2-SHA256', iter: ITER,
    salt: salt.toString('base64'), iv: iv.toString('base64'), ct: ct.toString('base64') });
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
  <p>Enter the vault passkey. Decryption happens entirely in your browser.</p>
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
  async function tryDecrypt(pw) {
    var base = await crypto.subtle.importKey('raw', new TextEncoder().encode(pw), 'PBKDF2', false, ['deriveKey']);
    var key = await crypto.subtle.deriveKey(
      { name: 'PBKDF2', salt: b64(meta.salt), iterations: meta.iter, hash: 'SHA-256' },
      base, { name: 'AES-GCM', length: 256 }, false, ['decrypt']);
    var pt = await crypto.subtle.decrypt({ name: 'AES-GCM', iv: b64(meta.iv) }, key, b64(meta.ct));
    return new TextDecoder().decode(pt);
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
    try {
      var html = await tryDecrypt(pw);
      try { sessionStorage.setItem(CACHE, pw); } catch (e) {}
      reveal(html);
    } catch (e) {
      err.textContent = 'Wrong passkey.';
    }
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
    catch (e) { try { sessionStorage.removeItem(CACHE); } catch (err) {} }
  })();
})();
</script>
</body></html>
`;
}

/* documents */
let count = 0;
for (const sec of manifest.sections) {
  for (const doc of sec.docs) {
    const inner = fs.readFileSync(path.join(ws, doc.file), 'utf8');
    const out = path.join(REPO, 'vault', doc.slug, 'index.html');
    fs.mkdirSync(path.dirname(out), { recursive: true });
    fs.writeFileSync(out, shell({ title: 'Vault document', payload: encrypt(inner), isIndex: false }));
    count++;
    console.log('doc  : vault/' + doc.slug + '/index.html');
  }
}

/* index */
let idx = `<header><h1>Vault</h1><p class="meta">Private documents &middot; unlocked for this tab &middot; use Lock to re-gate</p></header>`;
for (const sec of manifest.sections) {
  idx += `<section><h2>${esc(sec.name)}</h2>`;
  if (sec.desc) idx += `<p class="d" style="color:#9aa0a8;font-size:14px">${esc(sec.desc)}</p>`;
  idx += `<ul class="vault-list">`;
  for (const doc of sec.docs) {
    idx += `<li><a href="${BASE}${encodeURIComponent(doc.slug)}/">${esc(doc.title)}</a>` +
      `<div class="d">${esc(doc.desc || '')}${doc.date ? ' &middot; ' + esc(doc.date) : ''}</div></li>`;
  }
  idx += `</ul></section>`;
}
const idxOut = path.join(REPO, 'vault', 'index.html');
fs.mkdirSync(path.dirname(idxOut), { recursive: true });
fs.writeFileSync(idxOut, shell({ title: 'Vault', payload: encrypt(idx), isIndex: true }));
console.log('index: vault/index.html');
console.log('published ' + count + ' document(s) + index, ' + ITER + ' KDF iterations');
