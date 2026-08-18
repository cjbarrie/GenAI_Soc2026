import { chromium } from "/Users/christopherbarrie/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs";
import path from "node:path";
import { pathToFileURL } from "node:url";

const [htmlPath, imagePath] = process.argv.slice(2);
if (!htmlPath || !imagePath) {
  throw new Error("Usage: node capture_page.mjs PAGE.html OUTPUT.png");
}

const browser = await chromium.launch({
  headless: true,
  executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
});
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await page.goto(pathToFileURL(path.resolve(htmlPath)).href, { waitUntil: "networkidle" });
await page.screenshot({ path: path.resolve(imagePath), fullPage: true });
console.log(JSON.stringify({ title: await page.title(), height: await page.evaluate(() => document.body.scrollHeight) }));
await browser.close();
