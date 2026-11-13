#!/usr/bin/env python3
"""Carga las clases de Batería (Niveles 1–3, clases 1–36) en plataforma-arp.html.
Lee academia-musica-ama/contenido/bateria/nivel-N/clase-M.md y reescribe la línea `const BNC=[...];`.
Uso: python3 herramientas/bateria.py [carpeta contenido/bateria] [--check]"""
import sys, os, re, json
args = [a for a in sys.argv[1:] if not a.startswith('--')]
SRC = args[0] if args else os.path.join(os.path.dirname(__file__), '..', '..', 'academia-musica-ama', 'contenido', 'bateria')
HTML = os.path.join(os.path.dirname(__file__), '..', 'plataforma-arp.html')
arr = []
for n in range(1, 37):
    f = os.path.join(SRC, f'nivel-{(n - 1) // 12 + 1}', f'clase-{n}.md')
    if os.path.exists(f): arr.append({'n': n, 'raw': open(f, encoding='utf-8').read().replace('\r', '')})
js = 'const BNC=' + json.dumps(arr, ensure_ascii=False).replace('</', '<\\/') + ';'
t = open(HTML, encoding='utf-8').read()
m = re.search(r'(?m)^const BNC=\[.*\];$', t)
if not m: sys.exit('No encuentro la línea const BNC')
if '--check' in sys.argv:
    old = json.loads(m.group(0)[len('const BNC='):-1])
    for o in old:
        a = next((x for x in arr if x['n'] == o['n']), None)
        print(o['n'], 'igual' if a and a['raw'] == o['raw'] else 'DISTINTA')
    sys.exit()
open(HTML, 'w', encoding='utf-8').write(t[:m.start()] + js + t[m.end():])
print('Clases cargadas:', [a['n'] for a in arr])
