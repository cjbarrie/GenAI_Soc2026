import { chromium } from "playwright";
import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";

const [htmlPath, outputDir, pdfPath] = process.argv.slice(2);
if (!htmlPath || !outputDir) {
  throw new Error("Usage: node capture_reveal.mjs DECK.html OUTPUT_DIR");
}

fs.mkdirSync(outputDir, { recursive: true });
const browser = await chromium.launch({
  headless: true,
  executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
});
const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
await page.goto(pathToFileURL(path.resolve(htmlPath)).href, { waitUntil: "networkidle" });
await page.waitForFunction(() => window.Reveal?.isReady());

const slideCount = await page.evaluate(() => window.Reveal.getHorizontalSlides().length);
const report = [];
for (let index = 0; index < slideCount; index += 1) {
  await page.evaluate((i) => window.Reveal.slide(i, 0, 0), index);
  await page.waitForTimeout(700);
  const geometry = await page.evaluate(() => {
    const slide = window.Reveal.getCurrentSlide();
    const slideBox = slide.getBoundingClientRect();
    const content = [...slide.querySelectorAll("h1,h2,h3,p,li,pre,table,blockquote,.metric,.course-map")];
    const offenders = content
      .filter((element) => {
        const box = element.getBoundingClientRect();
        return (
          box.left < slideBox.left - 2 ||
          box.top < slideBox.top - 2 ||
          box.right > slideBox.right + 2 ||
          box.bottom > slideBox.bottom + 2 ||
          (["PRE", "TABLE"].includes(element.tagName) &&
            (element.scrollWidth > element.clientWidth + 2 ||
              element.scrollHeight > element.clientHeight + 2))
        );
      })
      .map((element) => element.tagName + ":" + element.textContent.trim().slice(0, 50));
    for (const line of slide.querySelectorAll("pre code > span[id]")) {
      const lineBox = line.getBoundingClientRect();
      const preBox = line.closest("pre").getBoundingClientRect();
      const lineHeight = Number.parseFloat(window.getComputedStyle(line).lineHeight);
      const wraps = Number.isFinite(lineHeight) && lineBox.height > lineHeight * 1.5;
      // Quarto's line-number gutter deliberately begins inside the pre element's
      // left padding, so a left-edge comparison produces false positives. A real
      // long-line problem either wraps to a second visual line or crosses the
      // right edge of the code block.
      if (wraps || lineBox.right > preBox.right + 2) {
        offenders.push("CODE-LINE:" + line.textContent.trim().slice(0, 50));
      }
    }
    return {
      title: slide.querySelector("h1,h2")?.textContent?.trim() ?? "",
      offenders,
    };
  });
  const filename = `slide-${String(index + 1).padStart(2, "0")}.png`;
  await page.screenshot({ path: path.join(outputDir, filename) });
  report.push({ slide: index + 1, ...geometry });
}

fs.writeFileSync(path.join(outputDir, "qa-report.json"), JSON.stringify(report, null, 2));
if (pdfPath) {
  await page.goto(`${pathToFileURL(path.resolve(htmlPath)).href}?print-pdf`, { waitUntil: "networkidle" });
  await page.waitForFunction(() => window.Reveal?.isReady());
  await page.emulateMedia({ media: "print" });
  await page.pdf({
    path: path.resolve(pdfPath),
    width: "13.333333in",
    height: "7.5in",
    printBackground: true,
    preferCSSPageSize: true,
  });
}
console.log(JSON.stringify({ slideCount, overflowSlides: report.filter((item) => item.offenders.length) }));
await browser.close();
