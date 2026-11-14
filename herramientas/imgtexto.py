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
    out = list(dict.fromkeys(out))
    # un renglón que empieza en minúscula es el detalle del anterior: se unen («Pies planos en el suelo: firmes…»)
    res, merged = [], set()
    for t in out:
        i = len(res) - 1
        if i >= 1 and i not in merged and t[:1].islower() and len(t.split()) >= 2 and len(res[i].split()) >= 2 and len(res[i]) < 60:
            res[i] = res[i].rstrip(':') + (' ' if res[i].endswith(',') else ', ' if ':' in res[i] else ': ') + t; merged.add(i)
        else: res.append(t)
    # 3 o más renglones cortos seguidos (DO, RE, MI…) van en un solo renglón: «DO · RE · MI»
    fin, run = [], []
    for t in res + [None]:
        if t is not None and len(fin) >= 1 and len(t) <= 10: run.append(t); continue
        if len(run) >= 3: fin.append(' · '.join(run))
        else: fin.extend(run)
        run = []
        if t is not None: fin.append(t)
    return fin[:30]  # el primero es el título de la lámina
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
