// Capture each horizontal Reveal slide at presentation size for visual review.
import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

const [input, outputDirectory] = process.argv.slice(2);
if (!input || !outputDirectory) {
  throw new Error("Usage: node capture_reveal_slides.mjs DECK.html OUTPUT_DIRECTORY");
}

fs.mkdirSync(outputDirectory, { recursive: true });
const browser = await chromium.launch({
  headless: true,
  executablePath: process.env.CHROME_PATH || undefined,
});
const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
await page.goto(pathToFileURL(path.resolve(input)).href, { waitUntil: "networkidle" });
await page.waitForFunction(() => window.Reveal && window.Reveal.isReady());
const count = await page.evaluate(() => window.Reveal.getHorizontalSlides().length);

for (let index = 0; index < count; index += 1) {
  await page.evaluate((slideIndex) => window.Reveal.slide(slideIndex), index);
  await page.waitForTimeout(650);
  const filename = `slide-${String(index + 1).padStart(2, "0")}.png`;
  await page.screenshot({ path: path.join(outputDirectory, filename) });
}

await browser.close();
process.stdout.write(`${count} slides captured in ${outputDirectory}\n`);
