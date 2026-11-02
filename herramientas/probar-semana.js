// Prueba rápida de UNA semana de Audio Técnica en móvil (390 px).
// Uso:  node herramientas/probar-semana.js 1-6-3        (clave de la semana)
//       node herramientas/probar-semana.js 1-6-3 --foto  (además guarda una captura del paso Ver)
// Requiere Playwright (en el entorno en la nube ya viene instalado).
const path = require('path');
const { chromium } = require('playwright');
(async () => {
  const k = process.argv[2];
  if (!k) { console.log('Falta la clave. Ejemplo: node herramientas/probar-semana.js 1-6-3'); process.exit(1); }
  const foto = process.argv.includes('--foto');
  const url = 'file://' + path.resolve(__dirname, '..', 'plataforma-arp.html');
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 390, height: 844 } });
  const errs = [];
  p.on('pageerror', e => errs.push(e.message));
  p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.goto(url); await p.waitForTimeout(300);
  const info = await p.evaluate(k => {
    if (!LD[k]) return { falta: true };
    // Desbloquea todo lo anterior: semanas hechas y evaluaciones aprobadas
    const [l] = k.split('-').map(Number);
    for (let n = 0; n <= l; n++) {
      atKeys(n).forEach(x => { if (x !== k && (n < l || atKeys(n).indexOf(x) < atKeys(n).indexOf(k))) S.done[x] = true; });
      if (n < l && LD[atEv(n)]) { const Q = LD[atEv(n)].q; S.ls[atEv(n)] = { ans: Q.map(q => q[2]), score: Q.length, fix: {}, status: 'review' }; }
    }
    S.mode = 'adult'; S.cur = k; go('leccion');
    return { bloqueada: atLocked(k), t: LD[k].t, preguntas: LD[k].q.length, correctas: LD[k].q.map(q => q[2]).join(','), retro: LD[k].q.every(q => (q[3] || '').length > 15) };
  }, k);
  if (info.falta) { console.log('No existe contenido para la clave ' + k + ' (¿falta ATC[\'' + k + '\']?).'); await b.close(); process.exit(1); }
  const painted = new Set(); const wide = [];
  for (let st = 0; st < 5; st++) {
    await p.evaluate(st => { S.ls[S.cur] = Object.assign(S.ls[S.cur] || {}, { step: st }); lec(); document.querySelectorAll('.atlec').forEach(d => d.open = true); }, st);
    await p.waitForTimeout(150);
    const w = await p.evaluate(() => document.documentElement.scrollWidth); if (w > 390) wide.push('paso ' + (st + 1) + ': ' + w + ' px');
    (await p.$$eval('#lec-body .nt', e => e.map(s => ((s.previousSibling && s.previousSibling.textContent || '').slice(-18) + '[' + s.textContent + ']' + (s.nextSibling && s.nextSibling.textContent || '').slice(0, 14)).replace(/\s+/g, ' ')))).forEach(x => painted.add(x));
    if (st === 0 && foto) await p.screenshot({ path: 'semana-' + k + '-ver.png', fullPage: true });
  }
  await p.evaluate(() => go('home'));
  console.log('Semana:', info.t);
  console.log('Bloqueada con lo anterior completo:', info.bloqueada ? 'SÍ (revisar)' : 'no');
  console.log('Preguntas:', info.preguntas, '| retroalimentación en todas:', info.retro ? 'sí' : 'NO', '| posición de la correcta:', info.correctas);
  console.log('Desborde horizontal:', wide.length ? wide.join(', ') : 'ninguno');
  console.log('Notas pintadas (revisa que sean notas de verdad):', painted.size ? [...painted].join(' | ') : 'ninguna');
  console.log('Errores de consola:', errs.length ? errs.join(' | ') : 'ninguno');
  if (foto) console.log('Captura: semana-' + k + '-ver.png');
  await b.close();
  process.exit(errs.length || wide.length || info.bloqueada ? 1 : 0);
})();
