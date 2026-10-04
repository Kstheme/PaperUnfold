// Optional artifact check. Supply an installed Playwright module and browser.
// node tests/check_guide_browser.cjs <playwright-module> <browser-exe> <guide.html> [prompts.json]
const fs = require('node:fs');
const path = require('node:path');
const [modulePath, executablePath, artifact, promptOutput] = process.argv.slice(2);
if (!modulePath || !executablePath || !artifact) {
  console.error('Supply Playwright module, browser executable, and saved HTML.');
  process.exit(1);
}
const { chromium } = require(path.resolve(modulePath));
(async () => {
  const browser = await chromium.launch({ executablePath, headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
    const content = fs.readFileSync(artifact, 'utf8');
    const requests = [];
    page.on('request', request => requests.push(request.url()));
    await page.context().setOffline(true);
    await page.setContent(content);
    await page.evaluate(() => document.fonts.ready);
    const mathCount = await page.locator('.katex').count();
    if (content.includes('renderMathInElement')) {
      if (!mathCount) {
        throw new Error('Mathematics failed to render offline');
      }
      if (await page.locator('.katex-error').count()) throw new Error('Invalid example mathematics');
      if (await page.locator('blockquote .katex, pre .katex').count()) {
        throw new Error('Source text was altered by mathematics rendering');
      }
    }
    if (requests.length) throw new Error('Saved guide attempted network requests');
    for (const image of await page.locator('.visual img').all()) {
      if (!await image.evaluate(element => element.complete && element.naturalWidth > 0 && Boolean(element.alt))) {
        throw new Error('Embedded source figure is unreadable or lacks an accessible description');
      }
    }
    for (const details of await page.locator('details').all()) {
      await details.evaluate(element => {
        for (let ancestor = element.parentElement; ancestor; ancestor = ancestor.parentElement) {
          if (ancestor.tagName === 'DETAILS') ancestor.open = true;
        }
      });
      const before = await details.evaluate(element => element.open);
      await details.locator(':scope > summary').click();
      const after = await details.evaluate(element => element.open);
      if (before === after) throw new Error('Expansion control did not toggle');
      await details.locator(':scope > summary').click();
    }
    const handoffs = page.locator('.teaching-prompt');
    if (!await handoffs.count()) throw new Error('No chapter/term teaching prompts');
    const prompts = [];
    for (const handoff of await handoffs.all()) {
      await handoff.evaluate(element => {
        element.open = true;
        for (let ancestor = element.parentElement; ancestor; ancestor = ancestor.parentElement) {
          if (ancestor.tagName === 'DETAILS') ancestor.open = true;
        }
      });
      const textarea = handoff.locator('textarea');
      const prompt = await textarea.inputValue();
      if (!prompt.includes('$paper-tutor') || !prompt.trim()) throw new Error('Unusable teaching prompt');
      prompts.push({ id: await textarea.getAttribute('id'), prompt });
      await page.evaluate(() => Object.defineProperty(navigator, 'clipboard', { configurable: true, value: undefined }));
      await handoff.locator('button').click();
      const fallback = await handoff.getAttribute('data-fallback');
      await handoff.locator('[role="status"]').getByText(fallback, { exact: true }).waitFor();
      if (!await textarea.evaluate(element => document.activeElement === element && element.selectionStart === 0 && element.selectionEnd === element.value.length)) {
        throw new Error('Clipboard fallback did not select the complete teaching prompt');
      }
      // Exercise the success branch with a stub, not a claim about OS clipboard support.
      await page.evaluate(() => Object.defineProperty(navigator, 'clipboard', { configurable: true,
        value: { writeText: async text => { window.testCopiedPrompt = text; } } }));
      await handoff.locator('button').click();
      await handoff.locator('[role="status"]').getByText(await handoff.getAttribute('data-success'), { exact: true }).waitFor();
      if (await page.evaluate(() => window.testCopiedPrompt) !== prompt) throw new Error('Copy payload differs from visible prompt');
    }
    if (promptOutput) fs.writeFileSync(promptOutput, JSON.stringify(prompts, null, 2));
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
    await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
    if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth)) {
      const overflowing = await page.evaluate(() => [...document.querySelectorAll('*')]
        .filter(element => element.getBoundingClientRect().right > innerWidth)
        .slice(0, 5).map(element => `${element.tagName}.${element.className}`));
      throw new Error(`Guide overflows mobile viewport: ${overflowing.join(', ')}`);
    }
    const noJsContext = await browser.newContext({ javaScriptEnabled: false });
    const noJsPage = await noJsContext.newPage();
    await noJsContext.setOffline(true);
    await noJsPage.setContent(content);
    const noJsPrompt = noJsPage.locator('.teaching-prompt').first();
    await noJsPrompt.locator(':scope > summary').click();
    await noJsPrompt.locator('textarea').focus();
    await noJsPage.keyboard.press('Control+A');
    if (!await noJsPrompt.locator('textarea').evaluate(element => element.selectionEnd === element.value.length && element.selectionStart === 0)) {
      throw new Error('JavaScript-disabled guide has no selectable copy fallback');
    }
    await noJsContext.close();
    console.log(JSON.stringify({ controls: await page.locator('details').count(), anchors: links.length,
      navigation: true, mobileOverflow: false, mathCount, networkRequests: requests.length,
      explanatoryVisuals: await page.locator('.visual').count(), sourceImages: await page.locator('.visual img').count(),
      teachingPrompts: prompts.length, clipboardFallback: true, noJavaScriptCopyFallback: true,
      clipboardSuccessStub: true, actualClipboardTested: false }));
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
