"""Gera artes GAP no padrão aprovado (foto em tela cheia + moldura GAP + selo de preço + CTA).
Uso: python3 make_art.py variants.json saida_dir
variants.json = {"ID": {IMG, POS, SHADEH, H1, SEALB, CHIP, SEALTOP, PRICE, H1TXT, SUB, TAGS, CTA}, ...}
IMG = arquivo dentro de toolkit/photos/ (foto real Pexels/Unsplash, tratada com grade.py)
"""
import sys, json, os
from playwright.sync_api import sync_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
TPL = r"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
@font-face{font-family:"Montserrat";font-weight:900;src:url(fonts/montserrat-latin-900-normal.woff2)}
@font-face{font-family:"Montserrat";font-weight:800;src:url(fonts/montserrat-latin-800-normal.woff2)}
@font-face{font-family:"Manrope";font-weight:500;src:url(fonts/manrope-latin-500-normal.woff2)}
@font-face{font-family:"Manrope";font-weight:700;src:url(fonts/manrope-latin-700-normal.woff2)}
@font-face{font-family:"Manrope";font-weight:800;src:url(fonts/manrope-latin-800-normal.woff2)}
:root{--ink:#171724;--purple:#9a20d1;--pink:#ed2d9b;--cyan:#14bfd0;--green:#36d663;--yellow:#ffd83d;--orange:#ff6b20}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden;background:#fff}
body{position:relative;font-family:Manrope,sans-serif;color:#fff}
/* moldura nas cores da GAP */
.frame{position:absolute;inset:0;padding:18px;
  background:conic-gradient(from 210deg at 50% 50%,var(--purple),var(--pink),var(--orange),var(--yellow),var(--green),var(--cyan),var(--purple))}
.inner{position:relative;width:100%;height:100%;border-radius:30px;overflow:hidden}
.photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:__POS__}
.shade-top{position:absolute;left:0;right:0;top:0;height:300px;background:linear-gradient(180deg,rgba(10,8,25,.55),rgba(10,8,25,0))}
.shade-bot{position:absolute;left:0;right:0;bottom:0;height:__SHADEH__px;
  background:linear-gradient(0deg,rgba(14,10,34,.92) 0%,rgba(14,10,34,.78) 38%,rgba(14,10,34,0) 100%)}
.logo{position:absolute;left:44px;top:40px;height:150px}
.chip{position:absolute;right:44px;top:52px;background:rgba(255,255,255,.95);color:var(--ink);border-radius:999px;
  padding:14px 22px;font:800 22px/1 Manrope;display:flex;gap:10px;align-items:center;box-shadow:0 10px 28px rgba(0,0,0,.18)}
.chip i{width:12px;height:12px;border-radius:50%;background:var(--green);display:block}
.copy{position:absolute;left:54px;right:54px;bottom:54px}
h1{font:900 __H1__px/.92 Montserrat;letter-spacing:-.05em;text-shadow:0 4px 30px rgba(0,0,0,.25)}
h1 em{font-style:normal;color:var(--yellow)}
.sub{margin-top:22px;font:700 31px/1.32 Manrope;color:rgba(255,255,255,.92);max-width:760px}
.row{margin-top:34px;display:flex;align-items:center;gap:22px}
.btn{background:#fff;color:var(--ink);border-radius:999px;padding:25px 38px;font:800 31px/1 Manrope;
  box-shadow:0 12px 30px rgba(0,0,0,.25);display:flex;gap:14px;align-items:center}
.btn b{width:38px;height:38px;border-radius:50%;background:linear-gradient(120deg,var(--purple),var(--pink),var(--orange));
  color:#fff;font:900 24px/38px Montserrat;text-align:center}
.url{font:800 28px/1 Manrope}
.seal{position:absolute;right:46px;bottom:__SEALB__px;width:232px;height:232px;border-radius:50%;
  background:var(--yellow);color:var(--ink);transform:rotate(-10deg);display:flex;flex-direction:column;align-items:center;justify-content:center;
  box-shadow:0 16px 40px rgba(0,0,0,.30);border:6px solid #fff}
.seal small{font:800 21px/1.05 Manrope;text-align:center}
.seal b{font:900 84px/.9 Montserrat;letter-spacing:-.05em;margin:4px 0}
.seal span{font:800 19px/1 Manrope}
.tags{margin-top:20px;display:flex;gap:10px;flex-wrap:wrap}
.tags span{border:2px solid rgba(255,255,255,.75);border-radius:999px;padding:9px 16px;font:800 21px/1 Manrope}
</style></head><body>
<div class="frame"><div class="inner">
  <img class="photo" src="photos/__IMG__" alt="">
  <div class="shade-top"></div><div class="shade-bot"></div>
  <img class="logo" src="gap_logo_original.png" alt="GAP Mobile">
  <div class="chip"><i></i>__CHIP__</div>
  <div class="seal"><small>__SEALTOP__</small><b>$__PRICE__</b><span>USD</span></div>
  <div class="copy">
    <h1>__H1TXT__</h1>
    <p class="sub">__SUB__</p>
    <div class="tags">__TAGS__</div>
    <div class="row"><span class="btn"><b><svg width="20" height="20" viewBox="0 0 20 20" style="margin-top:9px"><path d="M4 10h11M10 4l6 6-6 6" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></b>__CTA__</span><span class="url">gapsim.com</span></div>
  </div>
</div></div>
</body></html>"""

def render(html_path, out):
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
        pg.goto('file://'+html_path); pg.wait_for_timeout(600)
        pg.screenshot(path=out, type='jpeg', quality=92); b.close()

if __name__=='__main__':
    variants=json.load(open(sys.argv[1])); outdir=os.path.abspath(sys.argv[2]); os.makedirs(outdir,exist_ok=True)
    for key,v in variants.items():
        html=TPL
        for k,val in v.items(): html=html.replace(f"__{k}__",str(val))
        hp=os.path.join(HERE,f"_tmp_{key}.html"); open(hp,'w').write(html)
        render(hp, os.path.join(outdir,f"{key}.jpg")); os.remove(hp); print('ok',key)
