"""In this exercise, you will read a threshold from an environment variable
and count how many measurements are greater than or equal to it.

Read MIN_SIGNAL from the environment and convert it to a number. If it is
unset, use 0.5. Print the number of measurements that meet the threshold.

Run the tests from the repository root:
    python -m pytest -q -k test_EnvironmentVariables
The grader supplies MIN_SIGNAL automatically, including when run locally.

To run outside the grader, use Bash from EnvironmentVariables/:
    export MIN_SIGNAL=0.3
    python main.py           # expected: 2
    unset MIN_SIGNAL
    python main.py           # expected: 1 (uses the default)
"""

import os


if __name__ == "__main__":
    measurements = [0.12, 0.48, 0.83]
    mode = float(os.getenv("THRESHOLD", 0.5))#default to o.5

    count = 0
    for i in measurements:
        if measurements >= mode:
            count += 1

    print(count)
    pass
