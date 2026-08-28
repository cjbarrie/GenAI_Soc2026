import { chromium } from "/Users/christopherbarrie/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs";
import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";

const [reportPath, ...htmlPaths] = process.argv.slice(2);
if (!reportPath || htmlPaths.length === 0) {
  throw new Error("Usage: node check_web_pages.mjs REPORT.json PAGE.html [PAGE.html ...]");
}

const browser = await chromium.launch({
  headless: true,
  executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
});
const viewports = {
  desktop: { width: 1440, height: 900 },
  mobile: { width: 390, height: 844 },
};
const report = [];

for (const htmlPath of htmlPaths) {
  for (const [mode, viewport] of Object.entries(viewports)) {
    const page = await browser.newPage({ viewport });
    await page.goto(pathToFileURL(path.resolve(htmlPath)).href, { waitUntil: "networkidle" });
    await page.evaluate(() => document.fonts?.ready);
    const result = await page.evaluate(() => ({
      title: document.title,
      textLength: document.body.innerText.trim().length,
      documentOverflow: document.documentElement.scrollWidth > window.innerWidth + 2,
      brokenImages: [...document.images]
        .filter((image) => !image.complete || image.naturalWidth === 0)
        .map((image) => image.src),
    }));
    report.push({ file: htmlPath, mode, viewport, ...result });
    await page.close();
  }
}

fs.mkdirSync(path.dirname(path.resolve(reportPath)), { recursive: true });
fs.writeFileSync(path.resolve(reportPath), JSON.stringify(report, null, 2));
const failures = report.filter(
  (item) => item.documentOverflow || item.brokenImages.length || item.textLength < 100,
);
console.log(JSON.stringify({ pages: htmlPaths.length, checks: report.length, failures }));
await browser.close();
if (failures.length) process.exit(1);
