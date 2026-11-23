"""In this exercise, you will read a filename from the command line and
print how many words are in that file.

Complete num_words(string) to return the number of whitespace-separated
words. Then use sys.argv to get the filename, read the file, and print:
    The file has <count> words.

Run the tests from the repository root:
    python -m pytest -q -k test_CommandLineScript
The grader checks the function and the command-line script separately.

To run outside the grader, use Bash from CommandLineScript/:
    python main.py sample.txt
    # The file has 9 words.
"""

import sys


def num_words(string: str) -> int:
    """Return the number of whitespace-separated words in string."""
    # TODO: Return the word count.
    pass


if __name__ == "__main__":
    # TODO: Read the file named by sys.argv[1] into text.
    text = ...
    print(f"The file has {num_words(text)} words.")
