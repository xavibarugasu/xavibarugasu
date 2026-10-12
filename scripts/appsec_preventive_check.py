#!/usr/bin/env python3
"""AppSec lightweight checks. Copyright 2026 Javier Enrique Vargas Carrasco."""
import json
import os
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "node_modules", ".venv", "venv", "dist", "build", "__pycache__", ".next", "coverage"}
EXTENSIONS = {".py", ".php", ".js", ".jsx", ".ts", ".tsx", ".html", ".yml", ".yaml", ".json", ".env", ".ini", ".properties"}
MAX_BYTES = 1024 * 1024
# Heuristic indicators, not proof of compromise. Avoid displaying matched secrets.
RULES = [
    ("HIGH", "Private key header", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("HIGH", "GitHub token pattern", re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}")),
    ("HIGH", "AWS access key identifier", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("MEDIUM", "Possible hardcoded password", re.compile(r"""(?i)\b(?:password|passwd|db_password)\s*[:=]\s*['\"][^'\"]{8,}['\"]""")),
]
findings = []
scanned = 0
for base, dirs, names in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in SKIP and not d.startswith(".git")]
    for name in names:
        path = Path(base) / name
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(".github/") or rel.startswith(".claude/"):
            continue
        if path.suffix.lower() not in EXTENSIONS and name != ".env":
            continue
        if path.is_symlink() or path.stat().st_size > MAX_BYTES:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            continue
        scanned += 1
        for n, line in enumerate(content.splitlines(), 1):
            for severity, title, pattern in RULES:
                if pattern.search(line):
                    findings.append({"severity": severity, "rule": title, "file": rel, "line": n})
summary = [
    "# AppSec preventive scan",
    "",
    "Owner: Javier Enrique Vargas Carrasco · AppSec Security Auditor v1.1",
    "",
    f"Code/config files scanned: {scanned}",
    f"Potential findings: {len(findings)}",
    "",
    "**Scope:** heuristic secret indicators only; not a complete audit of the 20 controls or a Claude skill invocation.",
    "",
]
if findings:
    summary.extend(["| Severity | Indicator | File | Line |", "|---|---|---|---|"])
    summary.extend(f"| {f['severity']} | {f['rule']} | `{f['file']}` | {f['line']} |" for f in findings)
else:
    summary.append("No indicators found by the enabled patterns. This does not prove the repository is secure.")
report = "\n".join(summary) + "\n"
print(report)
with open(os.environ.get("GITHUB_STEP_SUMMARY", "/dev/null"), "a", encoding="utf-8") as out:
    out.write(report)
if findings:
    for f in findings:
        print(f"::warning file={f['file']},line={f['line']}::{f['rule']} ({f['severity']}); matched value suppressed")
sys.exit(1 if findings else 0)
