import re


def clean_text(text: str) -> str:
    text = text.replace("\x00", "")

    cleaned_lines = []

    for line in text.splitlines():
        line = line.strip()

        if not line:
            cleaned_lines.append("")
            continue

        single_char_spaces = re.findall(
            r"(?<!\S)\S\s(?=\S(?:\s|$))",
            line,
        )

        if len(single_char_spaces) >= 3:
            line = re.sub(r"(?<=\S) (?=\S)", "", line)

        line = re.sub(r"[ \t]+", " ", line)

        cleaned_lines.append(line)

    text = "\n".join(cleaned_lines)

    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()