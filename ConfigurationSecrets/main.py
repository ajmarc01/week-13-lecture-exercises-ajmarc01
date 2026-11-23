"""In this exercise, you will read a report label and an API key from the
environment, then print the label and whether a key was provided.

Read REPORT_LABEL and DATA_API_KEY. Print the label as:
    Report label: <label>
Print "API key configured: True" if the key is nonempty, or
"API key configured: False" if it is missing or empty. Never print the key.

Run the tests from the repository root:
    python -m pytest -q -k test_ConfigurationSecrets
The grader supplies the environment values automatically, including locally.

To run outside the grader, use Bash from ConfigurationSecrets/. Copy the
provided template to .env and load its settings into the environment:
    cp .env.example .env
    set -a
    source .env
    set +a
    python main.py
    # Report label: Signal screening
    # API key configured: True

Remove the key to check the missing-key case:
    unset DATA_API_KEY
    python main.py
    # Report label: Signal screening
    # API key configured: False
    unset REPORT_LABEL

The example key is fake. Keep your .env file out of Git.
"""

import os


if __name__ == "__main__":
    label = os.getenv("REPORT_LABEL")
    api_key = os.getenv("DATA_API_KEY")
    print(f"Report label: ",label)

    if api_key:#check if api key exists
        print("API key configured: True")
    else:
        print("API key configured: False")