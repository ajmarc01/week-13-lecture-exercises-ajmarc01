"""In this exercise, you will use argparse to read a filename and search
string from the command line, then count matches in the file.

Count non-overlapping substring matches, including matches inside longer
words. For example, "law" matches both "law" and "laws". Matching is
case-sensitive by default. Add --ignore-case so users can also count
matches regardless of capitalization.

Keep the filename and search string as positional arguments. Print:
    The word <search string> occurred <count> times in <filename>
Use the original search string in the output. Make --help describe both
positional arguments and the --ignore-case flag.

Run the tests from the repository root:
    python -m pytest -q -k test_ArgparseScript

To run outside the grader, use Bash from ArgparseScript/:
    python main.py file1.txt matter
    # The word matter occurred 5 times in file1.txt
    python main.py file1.txt matter --ignore-case
    # The word matter occurred 6 times in file1.txt
    python main.py --help
"""

import argparse


if __name__ == "__main__":
    # TODO: Parse arguments, read the file, and count substring matches.
    filename = ...
    word = ...
    count = ...
    print(f"The word {word} occurred {count} times in {filename}")
