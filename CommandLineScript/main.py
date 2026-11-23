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
    individual = string.split()#removes all the white spaces when splitting
    return len(individual)


if __name__ == "__main__":
    text = sys.argv[1]#the input file
    with open(text, "r", encoding="utf-8") as textfile:
        text = textfile.read() 
    text = str(text)
    print(f"The file has {num_words(text)} words.")
