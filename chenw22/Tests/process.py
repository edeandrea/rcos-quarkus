import os
MKDOCS_DIR = "docs/docs"
OUTPUT_DIR = "roq-site"
CONTENT_DIR = os.path.join(OUTPUT_DIR, "content")
PUBLIC_DIR = os.path.join(OUTPUT_DIR, "public")

def ensure_dirs():
    os.makedirs(CONTENT_DIR, exist_ok=True)
    os.makedirs(PUBLIC_DIR, exist_ok=True)


if __name__ == "__main__":
    ensure_dirs()
    print("check")