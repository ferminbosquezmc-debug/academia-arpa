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

**Plan aprobado por el dueño:** 3 niveles de 12 semanas (3 meses) cada uno; la semana 12 es la evaluación del nivel. Hoy hay 14 semanas escritas; faltan 19 nuevas. Orden de trabajo: completar el Nivel 1, luego el 2 y el 3.
- Nivel 1 · Fundamentos: Sonido · *Oído y cuidado auditivo* · Micrófonos · Uso de micrófonos · Cables · *Electricidad y seguridad* · *Altavoces y amplificadores* · Consola · *Consola digital* · *Montar un sistema pequeño* · *Práctica integradora* · Evaluación.
- Nivel 2 · Control y mezcla: Ganancia · Ecualización · Ecualización práctica · *Compresor y compuerta* · Efectos · Monitores · *In-ear a fondo* · *Microfonía de batería y coro* · *Mezcla en vivo* · *Grabar el evento* · *Práctica integradora* · Evaluación.
- Nivel 3 · Sonido profesional: Acoples · *Sistemas de sala* · *Acústica de iglesias y salones* · Trabajo en equipo · Prueba de sonido · *Lista de canales y rider* · *Transmisión en vivo* · *Fallas y mantenimiento* · *Dirigir un equipo de sonido* · *Eventos especiales* · Repaso final · Proyecto final.
(En cursiva, semanas nuevas.) Las claves existentes no cambian; el progreso guardado de los estudiantes debe conservarse.

Estructura actual (14 semanas):
- 14 semanas en 3 niveles (`AT`): N1 semanas 1–5, N2 semanas 6–10, N3 semanas 11–14. Cada nivel tiene descripción (`d`), objetivos (`obj`), títulos (`m`) y temas por semana (`tm`).
- Claves (no cambiarlas, conservan el registro original): Nivel 1 `0-5-0`…`0-5-4` y `0-5-ev`; Nivel 2 `1-6-0`…`1-6-4` y `1-6-ev`; Nivel 3 `2-6-0`…`2-6-3` y `2-6-ev`. `atKeys(nivel)` y `atEv(nivel)` las devuelven.
- Reglas en `ACAD_DEF` (aprobar 70 %, intentos ilimitados; configurable con la clave `arp-config` del navegador). Las semanas se abren en orden; aprobar la evaluación de un nivel abre el siguiente.
- Estado actual: 14 semanas completas, Evaluaciones de los Niveles 1 y 2, y Proyecto práctico y evaluación final (`2-6-ev`, con `proyecto`; se completa al aprobar y entregar el proyecto).

### Cómo agregar una semana
1. Busca el final de la semana anterior: `grep -n "^ATC\['1-6-" plataforma-arp.html` y ubica su última línea `e:'…'};`.
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

Git: rama `at-semana-N` → commit con mensaje claro → `git fetch origin` (otra sesión pudo subir cambios) → merge `--no-ff` a `main` → probar de nuevo → push.

## Juegos de práctica (vista Práctica)
Bloque JS que empieza con el comentario `Juegos de práctica`; CSS con prefijo `jg-`; HTML dentro de `<div data-nn>` en `#v-practica` (para que el pintor no toque los textos de Arpi).
- Racha (`jgRacha`): usa `streak()` y los días de `S.min`, igual que el cronómetro. Recompensas en `JG_RW` (3, 7, 14, 21 y 30 días).
- Atrapa la nota (`JG`, `jgStart`, `jgStop`) y Oído musical (`EAR`). El tiempo jugado se suma a `S.min` con `jgTime` (`S.jgs` guarda los segundos sueltos; `S.jgb` es el récord).
- Arpi, la mascota: `jgSay(html, 'wow'|'sad')`. `jgStop()` se llama en `go()`.
- Arpi en las pruebas de lecciones: `arpiHint(q,i,L)` muestra la pista (`q[3]`) cuando una respuesta está por corregir; `arpiSvg(mood)` dibuja la mascota. `L.tw[i]` guarda las opciones equivocadas ya probadas al corregir (quedan descartadas; se borra al reintentar).
