from pathlib import Path

for path in Path("docs").glob("*.md"):
    try:
        text = path.read_text(encoding="utf-8")
        print(f"OK UTF-8: {path}")
    except UnicodeDecodeError:
        text = path.read_text(encoding="cp1252")
        path.write_text(text, encoding="utf-8")
        print(f"Converted to UTF-8: {path}")