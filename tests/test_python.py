"""Behavior checks for Week 13; no shared imports named 'main'."""

import importlib.util
import os
from pathlib import Path
import re
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]


def run_script(exercise, cwd, *arguments, values=None):
    """Run a fresh interpreter with only controlled environment values."""
    env = {"PATH": os.defpath, "PYTHONIOENCODING": "utf-8"}
    env.update(values or {})
    result = subprocess.run(
        [sys.executable, str(ROOT / exercise / "main.py"), *map(str, arguments)],
        cwd=cwd,
        env=env,
        capture_output=True,
        text=True,
        timeout=5,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    return result


def load_helper(exercise):
    """Give each directly tested module its own name without altering sys.path."""
    spec = importlib.util.spec_from_file_location(
        f"week13_{exercise}", ROOT / exercise / "main.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    "threshold, expected", [(None, 1), ("0.3", 2), ("0.9", 0), ("0.48", 2), ("0.83", 1)]
)
def test_EnvironmentVariables(tmp_path, threshold, expected):
    values = {} if threshold is None else {"MIN_SIGNAL": threshold}
    result = run_script("EnvironmentVariables", tmp_path, values=values)
    assert result.stdout.strip() == str(expected)


@pytest.mark.parametrize("label", ["Signal screening", "Calibration report"])
@pytest.mark.parametrize("key", [None, "", "fake-key-for-classroom-only"])
def test_ConfigurationSecrets(tmp_path, label, key):
    values = {"REPORT_LABEL": label}
    if key is not None:
        values["DATA_API_KEY"] = key
    result = run_script("ConfigurationSecrets", tmp_path, values=values)
    assert result.stdout.splitlines() == [
        f"Report label: {label}",
        f"API key configured: {bool(key)}",
    ]
    assert "fake-key-for-classroom-only" not in result.stdout + result.stderr


def test_Subprocess(tmp_path):
    module = load_helper("Subprocess")
    # Spaces in the filename catch unquoted shell command construction.
    sample = tmp_path / "measurement notes.txt"
    text = "Signal measurements:\n  0.12\t0.48  0.83\n\n"
    sample.write_text(text, encoding="utf-8")
    assert module.run_subprocess(str(sample)) == text
    sample.write_text("", encoding="utf-8")
    assert module.run_subprocess(str(sample)) == ""
    with pytest.raises(subprocess.CalledProcessError):
        module.run_subprocess(str(tmp_path / "missing.txt"))


@pytest.mark.parametrize(
    "text, expected",
    [("This is a test string with eight words", 8), (" \t\n", 0),
     ("one\ttwo\nthree  four\r\nfive", 5), ("matter, matter.", 2)],
)
def test_CommandLineScript_helper(text, expected):
    module = load_helper("CommandLineScript")
    assert module.num_words(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [("This is a test file.\nIt has multiple lines.\n", 9), ("", 0),
     ("one\ttwo\nthree", 3)],
)
def test_CommandLineScript_script(tmp_path, text, expected):
    sample = tmp_path / "word sample.txt"
    sample.write_text(text, encoding="utf-8")
    result = run_script("CommandLineScript", tmp_path, sample.name)
    assert result.stdout.strip() == f"The file has {expected} words."


@pytest.mark.parametrize("ignore_case, expected", [(False, 5), (True, 6)])
def test_ArgparseScript_bundled(tmp_path, ignore_case, expected):
    sample = tmp_path / "file1.txt"
    sample.write_bytes((ROOT / "ArgparseScript/file1.txt").read_bytes())
    flags = ["--ignore-case"] if ignore_case else []
    result = run_script("ArgparseScript", tmp_path, sample.name, "matter", *flags)
    assert result.stdout.strip() == f"The word matter occurred {expected} times in file1.txt"


@pytest.mark.parametrize("ignore_case, expected", [(False, 3), (True, 5)])
def test_ArgparseScript_substrings(tmp_path, ignore_case, expected):
    sample = tmp_path / "search sample.txt"
    sample.write_text("law laws claw Law LAW\n", encoding="utf-8")
    flags = ["--ignore-case"] if ignore_case else []
    result = run_script("ArgparseScript", tmp_path, sample.name, "law", *flags)
    assert result.stdout.strip() == (
        f"The word law occurred {expected} times in {sample.name}"
    )


def test_ArgparseScript_help(tmp_path):
    help_text = run_script("ArgparseScript", tmp_path, "--help").stdout
    assert "--ignore-case" in help_text
    # Require descriptions, not just positional names repeated in usage.
    positional = re.search(
        r"positional arguments:\n(.*?)(?:\n\S|\Z)", help_text, re.DOTALL
    )
    assert positional, "--help should list and describe the positional arguments"
    described = re.findall(r"^\s+\S+[^\S\n]{2,}\S.+$", positional.group(1), re.MULTILINE)
    assert len(described) >= 2, "Describe both filename and search string in --help"
    assert re.search(r"^\s+--ignore-case\s{2,}\S", help_text, re.MULTILINE), (
        "Add a help description for --ignore-case"
    )
