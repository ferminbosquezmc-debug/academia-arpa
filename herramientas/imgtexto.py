#!/usr/bin/env python3
"""Extrae el texto de las láminas SVG y reescribe `const IMGTX=` en plataforma-arp.html.
Así el lector («Escuchar la clase») puede leer lo que dicen las imágenes.
Uso: python3 herramientas/imgtexto.py  (desde la carpeta academia-arpa). Con --check solo compara."""
import json, re, sys, glob, xml.etree.ElementTree as ET
DIRS = ['guitarra/img', 'guitarra/atlas', 'piano/img', 'bateria/img', 'bajo/img', 'canto/img']
def words(f):
    try: root = ET.parse(f).getroot()
    except ET.ParseError: return ''
    out = []
    for el in root.iter():
        if el.tag.split('}')[-1] != 'text': continue
        t = re.sub(r'\s+', ' ', ''.join(el.itertext())).strip()
        # solo textos con palabras (2 letras seguidas o más): se omiten números de dedos y letras sueltas
        if len(re.findall(r'[A-Za-zÁÉÍÓÚÑáéíóúñü]{2,}', t)) == 0: continue
        if out and out[-1] == t: continue
        out.append(t)
    s = ' · '.join(dict.fromkeys(out))
    return s[:600]
m = {}
for d in DIRS:
    for f in sorted(glob.glob(d + '/*.svg')):
        t = words(f)
        if t: m[f] = t
p = 'plataforma-arp.html'; h = open(p, encoding='utf-8').read()
line = 'const IMGTX=' + json.dumps(m, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + ';'
new = re.sub(r'^const IMGTX=.*;$', lambda _: line, h, count=1, flags=re.M)
if '--check' in sys.argv:
    print('igual' if new == h else 'distinto'); sys.exit(0)
if new == h and 'const IMGTX=' not in h: sys.exit('Falta la línea const IMGTX= en el HTML')
open(p, 'w', encoding='utf-8').write(new)
print(len(m), 'imágenes con texto ·', len(line)//1024, 'KB')
