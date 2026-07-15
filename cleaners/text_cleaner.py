import re
from pathlib import Path
from typing import Optional


def clean_text(
    raw: str,
    remove_control: bool = True,
    normalize_ws: bool = True,
    fix_petscii: bool = True,
    deduplicate: bool = False,
    max_line_length: int = 0,
) -> str:
    if remove_control:
        raw = re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]", "", raw)

    raw = re.sub(r"^\s*\d+\s*$", "", raw, flags=re.MULTILINE)

    if fix_petscii:
        raw = raw.replace("\xa0", " ")
        raw = raw.replace("\x00", "")

    if normalize_ws:
        raw = re.sub(r"[ \t]+", " ", raw)

    for op in ["LDA", "STA", "LDX", "STX", "LDY", "STY", "JSR", "JMP", "RTS"]:
        pattern = r"\b" + r"\s*".join(list(op)) + r"\b"
        raw = re.sub(pattern, op, raw, flags=re.IGNORECASE)

    raw = re.sub(r"\$\s+([0-9A-F]{2,4})", r"$\1", raw, flags=re.IGNORECASE)
    raw = re.sub(r"([A-Z0-9_]+)\s+:", r"\1:", raw, flags=re.IGNORECASE)

    raw = re.sub(r"\n\s*\n\s*\n+", "\n\n", raw)

    if deduplicate:
        lines = raw.split("\n")
        seen: set[str] = set()
        unique_lines: list[str] = []
        for line in lines:
            stripped = line.strip()
            if stripped and stripped not in seen:
                seen.add(stripped)
                unique_lines.append(line)
        raw = "\n".join(unique_lines)

    if max_line_length > 0:
        lines = raw.split("\n")
        raw = "\n".join(line[:max_line_length] for line in lines)

    return raw.strip()


advanced_clean = clean_text


def clean_file(input_path: str, output_path: str, **kwargs) -> None:
    text = Path(input_path).read_text(encoding="utf-8")
    cleaned = clean_text(text, **kwargs)
    Path(output_path).write_text(cleaned, encoding="utf-8")


def main():
    import sys

    if len(sys.argv) < 3:
        print("Usage: python -m cleaners.text_cleaner input.txt output.txt")
        return

    input_txt = sys.argv[1]
    output_txt = sys.argv[2]

    if not Path(input_txt).exists():
        print(f"File not found: {input_txt}")
        return

    clean_file(input_txt, output_txt)
    print(f"Cleaned text saved to: {output_txt}")


if __name__ == "__main__":
    main()
