// Optional artifact check. Supply an installed Playwright module and browser.
// node tests/check_guide_browser.cjs <playwright-module> <browser-exe> <guide.html>
const fs = require('node:fs');
const path = require('node:path');
const [modulePath, executablePath, artifact] = process.argv.slice(2);
if (!modulePath || !executablePath || !artifact) {
  console.error('Supply Playwright module, browser executable, and saved HTML.');
  process.exit(1);
}
const { chromium } = require(path.resolve(modulePath));
(async () => {
  const browser = await chromium.launch({ executablePath, headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
    await page.setContent(fs.readFileSync(artifact, 'utf8'));
    for (const details of await page.locator('details').all()) {
      const before = await details.evaluate(element => element.open);
      await details.locator('summary').click();
      const after = await details.evaluate(element => element.open);
      if (before === after) throw new Error('Expansion control did not toggle');
    }
    const links = await page.locator('a[href^="#"]').evaluateAll(elements =>
      elements.map(element => element.getAttribute('href').slice(1)));
    for (const id of links) {
      if (await page.locator(`[id="${id}"]`).count() !== 1) {
        throw new Error(`Invalid anchor: ${id}`);
      }
    }
    await page.locator('nav a').first().click();
    if (!page.url().endsWith('#thread')) throw new Error('Navigation did not reach research thread');
    await page.setViewportSize({ width: 390, height: 844 });
    if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth)) {
      throw new Error('Guide overflows mobile viewport');
    }
    console.log(JSON.stringify({ controls: await page.locator('details').count(), anchors: links.length,
      navigation: true, mobileOverflow: false }));
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
