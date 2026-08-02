from __future__ import annotations
from pathlib import Path

SOURCE_DIR = Path(__file__).resolve().parent / ".."
OUTPUT_FILE = Path(__file__).resolve().parent / "tekila.txt"
EXTENSIONS = {".css", ".html", ".js"}

ANSWER_FORMAT = """

"""

USER_PROMPT = ANSWER_FORMAT


def collect_files(source_dir: Path, extensions: set[str]) -> list[Path]:
    if not source_dir.exists():
        raise FileNotFoundError(f"Cannot found: {source_dir}")
    all_files = []
    for ext in extensions:
        all_files.extend(source_dir.rglob(f"*{ext}"))
    return sorted(set(all_files))

def write_combined_file(file_paths: list[Path], output_path: Path, prompt: str) -> None:
    with open(output_path, "w", encoding="utf-8") as out_f:
        for file_path in file_paths:
            rel_path = file_path.relative_to(SOURCE_DIR)
            out_f.write(f"{rel_path}:\n")
            content = file_path.read_text(encoding="utf-8", errors="ignore")
            out_f.write(content)
            out_f.write("\n\n")
        out_f.write(prompt + "\n")

def main() -> None:
    print(f"Searching files with {EXTENSIONS} extensions in {SOURCE_DIR}...")
    files = collect_files(SOURCE_DIR, EXTENSIONS)

    if not files:
        print("No files")
        return

    print(f"File count {len(files)}")
    write_combined_file(files, OUTPUT_FILE, USER_PROMPT)
    print(f"Final file: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()