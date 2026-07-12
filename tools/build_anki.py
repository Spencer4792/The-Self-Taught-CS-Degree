#!/usr/bin/env python3
"""Build the CS Mastery Anki deck from study/cards/answers-*.json + the glossary.

Usage: python3 tools/build_anki.py          (requires: pip install genanki)

Outputs:
  study/cs-mastery.apkg        import this into Anki
  study/teach-it-back.tsv      plain TSV fallback (Front<TAB>Back<TAB>Tags)

Deck layout: "CS Mastery::<part>" subdecks for Teach-it-back cards,
plus "CS Mastery::Glossary" built from 28-Appendix/28.2-glossary.md.
"""
import re, json, html, pathlib, hashlib
import genanki

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "study"

def md_to_html(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<i>\1</i>", s)
    return s.replace("\n", "<br>")

def clean_prompt(p):
    # drop chapter-transition boilerplate captured by extraction
    p = re.split(r"\s*---\s", p)[0]
    p = re.sub(r"\s*\*?(Next up|Next:|That closes|You(')?ve earned|On to )[^*]*\*?\s*$", "", p)
    return p.strip()

def stable_id(name):
    return int(hashlib.sha1(name.encode()).hexdigest()[:9], 16)

MODEL = genanki.Model(
    stable_id("cs-mastery-model"), "CS Mastery Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Source"}],
    templates=[{
        "name": "Card 1",
        "qfmt": "{{Front}}",
        "afmt": "{{FrontSide}}<hr id=answer>{{Back}}<br><br><small style='color:#888'>{{Source}}</small>",
    }],
    css=".card { font-family: -apple-system, sans-serif; font-size: 17px; text-align: left; "
        "color: #222; background: #fdfdfd; max-width: 600px; margin: auto; padding: 12px; } "
        "code { background: #eee; padding: 1px 4px; border-radius: 3px; font-size: 90%; }",
)

def part_title(chapter_path):
    d = chapter_path.split("/")[0]                     # e.g. 05-Systems
    return d.split("-", 1)[0] + " " + d.split("-", 1)[1].replace("-", " ")

def build():
    decks, tsv = {}, []
    def deck_for(name):
        if name not in decks:
            decks[name] = genanki.Deck(stable_id(name), name)
        return decks[name]

    # Teach-it-back cards
    n = 0
    for f in sorted(OUT.glob("cards/answers-*.json")):
        for card in json.loads(f.read_text(encoding="utf-8")):
            front = clean_prompt(card["prompt"])
            if len(front) < 10:
                continue
            dk = deck_for("CS Mastery::" + part_title(card["chapter"]))
            tag = card["chapter"].split("/")[-1].replace(".md", "").replace(".", "_")
            dk.add_note(genanki.Note(
                model=MODEL, guid=genanki.guid_for(card["id"]),
                fields=[md_to_html(front), md_to_html(card["answer"]), card["chapter"]],
                tags=[tag]))
            tsv.append((front, card["answer"], tag))
            n += 1

    # Glossary cards
    g = 0
    gdeck = deck_for("CS Mastery::Glossary")
    gtext = (ROOT / "28-Appendix/28.2-glossary.md").read_text(encoding="utf-8")
    for m in re.finditer(r"^\*\*(.+?)\*\*, (.+?) → see \[(.+?)\]", gtext, re.M):
        term, definition, chap = m.groups()
        gdeck.add_note(genanki.Note(
            model=MODEL, guid=genanki.guid_for("gloss-" + term),
            fields=[md_to_html(term), md_to_html(definition), chap], tags=["glossary"]))
        tsv.append((term, definition, "glossary"))
        g += 1

    genanki.Package(list(decks.values())).write_to_file(str(OUT / "cs-mastery.apkg"))
    with open(OUT / "teach-it-back.tsv", "w", encoding="utf-8") as fh:
        for front, back, tag in tsv:
            fh.write(front.replace("\t", " ") + "\t" + back.replace("\t", " ").replace("\n", " ") + "\t" + tag + "\n")
    print(f"{n} teach-it-back cards + {g} glossary cards -> study/cs-mastery.apkg ({len(decks)} subdecks)")

if __name__ == "__main__":
    build()
