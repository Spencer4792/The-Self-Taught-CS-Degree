// Validate every ```mermaid block in the given markdown files.
// Usage: node tools/check_mermaid.js file1.md [file2.md ...]
// Requires: npm install --no-save mermaid jsdom   (run from repo root)
const fs = require('fs');
const { JSDOM } = require('jsdom');
const dom = new JSDOM('<!DOCTYPE html><body></body>');
global.window = dom.window; global.document = dom.window.document;
global.DOMPurify = { sanitize: (x) => x, addHook: () => {} };
import('mermaid').then(async (m) => {
  const mermaid = m.default;
  mermaid.initialize({ startOnLoad: false });
  let bad = 0, total = 0;
  for (const f of process.argv.slice(2)) {
    const lines = fs.readFileSync(f, 'utf8').split('\n');
    let cur = null, start = 0;
    for (let i = 0; i < lines.length; i++) {
      const s = lines[i].trim();
      if (cur === null && s.startsWith('```mermaid')) { cur = []; start = i + 1; }
      else if (cur !== null && s.startsWith('```')) {
        total++;
        try { await mermaid.parse(cur.join('\n')); console.log(`OK   ${f}:${start}`); }
        catch (e) { bad++; console.log(`FAIL ${f}:${start} :: ${e.message.split('\n')[0]}`); }
        cur = null;
      } else if (cur !== null) cur.push(lines[i]);
    }
  }
  console.log(`${total} blocks, ${bad} failed`);
  process.exit(bad ? 1 : 0);
});
