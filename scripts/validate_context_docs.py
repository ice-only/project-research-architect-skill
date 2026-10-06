from pathlib import Path
import sys


REQUIRED_HEADINGS = {
    "AGENTS.md": ["Selective reading", "Selective writing"],
    "PROJECT_INDEX.md": ["项目"],
    "README.md": [],
    "NOW.md": [],
    "MAP.md": [],
    "RUNBOOK.md": [],
    "DECISIONS.md": [],
    "RISKS.md": [],
}


def validate(root: Path) -> list[str]:
    errors = []
    for name, headings in REQUIRED_HEADINGS.items():
        path = root / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                errors.append(f"{path}: missing required text {heading!r}")
    history = root / "history" / "README.md"
    if history.exists() and not history.read_text(encoding="utf-8").strip():
        errors.append(f"{history}: file is empty")
    return errors


if __name__ == "__main__":
    errors = validate(Path(sys.argv[1] if len(sys.argv) > 1 else "."))
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print("context documentation checks passed")

