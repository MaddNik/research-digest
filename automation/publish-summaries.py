#!/usr/bin/env python3
"""Copy summarize-anything outputs from research-material into the site and
build _data/summaries.yml. Also post-processes each published summary to add a
back bar, a "Full text" link, a figure lightbox with hover-preview on Figure N
text references, numbered display equations with hover-preview on Equation N text
references, and MathJax for equation rendering."""
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


PUBLISHERS = [
    (r"arxiv\.org", "arXiv"),
    (r"eprint\.iacr\.org|iacr\.org", "IACR ePrint"),
    (r"ieeexplore\.ieee\.org|doi\.org/10\.1109", "IEEE"),
    (r"dl\.acm\.org|doi\.org/10\.1145", "ACM"),
    (r"link\.springer\.com|doi\.org/10\.1007", "Springer"),
    (r"sciencedirect|doi\.org/10\.1016", "Elsevier"),
    (r"usenix\.org", "USENIX"),
]


def derive_publisher(source_url, source_type):
    """Best-effort publisher/repository name from the source reference."""
    blob = (source_url or "") + " " + (source_type or "")
    for pat, name in PUBLISHERS:
        if re.search(pat, blob, re.I):
            return name
    return ""


def build_meta_line(publisher, pub):
    """Single display line: publisher, then year if not already shown."""
    publisher = publisher or ""
    pub = pub or ""
    if publisher and pub and pub not in publisher:
        return "%s · %s" % (publisher, pub)
    if publisher:
        return publisher
    if pub:
        return "Published %s" % pub
    return ""


def clean(s):
    return (s or "").replace("—", " - ").replace("–", "-").strip()


def html_escape(s):
    return ((s or "").replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


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
#rt-eqprev{display:none;position:fixed;z-index:100001;max-width:60vw;max-height:50vh;padding:8px 16px;border:2px solid #888;border-radius:6px;box-shadow:0 10px 36px rgba(0,0,0,.6);pointer-events:none;background:#fff;color:#111;overflow:auto}
#rt-eqprev mjx-container,#rt-eqprev mjx-container *{color:#111!important}
a.rt-figref,a.rt-eqref{color:#1a73e8;text-decoration:none;border-bottom:1px dotted currentColor;cursor:pointer}
body{counter-reset:rt-eq}
mjx-container[display="true"]{position:relative;padding-right:2.4em}
mjx-container[display="true"]::after{counter-increment:rt-eq;content:"(" counter(rt-eq) ")";position:absolute;right:.2em;top:50%;transform:translateY(-50%);color:#999;font-size:.8em}
</style>
"""

ENHANCE_TAIL = r"""
<script>
(function(){
  var bar=document.getElementById('rt-bar');
  if(bar && window.self!==window.top){bar.style.display='none';}
  var lb=document.createElement('div');lb.id='rt-lightbox';lb.innerHTML='<img alt="">';document.body.appendChild(lb);
  lb.addEventListener('click',function(){lb.style.display='none';});
  var prev=document.createElement('img');prev.id='rt-figprev';prev.alt='';document.body.appendChild(prev);
  function showPrev(src,e){prev.src=src;prev.style.display='block';var x=Math.min(e.clientX+24,window.innerWidth-prev.offsetWidth-12);var y=Math.min(e.clientY+24,window.innerHeight-prev.offsetHeight-12);prev.style.left=Math.max(8,x)+'px';prev.style.top=Math.max(8,y)+'px';}
  function hidePrev(){prev.style.display='none';}
  var figs=document.querySelectorAll('figure'),srcByNum={};
  for(var i=0;i<figs.length;i++){
    var fig=figs[i],img=fig.querySelector('img');if(!img)continue;
    var num=i+1;fig.id='fig'+num;srcByNum[num]=img.src;
    var cap=fig.querySelector('figcaption');
    if(!cap){cap=document.createElement('figcaption');cap.style.opacity='.7';cap.style.fontSize='.85em';cap.style.marginTop='.3em';cap.textContent='Figure '+num;fig.appendChild(cap);}
    else if(!/^\s*fig/i.test(cap.textContent)){cap.textContent='Figure '+num+': '+cap.textContent;}
    (function(s){
      img.addEventListener('click',function(){lb.firstChild.src=s;lb.style.display='flex';});
    })(img.src);
  }
  var walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,null),nodes=[],nd;
  while(nd=walker.nextNode()){
    var pn=nd.parentNode;if(!pn)continue;var tg=pn.nodeName.toLowerCase();
    if(tg==='a'||tg==='pre'||tg==='code'||tg==='figcaption'||tg==='script'||tg==='style')continue;
    if(/\bfig(?:ure|\.)?\s*\d+/i.test(nd.nodeValue))nodes.push(nd);
  }
  nodes.forEach(function(node){
    var txt=node.nodeValue,re=/\b(fig(?:ure|\.)?\s*)(\d+)/gi,frag=document.createDocumentFragment(),last=0,m,used=false;
    while(m=re.exec(txt)){
      var num=parseInt(m[2],10);if(!srcByNum[num])continue;
      if(m.index>last)frag.appendChild(document.createTextNode(txt.slice(last,m.index)));
      var a=document.createElement('a');a.href='#fig'+num;a.className='rt-figref';a.textContent=m[0];
      (function(s){a.addEventListener('mousemove',function(e){showPrev(s,e);});a.addEventListener('mouseleave',hidePrev);})(srcByNum[num]);
      frag.appendChild(a);last=m.index+m[0].length;used=true;
    }
    if(used){if(last<txt.length)frag.appendChild(document.createTextNode(txt.slice(last)));node.parentNode.replaceChild(frag,node);}
  });
})();
function rtSetupEquations(){
  var prev=document.getElementById('rt-eqprev');
  if(!prev){prev=document.createElement('div');prev.id='rt-eqprev';document.body.appendChild(prev);}
  function showEq(html,e){prev.innerHTML=html;prev.style.display='block';var x=Math.min(e.clientX+20,window.innerWidth-prev.offsetWidth-12);var y=Math.min(e.clientY+20,window.innerHeight-prev.offsetHeight-12);prev.style.left=Math.max(8,x)+'px';prev.style.top=Math.max(8,y)+'px';}
  function hideEq(){prev.style.display='none';}
  var eqs=document.querySelectorAll('mjx-container[display="true"]'),htmlByNum={};
  for(var i=0;i<eqs.length;i++){var n=i+1;eqs[i].id='eq'+n;htmlByNum[n]=eqs[i].outerHTML;}
  if(!eqs.length)return;
  var walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,null),nodes=[],nd;
  while(nd=walker.nextNode()){
    var pn=nd.parentNode;if(!pn)continue;var tg=pn.nodeName.toLowerCase();
    if(tg==='a'||tg==='pre'||tg==='code'||tg==='script'||tg==='style')continue;
    if(pn.closest&&pn.closest('mjx-container'))continue;
    if(/\beq(?:uation|\.)?\s*\d+/i.test(nd.nodeValue))nodes.push(nd);
  }
  nodes.forEach(function(node){
    var txt=node.nodeValue,re=/\b(eq(?:uation|\.)?\s*)(\d+)/gi,frag=document.createDocumentFragment(),last=0,m,used=false;
    while(m=re.exec(txt)){
      var num=parseInt(m[2],10);if(!htmlByNum[num])continue;
      if(m.index>last)frag.appendChild(document.createTextNode(txt.slice(last,m.index)));
      var a=document.createElement('a');a.href='#eq'+num;a.className='rt-eqref';a.textContent=m[0];
      (function(h){a.addEventListener('mousemove',function(e){showEq(h,e);});a.addEventListener('mouseleave',hideEq);})(htmlByNum[num]);
      frag.appendChild(a);last=m.index+m[0].length;used=true;
    }
    if(used){if(last<txt.length)frag.appendChild(document.createTextNode(txt.slice(last)));node.parentNode.replaceChild(frag,node);}
  });
}
window.MathJax={tex:{inlineMath:[['$','$'],['\\(','\\)']],displayMath:[['$$','$$'],['\\[','\\]']],tags:'none'},options:{skipHtmlTags:['script','noscript','style','textarea','pre','code']},startup:{pageReady:function(){return MathJax.startup.defaultPageReady().then(function(){rtSetupEquations();});}}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
"""


def inject(path, source_url, meta_line=""):
    try:
        html = open(path, encoding="utf-8").read()
    except Exception:
        return
    # Rewrite the in-document meta line: show the publisher (not "PDF (text-layer)...")
    # and turn "full view" into a link to the article that opens in a new tab.
    if meta_line:
        if source_url:
            new_meta = ('%s &middot; <a href="%s" target="_blank" rel="noopener noreferrer">'
                        'full view &#8599;</a>' % (html_escape(meta_line), source_url))
        else:
            new_meta = html_escape(meta_line)
        html = re.sub(r'<p class="meta">.*?</p>',
                      '<p class="meta">%s</p>' % new_meta, html, count=1, flags=re.S)
    bar = '<div id="rt-bar"><a href="%s">&#8592; Back to Summaries</a>' % SUMMARIES_URL
    if source_url:
        bar += '<a href="%s" target="_blank" rel="noopener noreferrer">Full text &#8599;</a>' % source_url
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
        publisher = clean(meta.get("publisher") or derive_publisher(source_url, source_type))

        out = os.path.join(DEST, slug)
        shutil.rmtree(out, ignore_errors=True)
        os.makedirs(out, exist_ok=True)
        shutil.copyfile(os.path.join(root, "summary.html"), os.path.join(out, "index.html"))
        if os.path.isdir(os.path.join(root, "assets")):
            shutil.copytree(os.path.join(root, "assets"), os.path.join(out, "assets"))
        inject(os.path.join(out, "index.html"), source_url, build_meta_line(publisher, pub))

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
            "publisher": publisher, "meta_line": build_meta_line(publisher, pub),
            "url": "/summaries/%s/" % slug, "date": slug_date(slug, mtime),
        })

    entries.sort(key=lambda e: e["date"], reverse=True)
    lines = [
        "# Published summaries. Generated by automation/publish-summaries.py.",
        "# Do not edit by hand; rerun the publisher.",
        "",
    ]
    for e in entries:
        for k in ("slug", "title", "url", "date", "pub", "publisher", "meta_line", "source_type", "source_url", "pdf"):
            prefix = "- " if k == "slug" else "  "
            lines.append('%s%s: "%s"' % (prefix, k, yaml_escape(e[k])))
        tag_items = ", ".join('"%s"' % yaml_escape(t) for t in e.get("tags", []))
        lines.append('  tags: [%s]' % tag_items)
    open(MANIFEST, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("published %d summaries -> %s" % (len(entries), MANIFEST))


if __name__ == "__main__":
    main()
