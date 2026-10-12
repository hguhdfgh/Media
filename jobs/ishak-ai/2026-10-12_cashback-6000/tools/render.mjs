// usage: node render.mjs <buildDir> <outDir> <totalFrames> <workers> [comma list of times for stills]
import { createRequire } from 'module';
import fs from 'fs'; import path from 'path';
const require = createRequire('/opt/node-tools/node_modules/');
const { chromium } = require('playwright');
const [,, B, OUT, TOTAL, W, STILLS] = process.argv;
fs.mkdirSync(OUT, { recursive: true });
const html = fs.readFileSync(path.join(B,'index.html'),'utf8').replace('__WORDS__', fs.readFileSync(path.join(B,'words.json'),'utf8'));
fs.writeFileSync(path.join(B,'_page.html'), html);
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args:['--allow-file-access-from-files','--disable-web-security'] });
const jobs = STILLS ? STILLS.split(',').map(Number).map(t=>({t, name:`still_${t.toFixed(2)}.jpg`}))
  : Array.from({length:+TOTAL},(_,i)=>({t:i/30, name:`${String(i+1).padStart(5,'0')}.jpg`}));
let next = 0; const t0 = Date.now();
async function worker(){
  const page = await browser.newPage({ viewport:{width:1080,height:1920}, deviceScaleFactor:1 });
  page.on('pageerror', e=>console.error('PAGEERR', e.message));
  await page.goto('file://'+path.join(B,'_page.html'));
  await page.evaluate(()=>window.ready);
  while(next < jobs.length){
    const j = jobs[next++];
    await page.evaluate(t=>window.render(t), j.t);
    await page.screenshot({ path: path.join(OUT,j.name), type:'jpeg', quality:95 });
    if(next % 60 === 0) console.log(next, ((Date.now()-t0)/1000).toFixed(0)+'s');
  }
}
await Promise.all(Array.from({length:+W}, worker));
await browser.close();
console.log('done', jobs.length, ((Date.now()-t0)/1000).toFixed(0)+'s');
