import os
import shutil
import yaml
import re
from pathlib import Path

MKDOCS_DIR = Path("docs/docs")
OUTPUT_DIR = Path("roq-site")
CONTENT_DIR = OUTPUT_DIR / "content"
PUBLIC_DIR = OUTPUT_DIR / "public"


def load_mkdocs_nav(mkdocs_file="mkdocs.yml"):
    mkdocs_path = Path(mkdocs_file)
    if not mkdocs_path.exists():
        return []
    with mkdocs_path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config.get("nav", [])

def ensure_dirs():
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)

def convert_frontmatter(title):
    fm = {
        "title": title,
        "layout": "default"
    }
    return yaml.safe_dump(fm, sort_keys=False).rstrip() + "\n---\n\n"

def extract_title(md_text, fallback):
    match = re.search(r"^# (.+)", md_text, re.MULTILINE)
    return match.group(1).strip() if match else fallback

def slugify(name):
    return re.sub(r"[^a-zA-Z0-9_-]+", "-", name).strip("-").lower()

def rewrite_links(content):
    return re.sub(
        r"\]\(([^)]+?)\.md(#[^)]+)?\)",
        lambda m: f"]({m.group(1)}/{m.group(2) or ''})",
        content
    )

def process_markdown_file(src_path, dest_path):
    text = src_path.read_text(encoding="utf-8")

    title = extract_title(text, src_path.stem)
    text = rewrite_links(text)

    final = convert_frontmatter(title) + text

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(final, encoding="utf-8")


def copy_assets():
    for path in MKDOCS_DIR.rglob("*"):
        if path.is_file() and path.suffix != ".md":
            rel = path.relative_to(MKDOCS_DIR)
            dest = PUBLIC_DIR / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, dest)


def convert_all():
    for path in MKDOCS_DIR.rglob("*.md"):
        rel = path.relative_to(MKDOCS_DIR)

        if path.name == "index.md":
            dest = CONTENT_DIR / rel
        else:
            slug = slugify(path.stem)
            dest = CONTENT_DIR / rel.parent / slug / "index.md"

        process_markdown_file(path, dest)

if __name__ == "__main__":
    ensure_dirs()
    convert_all()
    copy_assets()
    print("Converted!")