#!/usr/bin/env python3
"""Copy summarize-anything outputs from research-material into the site and
build _data/summaries.yml. Also post-processes each published summary to add a
back bar, a "read the full article" link, a figure lightbox/hover-preview with
Figure N labels, and MathJax for equation rendering."""
import json, os, re, shutil, time

SRC = "/home/nik/research-material"
REPO = "/home/nik/research-digest"
DEST = os.path.join(REPO, "summaries")
MANIFEST = os.path.join(REPO, "_data", "summaries.yml")
SUMMARIES_URL = "/research-digest/summaries/"


def find_url(*texts):
    blob = " ".join(t for t in texts if t)
    m = re.search(r"https?://[^\s\"'<>)]+", blob)
    if m:
        return m.group(0).rstrip(".,);")
    m = re.search(r"(?:IACR\s+)?ePrint\s+(\d{4})/(\d+)", blob, re.I)
    if m:
        return "https://eprint.iacr.org/%s/%s" % (m.group(1), m.group(2))
    m = re.search(r"arXiv[:\s]+(\d{4}\.\d{4,5})", blob, re.I)
    if m:
        return "https://arxiv.org/abs/%s" % m.group(1)
    m = re.search(r"\b(10\.\d{4,9}/[^\s\"'<>]+)", blob)
    if m:
        return "https://doi.org/%s" % m.group(1).rstrip(".,);")
    return ""


MONTHS = ["", "January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def derive_pub(source_url, source_type):
    """Best-effort source publication date from the source reference."""
    blob = (source_url or "") + " " + (source_type or "")
    m = re.search(r"arxiv\.org/abs/(\d{2})(\d{2})\.", blob, re.I) or re.search(r"arXiv[:\s]+(\d{2})(\d{2})\.", blob, re.I)
    if m:
        mo = int(m.group(2))
        return "%s 20%s" % (MONTHS[mo] if 1 <= mo <= 12 else "", m.group(1))
    m = re.search(r"eprint\.iacr\.org/(\d{4})/", blob, re.I) or re.search(r"ePrint\s+(\d{4})/", blob, re.I)
    if m:
        return m.group(1)
    m = re.search(r"\b(19|20)\d{2}\b", blob)
    return m.group(0) if m else ""


def clean(s):
    return (s or "").replace("—", " - ").replace("–", "-").strip()


def yaml_escape(s):
    return (s or "").replace("\\", "\\\\").replace('"', '\\"')


def slug_date(slug, fallback):
    m = re.search(r"(\d{4}-\d{2}-\d{2})$", slug)
    return m.group(1) if m else fallback


ENHANCE_HEAD = """
<style>
#rt-bar{position:sticky;top:0;z-index:9999;display:flex;flex-wrap:wrap;gap:1.2rem;align-items:center;padding:.6rem 1.1rem;background:#15151a;border-bottom:1px solid #333;font:600 14px/1.4 system-ui,-apple-system,sans-serif}
#rt-bar a{color:#8ab4f8;text-decoration:none}
#rt-bar a:hover{text-decoration:underline}
figure img{cursor:zoom-in}
#rt-lightbox{display:none;position:fixed;inset:0;z-index:100000;background:rgba(0,0,0,.88);align-items:center;justify-content:center;padding:2rem}
#rt-lightbox img{max-width:95vw;max-height:95vh}
#rt-figprev{display:none;position:fixed;z-index:100001;max-width:42vw;max-height:46vh;border:2px solid #666;border-radius:6px;box-shadow:0 10px 36px rgba(0,0,0,.7);pointer-events:none;background:#000}
</style>
"""

ENHANCE_TAIL = """
<script>
(function(){
  var bar=document.getElementById('rt-bar');
  if(bar && window.self!==window.top){bar.style.display='none';}
  var lb=document.createElement('div');lb.id='rt-lightbox';lb.innerHTML='<img alt="">';document.body.appendChild(lb);
  lb.addEventListener('click',function(){lb.style.display='none';});
  var prev=document.createElement('img');prev.id='rt-figprev';prev.alt='';document.body.appendChild(prev);
  var n=0;
  Array.prototype.forEach.call(document.querySelectorAll('figure'),function(fig){
    var img=fig.querySelector('img');if(!img)return;n++;
    if(!fig.id)fig.id='fig'+n;
    var cap=fig.querySelector('figcaption');
    if(!cap){cap=document.createElement('figcaption');cap.style.opacity='.7';cap.style.fontSize='.85em';cap.style.marginTop='.3em';cap.textContent='Figure '+n;fig.appendChild(cap);}
    img.addEventListener('click',function(){lb.firstChild.src=img.src;lb.style.display='flex';});
    img.addEventListener('mousemove',function(e){
      prev.src=img.src;prev.style.display='block';
      var x=Math.min(e.clientX+24,window.innerWidth-prev.offsetWidth-12);
      var y=Math.min(e.clientY+24,window.innerHeight-prev.offsetHeight-12);
      prev.style.left=Math.max(8,x)+'px';prev.style.top=Math.max(8,y)+'px';
    });
    img.addEventListener('mouseleave',function(){prev.style.display='none';});
  });
})();
</script>
<script>window.MathJax={tex:{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$'],['\\\\[','\\\\]']]},options:{skipHtmlTags:['script','noscript','style','textarea','pre','code']}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
"""


def inject(path, source_url):
    try:
        html = open(path, encoding="utf-8").read()
    except Exception:
        return
    bar = '<div id="rt-bar"><a href="%s">&#8592; Back to Summaries</a>' % SUMMARIES_URL
    if source_url:
        bar += '<a href="%s" target="_blank" rel="noopener noreferrer">Read the full article &#8594;</a>' % source_url
    bar += "</div>"
    if "</head>" in html:
        html = html.replace("</head>", ENHANCE_HEAD + "</head>", 1)
    html = re.sub(r"(<body[^>]*>)", lambda m: m.group(1) + bar, html, count=1)
    if "</body>" in html:
        html = html.replace("</body>", ENHANCE_TAIL + "</body>", 1)
    else:
        html += ENHANCE_TAIL
    open(path, "w", encoding="utf-8").write(html)


def main():
    os.makedirs(DEST, exist_ok=True)
    entries = []
    for root, _dirs, files in os.walk(SRC):
        if "summary.html" not in files or "content.json" not in files:
            continue
        slug = os.path.basename(root)
        try:
            meta = json.load(open(os.path.join(root, "content.json")))
        except Exception:
            meta = {}
        title = clean(meta.get("title") or slug)
        source_type = clean(meta.get("source_type") or "")
        try:
            html = open(os.path.join(root, "summary.html"), encoding="utf-8").read(8000)
        except Exception:
            html = ""
        source_url = find_url(source_type, json.dumps(meta.get("sections", ""))[:4000], html)
        pub = derive_pub(source_url, source_type)

        out = os.path.join(DEST, slug)
        shutil.rmtree(out, ignore_errors=True)
        os.makedirs(out, exist_ok=True)
        shutil.copyfile(os.path.join(root, "summary.html"), os.path.join(out, "index.html"))
        if os.path.isdir(os.path.join(root, "assets")):
            shutil.copytree(os.path.join(root, "assets"), os.path.join(out, "assets"))
        inject(os.path.join(out, "index.html"), source_url)

        pdf = ""
        if not source_url and os.path.isfile(os.path.join(root, "source.pdf")):
            shutil.copyfile(os.path.join(root, "source.pdf"), os.path.join(out, "source.pdf"))
            pdf = "/summaries/%s/source.pdf" % slug

        try:
            mtime = time.strftime("%Y-%m-%d", time.gmtime(os.path.getmtime(os.path.join(root, "summary.html"))))
        except Exception:
            mtime = ""

        tags = meta.get("tags") or []
        if not isinstance(tags, list):
            tags = []
        entries.append({
            "slug": slug, "title": title, "source_type": source_type,
            "source_url": source_url, "pdf": pdf, "tags": tags, "pub": pub,
            "url": "/summaries/%s/" % slug, "date": slug_date(slug, mtime),
        })

    entries.sort(key=lambda e: e["date"], reverse=True)
    lines = [
        "# Published summaries. Generated by automation/publish-summaries.py.",
        "# Do not edit by hand; rerun the publisher.",
        "",
    ]
    for e in entries:
        for k in ("slug", "title", "url", "date", "pub", "source_type", "source_url", "pdf"):
            prefix = "- " if k == "slug" else "  "
            lines.append('%s%s: "%s"' % (prefix, k, yaml_escape(e[k])))
        tag_items = ", ".join('"%s"' % yaml_escape(t) for t in e.get("tags", []))
        lines.append('  tags: [%s]' % tag_items)
    open(MANIFEST, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("published %d summaries -> %s" % (len(entries), MANIFEST))


if __name__ == "__main__":
    main()
