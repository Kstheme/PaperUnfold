"""Render an agent-authored guide as offline HTML, checking literal source references."""
import argparse
import html
import json
from pathlib import Path
import re
import sys


LABELS_EN = dict(coverage="Coverage", missing="Not covered", thread="Research thread", contents="Contents",
                 terms="Terms", evidence="Source passages", source="Supplied text", role="Role / explanatory inference",
                 essential="Essential", optional="Optional", author="Author statement", background="Background",
                 inference="Inference", analogy="Analogy")
LABELS_ZH = dict(coverage="阅读覆盖范围", missing="未覆盖材料", thread="研究主线", contents="目录",
                 terms="术语", evidence="原文证据位置", source="提供的原文", role="章节作用 / 讲解者推断",
                 essential="必需术语", optional="按需术语", author="原文陈述", background="补充背景",
                 inference="推断", analogy="类比")
KINDS = {"author", "background", "inference", "analogy"}
IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9_-]*\Z")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def string(value, field):
    require(isinstance(value, str) and bool(value.strip()), f"{field} must be nonempty text")
    return value


def listing(value, field, nonempty=False):
    require(isinstance(value, list) and (bool(value) or not nonempty), f"{field} must be a {'nonempty ' if nonempty else ''}list")
    return value


def validate(data):
    require(isinstance(data, dict), "guide must be an object")
    string(data.get("title"), "title")
    language = string(data.get("language"), "language")
    require(re.fullmatch(r"[A-Za-z]{2,8}(?:-[A-Za-z0-9]{1,8})*", language) is not None, "language must be a language tag")
    source = data.get("source")
    require(isinstance(source, dict), "source must be an object")
    for key in ("name", "text", "coverage"):
        string(source.get(key), f"source.{key}")
    for value in listing(source.get("missing"), "source.missing"):
        string(value, "missing material")
    evidence_ids = set()
    for item in listing(data.get("evidence"), "evidence", True):
        require(isinstance(item, dict), "evidence entry must be an object")
        ident = string(item.get("id"), "evidence.id")
        require(IDENTIFIER.fullmatch(ident) is not None and ident not in evidence_ids, "evidence IDs must be unique identifiers")
        evidence_ids.add(ident)
        string(item.get("location"), "evidence.location")
        quote = string(item.get("quote"), "evidence.quote")
        require(quote in source["text"], f"evidence quote {ident} is absent from source.text")

    def point(item):
        require(isinstance(item, dict), "explanation must be an object")
        string(item.get("text"), "explanation.text")
        require(item.get("kind") in KINDS, "explanation.kind must be author, background, inference, or analogy")
        references = listing(item.get("evidence"), "explanation.evidence", item["kind"] in {"author", "inference"})
        for reference in references:
            require(isinstance(reference, str) and reference in evidence_ids, "explanation evidence references must name a supplied excerpt")

    for item in listing(data.get("thread"), "thread", True):
        point(item)
    section_ids = set()
    for section in listing(data.get("sections"), "sections", True):
        require(isinstance(section, dict), "section must be an object")
        ident = string(section.get("id"), "section.id")
        require(IDENTIFIER.fullmatch(ident) is not None and ident not in section_ids, "section IDs must be unique identifiers")
        section_ids.add(ident)
        for key in ("title", "role"):
            string(section.get(key), f"section.{key}")
        for item in listing(section.get("points"), "section.points", True):
            point(item)
    for term in listing(data.get("terms"), "terms"):
        require(isinstance(term, dict), "term must be an object")
        for key in ("original", "name"):
            string(term.get(key), f"term.{key}")
        require(isinstance(term.get("essential"), bool), "term.essential must be a boolean")
        point(term.get("explanation"))
    labels = data.get("labels")
    primary_language = language.split("-")[0].lower()
    if labels is not None:
        require(isinstance(labels, dict), "labels must be an object")
        for key in LABELS_EN:
            string(labels.get(key), f"labels.{key}")
    else:
        require(primary_language in {"en", "zh"}, "provide translated labels for this language")
    return labels if labels is not None else (LABELS_ZH if primary_language == "zh" else LABELS_EN)


CSS = """
:root{color-scheme:light;--ink:#182b32;--muted:#53676e;--accent:#14695d;--paper:#faf9f5}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.75 system-ui,sans-serif}
main{max-width:1000px;margin:auto;padding:48px 24px 80px}h1{font-size:clamp(30px,5vw,48px);line-height:1.15;letter-spacing:-.03em}h2{font-size:26px;margin-top:42px}h3{font-size:20px}
section{scroll-margin-top:20px}a{color:var(--accent);text-underline-offset:3px}nav{border-block:1px solid #d5ded9;padding:18px 0}nav ul{display:flex;gap:12px 24px;flex-wrap:wrap;list-style:none;padding:0;margin:0}
.coverage{border-left:4px solid var(--accent);padding:12px 20px;background:#eaf1ec}.coverage p{margin:6px 0}.muted{color:var(--muted)}
.point{margin:18px 0}.point p{margin:5px 0}.kind{font-size:12px;letter-spacing:.03em;color:var(--muted);border:1px solid #cdd8d2;border-radius:4px;padding:2px 6px}.refs{font-size:13px;display:flex;gap:12px;flex-wrap:wrap}
details{border:1px solid #d5ded9;border-radius:8px;padding:15px 20px;margin:14px 0;background:white}summary{cursor:pointer;font-weight:650}summary:focus-visible,a:focus-visible{outline:3px solid #db9234;outline-offset:4px}
blockquote{margin:8px 0;padding:10px 18px;border-left:3px solid #b2c7bc;white-space:pre-wrap}pre{font:14px/1.7 ui-monospace,monospace;white-space:pre-wrap;overflow-wrap:anywhere}.term-original{font-weight:400;color:var(--muted)}
@media print{body{background:white}main{padding:0}details{break-inside:avoid}details>summary{list-style:none}details>*{display:block!important}nav{display:none}}
"""


def render(data, labels):
    esc = html.escape

    def point(item):
        refs = "".join(f'<a href="#evidence-{esc(ref)}">{esc(evidence_locations[ref])}</a>' for ref in item["evidence"])
        return f'<div class="point"><span class="kind">{esc(labels[item["kind"]])}</span><p>{esc(item["text"])}</p><div class="refs">{refs}</div></div>'

    evidence_locations = {item["id"]: item["location"] for item in data["evidence"]}
    navigation = [("thread", labels["thread"])] + [("section-" + s["id"], s["title"]) for s in data["sections"]]
    if data["terms"]:
        navigation.append(("terms", labels["terms"]))
    navigation.append(("evidence", labels["evidence"]))
    nav = "".join(f'<li><a href="#{esc(ident)}">{esc(title)}</a></li>' for ident, title in navigation)
    missing = "".join(f'<li>{esc(value)}</li>' for value in data["source"]["missing"])
    coverage = f'<aside class="coverage"><strong>{esc(labels["coverage"])}</strong><p>{esc(data["source"]["name"])}</p><p>{esc(data["source"]["coverage"])}</p>'
    if missing:
        coverage += f'<strong>{esc(labels["missing"])}</strong><ul>{missing}</ul>'
    coverage += '</aside>'
    thread = f'<section id="thread"><h2>{esc(labels["thread"])}</h2>' + "".join(point(item) for item in data["thread"]) + '</section>'
    sections = ""
    for section in data["sections"]:
        sections += f'<section id="section-{esc(section["id"])}"><h2>{esc(section["title"])}</h2><p><span class="kind">{esc(labels["role"])}</span> {esc(section["role"])}</p><details open><summary>{esc(section["title"])}</summary>'
        sections += "".join(point(item) for item in section["points"]) + '</details></section>'
    terms = ""
    if data["terms"]:
        terms = f'<section id="terms"><h2>{esc(labels["terms"])}</h2>'
        for term in data["terms"]:
            original = f' <span class="term-original">({esc(term["original"])})</span>' if term["original"] != term["name"] else ""
            category = labels["essential" if term["essential"] else "optional"]
            terms += f'<details{" open" if term["essential"] else ""}><summary>{esc(term["name"])}{original} · {esc(category)}</summary>{point(term["explanation"])}</details>'
        terms += '</section>'
    evidence = f'<section id="evidence"><h2>{esc(labels["evidence"])}</h2>'
    for item in data["evidence"]:
        evidence += f'<article id="evidence-{esc(item["id"])}"><h3>{esc(item["location"])}</h3><blockquote>{esc(item["quote"])}</blockquote></article>'
    evidence += f'<details><summary>{esc(labels["source"])}</summary><pre>{esc(data["source"]["text"])}</pre></details></section>'
    return f'<!doctype html><html lang="{esc(data["language"])}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(data["title"])}</title><style>{CSS}</style></head><body><main><header><p class="muted">PaperUnfold</p><h1>{esc(data["title"])}</h1>{coverage}</header><nav aria-label="{esc(labels["contents"])}"><ul>{nav}</ul></nav>{thread}{sections}{terms}{evidence}</main></body></html>'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 JSON guide")
    parser.add_argument("--output", required=True, type=Path, help="Single-file HTML destination")
    args = parser.parse_args()
    try:
        require(args.input.resolve() != args.output.resolve(), "output must differ from input")
        data = json.loads(args.input.read_text(encoding="utf-8-sig"))
        labels = validate(data)
        content = render(data, labels)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
    except (OSError, ValueError, TypeError) as error:
        print(f"Cannot render guide: {error}", file=sys.stderr)
        return 1
    print(f"Saved {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
