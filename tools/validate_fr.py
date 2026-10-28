#!/usr/bin/env python3
"""Validate changed French Java .properties files without dependencies."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import os
import re
import subprocess
import sys

PARAM = re.compile(r"(?<!\{)\{\d+(?:,[^{}]*)?\}(?!\})")
HEX = set("0123456789abcdefABCDEF")


def validate_escapes(s: str, context: str, errors: list[str]) -> None:
    for m in re.finditer(r"\\u", s):
        digits = s[m.end():m.end() + 4]
        if len(digits) != 4 or any(c not in HEX for c in digits):
            errors.append(f"{context}: invalid Unicode escape at position {m.start()}")


def logical_lines(content: str):
    pending = ""
    first_line = 1
    continuing = False
    for lineno, line in enumerate(content.splitlines(), 1):
        if not continuing:
            first_line = lineno
            pending = line
        else:
            pending += line.lstrip(" \t\f")
        nslashes = len(pending) - len(pending.rstrip("\\"))
        continuing = nslashes % 2 == 1
        if continuing:
            pending = pending[:-1]
        else:
            yield first_line, pending
    if continuing:
        yield first_line, pending + "\\"  # Flagged below as unfinished continuation.


def parse(content: str, file_name: str, errors: list[str]) -> dict[str, str]:
    result = {}
    for lineno, raw in logical_lines(content):
        s = raw.lstrip(" \t\f")
        if not s or s[0] in "#!":
            continue
        # The bundles use the conventional key = value syntax.
        match = re.match(r"([^\s=:]+)\s*[=:]\s*(.*)$", s)
        if not match:
            errors.append(f"{file_name}:{lineno}: expected key = value")
            continue
        key, value = match.groups()
        ctx = f"{file_name}:{lineno} ({key})"
        validate_escapes(key, ctx, errors)
        validate_escapes(value, ctx, errors)
        if key in result:
            errors.append(f"{ctx}: duplicate key")
        result[key] = value
    return result


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True, stderr=subprocess.PIPE)


def main() -> int:
    base = os.getenv("BASE_SHA", "").strip()
    if not base:
        try:
            base = git("merge-base", "HEAD", "origin/main").strip()
        except subprocess.CalledProcessError:
            print("BASE_SHA is unset; run on a PR or provide BASE_SHA.", file=sys.stderr)
            return 2
    try:
        paths = git("diff", "--name-only", "--diff-filter=ACMR", base, "HEAD").splitlines()
    except subprocess.CalledProcessError as exc:
        print(f"Cannot compare commits: {exc}", file=sys.stderr)
        return 2
    french = [p for p in paths if Path(p).name.endswith("_fr.properties")]
    if not french:
        print("No changed French .properties bundles; check passed.")
        return 0
    errors: list[str] = []
    for p in french:
        path = Path(p)
        if not path.is_file():
            errors.append(f"{p}: file not found")
            continue
        try:
            current = parse(path.read_text(encoding="iso-8859-1"), p, errors)
        except OSError as exc:
            errors.append(f"{p}: {exc}")
            continue
        try:
            original = git("show", f"{base}:{p}")
        except subprocess.CalledProcessError:
            original = ""  # Newly created file.
        # Existing historical errors do not block newly improved translations.
        old = parse(original, f"{p} (base)", [])
        for key in sorted(old.keys() - current.keys()):
            errors.append(f"{p}: removed existing key: {key}")
        for key in sorted(old.keys() & current.keys()):
            if old[key] == current[key]:
                continue
            before = Counter(PARAM.findall(old[key]))
            after = Counter(PARAM.findall(current[key]))
            if before != after:
                errors.append(f"{p}: placeholders changed in {key}: {dict(before)} -> {dict(after)}")
        print(f"Checked {p}: {len(current)} entries")
    if errors:
        print("\nValidation failed:", file=sys.stderr)
        for error in errors:
            print(f" - {error}", file=sys.stderr)
        return 1
    print("French translation checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
