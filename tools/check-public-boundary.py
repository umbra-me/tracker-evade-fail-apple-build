from pathlib import Path
import subprocess
root = Path(__file__).resolve().parents[1]
paths = [str(path.relative_to(root)) for path in root.rglob("*") if path.is_file() and ".git" not in path.relative_to(root).parts]
for path in paths:
    assert path.startswith(".github/") or path in {".gitignore", "README.md", "AGENTS.md", "CLAUDE.md", "MIGRATION-STAGED.md", "umbra.dev.yaml", "tools/check-public-boundary.py"}, f"unexpected public source: {path}"
    assert Path(path).suffix.lower() not in {".swift", ".ipa", ".p12", ".mobileprovision", ".key", ".env"}, f"private artifact: {path}"
print("public orchestration boundary passed")
