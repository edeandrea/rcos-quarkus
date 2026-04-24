import os
import shutil
import yaml
import re
from pathlib import Path

MKDOCS_DIR = "docs/docs"
OUTPUT_DIR = "roq-site"
CONTENT_DIR = os.path.join(OUTPUT_DIR, "content")
PUBLIC_DIR = os.path.join(OUTPUT_DIR, "public")

def load_mkdocs_nav(mkdocs_file="mkdocs.yml"):
    if not os.path.exists(mkdocs_file):
        return []
    with open(mkdocs_file, "r") as f:
        config = yaml.safe_load(f)
    return config.get("nav", [])

def ensure_dirs():
    os.makedirs(CONTENT_DIR, exist_ok=True)
    os.makedirs(PUBLIC_DIR, exist_ok=True)

def convert_frontmatter(title):
    return f"""---
title: {title}
layout: default
---

"""

def extract_title(md_text, fallback):
    match = re.search(r"^# (.+)", md_text, re.MULTILINE)
    return match.group(1).strip() if match else fallback

def rewrite_links(content):
    content = re.sub(r"\]\((.*?)\.md\)", r"](\1/)", content)
    return content

def process_markdown_file(src_path, dest_path):
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    title = extract_title(content, Path(src_path).stem)
    content = rewrite_links(content)

    final = convert_frontmatter(title) + content

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final)

def copy_assets():
    for root, _, files in os.walk(MKDOCS_DIR):
        for file in files:
            if not file.endswith(".md"):
                src = os.path.join(root, file)
                rel = os.path.relpath(src, MKDOCS_DIR)
                dest = os.path.join(PUBLIC_DIR, rel)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copy2(src, dest)

def convert_all():
    for root, _, files in os.walk(MKDOCS_DIR):
        for file in files:
            if file.endswith(".md"):
                src = os.path.join(root, file)
                rel = os.path.relpath(src, MKDOCS_DIR)

                if file == "index.md":
                    dest = os.path.join(CONTENT_DIR, rel)
                else:
                    name = Path(file).stem
                    dest = os.path.join(CONTENT_DIR, os.path.dirname(rel), name, "index.md")

                process_markdown_file(src, dest)

if __name__ == "__main__":
    ensure_dirs()
    convert_all()
    copy_assets()
    print("Converted!")