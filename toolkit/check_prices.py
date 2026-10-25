"""Lê os preços atuais exibidos em gapsim.com (página renderizada) antes de cada arte."""
import os, re, json
from playwright.sync_api import sync_playwright
proxy = os.environ.get('HTTPS_PROXY') or os.environ.get('https_proxy')
with sync_playwright() as p:
    b = p.chromium.launch(proxy={'server': proxy} if proxy else None)
    pg = b.new_page(ignore_https_errors=True)
    pg.goto('https://gapsim.com', wait_until='networkidle', timeout=60000); pg.wait_for_timeout(2500)
    cards = pg.eval_on_selector_all('#planos article, .plan-card, [class*=plan]',
        'els => els.map(e => e.innerText).filter(t => /A PARTIR DE|a partir de/i.test(t))')
    hero = pg.inner_text('body')[:600]
    b.close()
seen = []
for c in cards:
    t = ' '.join(c.split())
    m = re.search(r'(ESIM \w+)\s+(USA|EUROPA|GLOBAL)\b.*?A PARTIR DE\s*\$?\s*([\d.,]+)', t, re.I)
    if m:
        row = (m.group(1).upper(), m.group(2).upper(), m.group(3))
        if row not in seen: seen.append(row)
print(json.dumps(seen, ensure_ascii=False))
print('HERO:', ' '.join(hero.split())[:400])
