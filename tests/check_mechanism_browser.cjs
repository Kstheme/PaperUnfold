/* Exercise a saved artifact via the public renderer and visible browser controls. */
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const {execFileSync} = require('node:child_process');
const assert = require('node:assert/strict');
const [python, playwrightPath, edge] = process.argv.slice(2);
if (!edge) throw new Error('Usage: node check_mechanism_browser.cjs <python> <playwright-module> <edge>');
const {chromium} = require(playwrightPath);
const directory = fs.mkdtempSync(path.join(os.tmpdir(), 'paperunfold-mechanism-'));
const point = {kind: 'author', text: 'Apply softmax to scores and weight the values.', evidence: ['e1']};
const visual = {type: 'softmax', title: 'How does temperature change weights?', purpose: point,
  reading: {kind: 'analogy', text: 'Lower T emphasizes the larger fixed score.', evidence: []},
  contribution: {kind: 'analogy', text: 'Constructed teaching inputs, not paper results.', evidence: []},
  source_evidence: ['e1'], assumptions: 'Two scalar values; vary only T; fixed scores and values.',
  scores: [0, 1.0986122886681098], values: [2, 6], javascript: 'window.injected = true;'};
const guide = {title: 'Mechanism worked example', language: 'en',
  source: {name: 'Supplied mathematical passage', text: point.text, coverage: 'One passage only.', missing: []},
  evidence: [{id: 'e1', location: 'Supplied passage', quote: point.text}], thread: [point],
  sections: [{id: 'mechanism', title: 'Mechanism', role: 'Read the softmax relation.', points: [point], visuals: [visual]}], terms: []};
fs.writeFileSync(path.join(directory, 'guide.json'), JSON.stringify(guide));
execFileSync(python, [path.resolve('skills/paper-guide/scripts/render_guide.py'), path.join(directory, 'guide.json'), '--output', path.join(directory, 'guide.html')]);
const html = fs.readFileSync(path.join(directory, 'guide.html'), 'utf8');
(async () => {
  const browser = await chromium.launch({executablePath: edge, headless: true});
  try {
    const context = await browser.newContext({viewport: {width: 390, height: 844}});
    let requests = 0;
    await context.route('**/*', route => {requests++; return route.abort();});
    const page = await context.newPage();
    const errors = []; page.on('pageerror', error => errors.push(error.message));
    await page.setContent(html);
    const slider = page.locator('.softmax-demo input[type="range"]');
    assert.equal(await slider.isVisible(), true);
    const status = page.locator('.softmax-demo [role="status"]');
    // Independent worked example: exp(ln 3)=3, weights 1/4 and 3/4, y=5.
    assert.match(await status.innerText(), /0\.2500, 0\.7500.*5\.0000/);
    await slider.focus(); await page.keyboard.press('Home');
    // T=1/4: odds 3^4=81, weights 1/82 and 81/82, y=488/82.
    assert.match(await status.innerText(), /0\.0122, 0\.9878.*5\.9512/);
    await page.keyboard.press('End');
    assert.equal(await slider.inputValue(), '4');
    assert.match(await status.innerText(), /0\.4318, 0\.5682.*4\.2729/);
    assert.equal(await page.evaluate(() => window.injected), undefined);
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true);
    assert.deepEqual(errors, []); assert.equal(requests, 0);
    const staticContext = await browser.newContext({javaScriptEnabled: false});
    const staticPage = await staticContext.newPage(); await staticPage.setContent(html);
    assert.equal(await staticPage.locator('.mechanism-controls').isVisible(), false);
    assert.match(await staticPage.locator('.softmax-demo table').innerText(), /0\.2500, 0\.7500\s+5\.0000/);
    assert.match(await staticPage.locator('.softmax-demo').innerText(), /not paper results/);
    console.log('Passed: keyboard changes, independently worked weights/output, no JavaScript fallback, provenance, mobile, no network or JSON code execution.');
  } finally {
    await browser.close();
    const cleanup = path.resolve(directory);
    assert.ok(cleanup.startsWith(path.resolve(os.tmpdir()) + path.sep) &&
      path.basename(cleanup).startsWith('paperunfold-mechanism-'), 'Cleanup must stay in the test TEMP directory');
    fs.rmSync(cleanup, {recursive: true, force: true});
  }
})().catch(error => {console.error(error); process.exitCode = 1;});
