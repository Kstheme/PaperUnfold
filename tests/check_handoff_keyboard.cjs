// Actual keyboard clipboard check in an isolated browser page, not an API stub.
// node tests/check_handoff_keyboard.cjs <playwright-module> <browser-exe> <guide.html> <prompts.json> [chapter-textarea-id]
const fs = require('node:fs');
const path = require('node:path');
const [modulePath, executablePath, artifact, destination, chapterId] = process.argv.slice(2);
if (!modulePath || !executablePath || !artifact || !destination) {
  console.error('Supply Playwright module, browser executable, guide HTML, and prompt output.');
  process.exit(1);
}
if (path.resolve(artifact) === path.resolve(destination)) {
  console.error('Prompt output must differ from the input HTML.');
  process.exit(1);
}
const { chromium } = require(path.resolve(modulePath));
(async () => {
  const browser = await chromium.launch({ executablePath, headless: true });
  try {
    const page = await browser.newPage();
    await page.context().setOffline(true);
    await page.setContent(fs.readFileSync(artifact, 'utf8'));
    const prompts = [];
    const chapterSelector = chapterId ? `textarea[id="${chapterId}"]` : 'textarea[id^="teach-section-"]';
    for (const selector of [chapterSelector, 'textarea[id^="teach-term-"]']) {
      const text = page.locator(selector).first();
      await text.evaluate(element => {
        for (let parent = element.parentElement; parent; parent = parent.parentElement) {
          if (parent.tagName === 'DETAILS') parent.open = true;
        }
      });
      await text.click();
      await page.keyboard.press('Control+A');
      await page.keyboard.press('Control+C');
      await page.evaluate(() => {
        document.querySelector('#paste-target')?.remove();
        const target = document.createElement('textarea');
        target.id = 'paste-target';
        document.body.append(target);
      });
      await page.locator('#paste-target').focus();
      await page.keyboard.press('Control+V');
      const copied = await page.locator('#paste-target').inputValue();
      if (copied !== await text.inputValue()) throw new Error('Real keyboard copy/paste mismatch');
      prompts.push({ id: await text.getAttribute('id'), prompt: copied });
    }
    fs.writeFileSync(destination, JSON.stringify(prompts, null, 2));
    console.log(JSON.stringify({ actualKeyboardCopyPaste: true, prompts: prompts.length }));
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
