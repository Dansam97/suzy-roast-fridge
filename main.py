import os

TEXT = "My fridge's crisper drawer is a hospice for vegetables I bought with good intentions and abandoned by Tuesday."


def render():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, not whitespace-only.
    if not (1 <= len(TEXT) <= 200):
        raise ValueError("entry text outside 1-200 character gate")
    if not TEXT.strip():
        raise ValueError("entry text is whitespace-only")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry text must be a single line")
    TEXT.encode("utf-8")
    return TEXT


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(render() + "\n")


if __name__ == "__main__":
    main()
