# Academia de Música ARPA (AMA)

Proyecto de Fermín Bósquez McKenzie y Dawn de Bosquez.

- `plataforma-arp.html`: plataforma del estudiante (un solo archivo, modo niños/adultos, símbolos y ayuda).
- Zona Exploradores (niños desde 9 años): dentro de `plataforma-arp.html`, en la lista `KIDS`. En modo Explorador, la pestaña «Clases» cambia a «🚀 Misiones». Cada misión usa los mismos 5 pasos de la lección, el metrónomo y los gráficos. Para agregar una, copia un objeto de `KIDS`; los campos están explicados en el comentario de arriba de la lista. Las notas se escriben con `<n>Sol</n>`.
- Audio Técnica Básica para Músicos (antes «Audiotécnica para músicos»): misma asignatura y mismas claves, en `plataforma-arp.html` (bloque «AUDIO TÉCNICA BÁSICA PARA MÚSICOS»). 14 semanas en 3 niveles (5 + 5 + 4), una evaluación por nivel y proyecto final en el Nivel 3. Las semanas se abren en orden; aprobar la evaluación de un nivel abre el siguiente. La nota mínima y el número de intentos están en la configuración académica (`ACAD_DEF`: 70 % e intentos ilimitados) y se pueden cambiar sin tocar el código guardando la clave `arp-config` en el navegador, por ejemplo `{"asignaturas":{"audio-tecnica":{"aprobar":75,"intentos":3}}}`. El contenido de cada semana se carga en `ATC` con su clave (Nivel 1 `0-5-*`, Nivel 2 `1-6-*`, Nivel 3 `2-6-*`); mientras no tenga contenido aparece como «Contenido pendiente».
- `landing/Main.dc.html`: página pública de la academia (contactos, CVs y fotos aún son marcadores).

Artifacts publicados en claude.ai:
- Plataforma: https://claude.ai/artifact/WJNwYKDShseYxAFLTbHmxS
- Landing: https://claude.ai/artifact/4LjpX8b9o1aJpnmEB2GAxy

Pendiente: datos reales de contacto, fotos y nombres de docentes.
