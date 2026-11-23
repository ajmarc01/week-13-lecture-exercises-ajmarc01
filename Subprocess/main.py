"""In this exercise, you will run the cat command from Python and return
the file contents it prints.

Complete run_subprocess(filename). Run cat on the supplied file and return
its output as a string, preserving whitespace and newlines. If the file
is missing, raise subprocess.CalledProcessError.

Run the tests from the repository root:
    python -m pytest -q -k test_Subprocess

To run outside the grader, use Bash from Subprocess/:
    python main.py
The output should match the contents of file1.txt.
"""

import subprocess


def run_subprocess(filename):
    """Return the text that cat reads from filename; propagate command errors."""
    # TODO: Run cat and return its captured standard output.
    pass


if __name__ == "__main__":
    result = run_subprocess("file1.txt")
    print(result, end="")
