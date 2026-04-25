import yaml
import os
from pathlib import Path

MKDOCS_FILE = "mkdocs.yml"
OUTPUT_FILE = "roq-site/data/menu.yaml"


def md_to_url(path):
    if path == "index.md":
        return "/"
    path = path.replace(".md", "")
    if path.endswith("/index"):
        path = path[:-6]
    return f"/{path}/"


def process_nav_item(item):
    if isinstance(item, dict):
        result = []
        for title, value in item.items():
            if isinstance(value, str):
                result.append({
                    "title": title,
                    "url": md_to_url(value)
                })
            elif isinstance(value, list):
                result.append({
                    "title": title,
                    "children": process_nav_list(value)
                })
        return result
    return []


def process_nav_list(nav_list):
    output = []
    for item in nav_list:
        if isinstance(item, dict):
            for title, value in item.items():
                if isinstance(value, str):
                    output.append({
                        "title": title,
                        "url": md_to_url(value)
                    })
                elif isinstance(value, list):
                    output.append({
                        "title": title,
                        "children": process_nav_list(value)
                    })
    return output


def convert():
    with open(MKDOCS_FILE, "r") as f:
        config = yaml.safe_load(f)

    nav = config.get("nav", [])
    menu = process_nav_list(nav)

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w") as f:
        yaml.dump({"menu": menu}, f, sort_keys=False)


if __name__ == "__main__":
    convert()