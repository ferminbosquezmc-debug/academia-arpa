#!/usr/bin/env python3
"""Carga las clases de Guitarra Niveles 2 y 3 (clases 13–36) en plataforma-arp.html.
Lee los .md de academia-musica-ama/contenido/guitarra/nivel-2 y nivel-3 y reescribe la línea `const GNC23=[...];`.
Uso: python3 herramientas/guitarra_n23.py [carpeta de contenido/guitarra]"""
import sys, os, re, json
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..', '..', 'academia-musica-ama', 'contenido', 'guitarra')
HTML = os.path.join(os.path.dirname(__file__), '..', 'plataforma-arp.html')
arr = []
for n in range(13, 37):
    f = os.path.join(SRC, 'nivel-2' if n <= 24 else 'nivel-3', f'clase-{n}.md')
    if os.path.exists(f):
        arr.append({'n': n, 'raw': open(f, encoding='utf-8').read().replace('\r', '')})
js = 'const GNC23=' + json.dumps(arr, ensure_ascii=False).replace('</', '<\\/') + ';'
t = open(HTML, encoding='utf-8').read()
new, k = re.subn(r'(?m)^const GNC23=\[.*\];$', lambda m: js, t)
if k != 1: sys.exit(f'Se esperaba una línea const GNC23 y hay {k}')
open(HTML, 'w', encoding='utf-8').write(new)
print('Clases cargadas:', [a['n'] for a in arr])
