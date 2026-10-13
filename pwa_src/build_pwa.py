#!/usr/bin/env python3
"""Build the installable offline app into ../pwa/ from app_template.html + subject_data.json."""
import json, shutil, time
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parent; OUT = ROOT / "pwa"
OUT.mkdir(exist_ok=True)
tpl = (ROOT / "app_template.html").read_text(encoding="utf-8")
data = json.loads((ROOT / "subject_data.json").read_text(encoding="utf-8"))
shim = (HERE / "device_shim.js").read_text(encoding="utf-8")

cdn = '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.js"></script>'
assert cdn in tpl
html = tpl.replace(cdn, "<script>\n" + shim + "\n</script>")
html = html.replace("__SUBJECT_DATA_JSON__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))

head_add = ('<link rel="manifest" href="manifest.webmanifest">\n<meta name="theme-color" content="#0f172a">\n'
            '<meta name="mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-capable" content="yes">\n'
            '<link rel="apple-touch-icon" href="icon-192.png">\n')
html = html.replace("<title>", head_add + "<title>", 1)
# no accounts on-device: drop log-out button
html = html.replace('<button class="auth-btn" id="logout-btn">Log out</button>', '')
html = html.replace("document.getElementById('logout-btn').onclick = ()=> doLogout();", "")
sw_reg = ("<script>if('serviceWorker' in navigator && location.protocol.indexOf('http')===0){"
          "window.addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}));}</script>\n</body>")
assert "</body>" in html
html = html.replace("</body>", sw_reg, 1)
(OUT / "index.html").write_text(html, encoding="utf-8")
(OUT / "sw.js").write_text((HERE / "sw.js").read_text().replace("__BUILD__", str(int(time.time()))), encoding="utf-8")
for f in ["manifest.webmanifest", "icon-192.png", "icon-512.png", "icon-maskable-512.png"]:
    shutil.copy(HERE / f, OUT / f)
print("Built", OUT, len(html)//1024, "KB")
