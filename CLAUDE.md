# Academia de Música ARPA (AMA) — instrucciones para Claude

Responde en español, breve y claro. El dueño del proyecto es principiante: explica en pasos simples y sin tecnicismos innecesarios.

## Archivos
- `plataforma-arp.html`: plataforma del estudiante. Un solo archivo HTML + CSS + JS puro, sin librerías. Estado en `localStorage` (clave `arp`, objeto `S`). Vistas: home, clases, practica, biblioteca, leccion, perfil, ninos, asig. Se navega con `go('vista')`.
- La página pública no está aquí: vive en el repositorio `academia-musica-ama`.
- `herramientas/probar-semana.js`: prueba rápida de una semana.

## Versión oficial (una sola)
- La versión oficial es `plataforma-arp.html` en `main` de GitHub. Todo cambio se hace aquí primero (rama → pruebas → merge a `main` → push).
- El enlace de claude.ai (https://claude.ai/artifact/WJNwYKDShseYxAFLTbHmxS) es solo una copia publicada: se actualiza publicando este archivo desde `main`, sin pasar `capabilities` (así se conserva la base de datos del Nivel 4). Nunca se edita ahí directamente.
- Antes de publicar: `git pull origin main` y lee el enlace (acción read). Si el enlace tiene algo que no está en `main`, primero tráelo a `main` y después publica.
- No crees copias nuevas (otros archivos, otros enlaces o carpetas) de la plataforma ni de la página pública.

## Reglas generales
- Lee solo la parte del código que vas a tocar (usa `grep -n` para ubicarla). No leas el archivo completo.
- Cambios pequeños. Después de cada cambio: validar la sintaxis y probar en móvil (390 px) sin errores de consola.
- Derechos de autor: todo en palabras propias, ejemplos y gráficos originales (SVG/HTML propios). Nunca copiar textos, imágenes ni ejercicios de libros o de otras academias. Datos técnicos estándar sí (y marcar como «aproximados» los rangos que varían).
- No inventar contactos, nombres ni datos de estudiantes. No guardar llaves ni contraseñas.
- Colores de las notas: Do rojo, Re naranja, Mi amarillo, Fa verde claro, Sol celeste, La azul oscuro, Si morado (función `nc()`, sistema tipo Boomwhackers). Las teclas negras del piano (sostenidos y bemoles) van en negro. En contenido nuevo escribe las notas con `<n>Sol</n>`; usa `<span data-nn>` para impedir que algo se pinte. Cuidado: el pintor automático colorea frases como «La mayor parte» o «Si fallas» si siguen ciertos patrones; revisa la salida del probador.

## Ahorro de créditos (pedido del dueño)
- No tomes ni revises capturas salvo que el dueño las pida. Usa el probador de texto.
- Prueba solo la semana nueva (`probar-semana.js`), no toda la plataforma.
- Une cada semana a `main` cuando sus pruebas pasen, sin pedir confirmación, y da un resumen corto al final.

## Carrera «Audio Técnica · Sonido en Vivo»
Antes «Audio Técnica Básica para Músicos». Es una **carrera aparte** de las carreras de instrumentos: no aparece en Clases ni cuenta en el avance de instrumentos (`isAT(l,si)`); se entra desde el botón de Inicio (`.athome`, vista `asig`). En el código sigue en `LEV` solo para conservar sus claves. Bloque en `plataforma-arp.html` que empieza con el comentario `AUDIO TÉCNICA BÁSICA PARA MÚSICOS`.

**Plan aprobado por el dueño (completo):** 3 niveles de 12 semanas (3 meses) cada uno; la semana 12 de cada nivel es su evaluación. Total: 33 semanas de contenido + 3 evaluaciones = 36 semanas.
- Nivel 1 · Fundamentos: Sonido · *Oído y cuidado auditivo* · Micrófonos · Uso de micrófonos · Cables · *Electricidad y seguridad* · *Altavoces y amplificadores* · Consola · *Consola digital* · *Montar un sistema pequeño* · *Práctica integradora* · Evaluación.
- Nivel 2 · Control y mezcla: Ganancia · Ecualización · Ecualización práctica · *Compresor y compuerta* · Efectos · Monitores · *In-ear a fondo* · *Microfonía de batería y coro* · *Mezcla en vivo* · *Grabar el evento* · *Práctica integradora* · Evaluación.
- Nivel 3 · Sonido profesional: Acoples · *Sistemas de sala* · *Acústica de iglesias y salones* · Trabajo en equipo · Prueba de sonido · *Lista de canales y rider* · *Transmisión en vivo* · *Fallas y mantenimiento* · *Dirigir un equipo de sonido* · *Eventos especiales* · Repaso final · Proyecto final.
(En cursiva, semanas nuevas.) Las claves existentes no cambian; el progreso guardado de los estudiantes debe conservarse.

Avance del plan: **Nivel 1 completo** (claves nuevas `0-5-b1`…`b6`; evaluación de 40 preguntas en la semana 12). **Nivel 2 completo** (claves nuevas `1-6-b1` Compresor y compuerta, `b2` In-ear, `b3` Batería y coro, `b4` Mezcla en vivo, `b5` Grabar el evento, `b6` Práctica integradora; Efectos `4` va antes de Monitoreo `3`; evaluación de 40 preguntas en la semana 24). **Nivel 3 completo** (nuevas `2-6-b1` Sistemas de sala, `b2` Acústica, `b3` Lista de canales y rider, `b4` Transmisión en vivo, `b5` Fallas y mantenimiento, `b6` Dirigir un equipo, `b7` Eventos especiales; `ks:['0','b1','b2','1','2','b3','b4','b5','b6','b7','3']`). La evaluación final `2-6-ev` (semana 36) repasa toda la carrera con 34 preguntas: por cada semana nueva del N3 se agregaron 2 preguntas (no 4).
- Cada nivel de `AT` tiene descripción (`d`), objetivos (`obj`), títulos (`m`), temas por semana (`tm`) y, si tiene semanas nuevas, `ks`: la lista de claves en orden (las originales conservan su número; las nuevas usan `b1`, `b2`…). Ejemplo Nivel 1: `ks:['0','b1','1','2','3','b2','b3','4','b4','b5','b6']`.
- **Para insertar una semana nueva:** agrega su título en `m`, sus temas en `tm` y su clave en `ks`, todos en la misma posición; usa la siguiente clave libre (`b2`, `b3`…). Nunca renombres las claves existentes.
- Claves originales (no cambiarlas): Nivel 1 `0-5-0`…`0-5-4` y `0-5-ev`; Nivel 2 `1-6-0`…`1-6-4` y `1-6-ev`; Nivel 3 `2-6-0`…`2-6-3` y `2-6-ev`. `atKeys(nivel)` las devuelve en orden; `atPos(clave)` da la posición; `atTotal()` el total de semanas.
- Numeración: las semanas se numeran solas en toda la carrera, y la evaluación de cada nivel cuenta como una semana (N1 termina en la 12; N2 empieza en la 13). El contenido antiguo dice «Semana N» con la numeración original (1 a 14) y `atLoad` lo traduce (`AT_OLD`). **En contenido nuevo no escribas «Semana N»: usa `{{w:clave}}`** (por ejemplo `{{w:0-5-b1}}`), que se convierte en el número actual. Marca el objeto nuevo con `nw:1`.
- Si una semana nueva entra en un nivel, agrega 4 preguntas sobre ella en la evaluación del nivel y una línea en su repaso.
- Reglas en `ACAD_DEF` (aprobar 70 %, intentos ilimitados; configurable con la clave `arp-config` del navegador). Las semanas se abren en orden; aprobar la evaluación de un nivel abre el siguiente.
- Estado: todas las semanas listadas en `AT` tienen contenido, más las Evaluaciones de los Niveles 1 y 2, y Proyecto práctico y evaluación final (`2-6-ev`, con `proyecto`; se completa al aprobar y entregar el proyecto).

### Cómo agregar una semana
1. Busca el final de la semana anterior: `grep -n "^ATC\['0-5-" plataforma-arp.html` y ubica su última línea `e:'…'};`. Revisa que los nombres de tus variables no existan ya (`grep -n "const NOMBRE"`).
2. Inserta justo después: primero las herramientas propias de la semana (dibujos y demostración), luego el objeto `ATC['<clave>']={…}` con este formato:
   - `intro` (HTML), `demo` (función que devuelve una tarjeta interactiva; opcional), `obj` (lista de objetivos),
   - `lecciones`: `[{t:'Título',html:'…'}]` — una por cada tema de `AT[n].tm[i]`,
   - `ilus` (opcional), `ej` (ejemplos del entorno musical, HTML), `act` (6 actividades),
   - `prac`: `()=>chBox('id','Ejercicio: …','intro',LISTA,OPCIONES,'pista')` con 5 situaciones `[situación, clave correcta, explicación]`,
   - `glos`: `[['término','definición'],…]` (unos 15),
   - `q`: 10 preguntas `[pregunta,[3 opciones],0,'retroalimentación']` — escribe la correcta en la posición 0; `atMix` la cambia de lugar sola,
   - `res` (resumen HTML) y `e` (qué entrega el estudiante).
3. Si la demostración usa controles: agrega su manejador en los escuchas de `#v-leccion` (`click` con `data-…`, `input` por `id`). Si suena, crea una función `…Stop()` y llámala en `go()` y al cambiar de paso (igual que `sgStop` y `eqStop`).
4. Herramientas reutilizables: `card`, `tips([[error,corrección]])`, `flow([pasos],'título')`, `chBox`, clases CSS `mcg/mcc` (tarjetas), `mug/muc` (lista con símbolo), `attb` (tabla), `atwarn` (aviso). Demostraciones existentes: generador de tonos (`SG`), patrones polares (`PP`), distancia (`DD`), cable balanceado (`BN`), canal de consola (`CS`), ganancia (`GS`), ecualizador que suena (`EQ`, con ajustes `EQPRE`), mezcla de monitor (`MX`), efectos que suenan (`FX`, se apaga con `fxStop`), simulador de acople (`FB`, no suena), constructor de pedidos (`RQ`, con selects), ordenar la prueba de sonido (`SC`).

### Probar y publicar
```
sed -n '/<script>/,/<\/script>/p' plataforma-arp.html | sed '1d;$d' > /tmp/p.js && node --check /tmp/p.js
node herramientas/probar-semana.js <clave>
```
El probador desbloquea lo anterior, recorre los 5 pasos y muestra: bloqueo, preguntas, desborde, notas pintadas y errores. Debe terminar sin errores ni desborde.

Ojo: escribe «ponderación <span data-nn>C</span>» y letras sueltas parecidas con `data-nn`; el pintor las toma por notas.

Git: rama `at-semana-N` → commit con mensaje claro → `git fetch origin` (otra sesión pudo subir cambios) → merge `--no-ff` a `main` → probar de nuevo → push.

## Juegos de práctica (vista Práctica)
Bloque JS que empieza con el comentario `Juegos de práctica`; CSS con prefijo `jg-`; HTML dentro de `<div data-nn>` en `#v-practica` (para que el pintor no toque los textos de Arpi).
- Racha (`jgRacha`): usa `streak()` y los días de `S.min`, igual que el cronómetro. Recompensas en `JG_RW` (3, 7, 14, 21 y 30 días).
- Atrapa la nota (`JG`, `jgStart`, `jgStop`) y Oído musical (`EAR`). El tiempo jugado se suma a `S.min` con `jgTime` (`S.jgs` guarda los segundos sueltos; `S.jgb` es el récord).
- Arpi, la mascota: `jgSay(html, 'wow'|'sad')`. `jgStop()` se llama en `go()`.
- Arpi en las pruebas de lecciones: `arpiHint(q,i,L)` muestra la pista (`q[3]`) cuando una respuesta está por corregir; `arpiSvg(mood)` dibuja la mascota. `L.tw[i]` guarda las opciones equivocadas ya probadas al corregir (quedan descartadas; se borra al reintentar).
