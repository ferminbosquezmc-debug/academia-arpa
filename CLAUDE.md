# Academia de Música ARPA (AMA) — instrucciones para Claude

Responde en español, breve y claro. El dueño del proyecto es principiante: explica en pasos simples y sin tecnicismos innecesarios.

## Archivos
- `plataforma-arp.html`: plataforma del estudiante. Un solo archivo HTML + CSS + JS puro, sin librerías. Estado en `localStorage` (clave `arp`, objeto `S`). Vistas: home, clases, practica, biblioteca, leccion, perfil, ninos, asig. Se navega con `go('vista')`.
- `landing/Main.dc.html`: página pública (diseño de Claude).
- `herramientas/probar-semana.js`: prueba rápida de una semana.

## Reglas generales
- Lee solo la parte del código que vas a tocar (usa `grep -n` para ubicarla). No leas el archivo completo.
- Cambios pequeños. Después de cada cambio: validar la sintaxis y probar en móvil (390 px) sin errores de consola.
- Derechos de autor: todo en palabras propias, ejemplos y gráficos originales (SVG/HTML propios). Nunca copiar textos, imágenes ni ejercicios de libros o de otras academias. Datos técnicos estándar sí (y marcar como «aproximados» los rangos que varían).
- No inventar contactos, nombres ni datos de estudiantes. No guardar llaves ni contraseñas.
- Colores de las notas: Do rojo, Re naranja, Mi amarillo, Fa verde, Sol celeste, La azul, Si morado (función `nc()`). En contenido nuevo escribe las notas con `<n>Sol</n>`; usa `<span data-nn>` para impedir que algo se pinte. Cuidado: el pintor automático colorea frases como «La mayor parte» o «Si fallas» si siguen ciertos patrones; revisa la salida del probador.

## Ahorro de créditos (pedido del dueño)
- No tomes ni revises capturas salvo que el dueño las pida. Usa el probador de texto.
- Prueba solo la semana nueva (`probar-semana.js`), no toda la plataforma.
- Une cada semana a `main` cuando sus pruebas pasen, sin pedir confirmación, y da un resumen corto al final.

## Asignatura «Audio Técnica Básica para Músicos»
Bloque en `plataforma-arp.html` que empieza con el comentario `AUDIO TÉCNICA BÁSICA PARA MÚSICOS`.
- 14 semanas en 3 niveles (`AT`): N1 semanas 1–5, N2 semanas 6–10, N3 semanas 11–14. Cada nivel tiene descripción (`d`), objetivos (`obj`), títulos (`m`) y temas por semana (`tm`).
- Claves (no cambiarlas, conservan el registro original): Nivel 1 `0-5-0`…`0-5-4` y `0-5-ev`; Nivel 2 `1-6-0`…`1-6-4` y `1-6-ev`; Nivel 3 `2-6-0`…`2-6-3` y `2-6-ev`. `atKeys(nivel)` y `atEv(nivel)` las devuelven.
- Reglas en `ACAD_DEF` (aprobar 70 %, intentos ilimitados; configurable con la clave `arp-config` del navegador). Las semanas se abren en orden; aprobar la evaluación de un nivel abre el siguiente.
- Estado actual: Semanas 1–11 y Evaluaciones de los Niveles 1 y 2 completas. Pendientes: Semanas 12–14 y Proyecto/Evaluación final del Nivel 3 (`2-6-ev`, con `proyecto`).

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
4. Herramientas reutilizables: `card`, `tips([[error,corrección]])`, `flow([pasos],'título')`, `chBox`, clases CSS `mcg/mcc` (tarjetas), `mug/muc` (lista con símbolo), `attb` (tabla), `atwarn` (aviso). Demostraciones existentes: generador de tonos (`SG`), patrones polares (`PP`), distancia (`DD`), cable balanceado (`BN`), canal de consola (`CS`), ganancia (`GS`), ecualizador que suena (`EQ`, con ajustes `EQPRE`), mezcla de monitor (`MX`), efectos que suenan (`FX`, se apaga con `fxStop`), simulador de acople (`FB`, no suena).

### Probar y publicar
```
sed -n '/<script>/,/<\/script>/p' plataforma-arp.html | sed '1d;$d' > /tmp/p.js && node --check /tmp/p.js
node herramientas/probar-semana.js <clave>
```
El probador desbloquea lo anterior, recorre los 5 pasos y muestra: bloqueo, preguntas, desborde, notas pintadas y errores. Debe terminar sin errores ni desborde.

Git: rama `at-semana-N` → commit con mensaje claro → `git fetch origin` (otra sesión pudo subir cambios) → merge `--no-ff` a `main` → probar de nuevo → push.
