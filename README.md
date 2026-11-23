# Week 13 Lecture Exercises

Complete these exercises in the order of lesson 13.1. Instructions and sample
commands are in each exercise's `main.py`. The existing Canvas quiz for 13.3
is separate.

| Order | Working directory | Task |
| --- | --- | --- |
| 1 | `EnvironmentVariables/` | Read a signal threshold from `MIN_SIGNAL`. |
| 2 | `ConfigurationSecrets/` | Load a `.env` file in Bash and read configuration. |
| 3 | `Subprocess/` | Capture command output with `run_subprocess(filename)`. |
| 4 | `CommandLineScript/` | Count words using `sys.argv`. |
| 5 | `ArgparseScript/` | Count substring matches and add `--ignore-case`. |

Run sample commands from the corresponding exercise directory. Expected
outputs are shown in `main.py`. Keep your local `.env` out of Git;
`.env.example` contains the fake key for this exercise.

## Run the tests

Use a Python environment with `pytest` installed. From the repository root,
run the same grader used by GitHub Actions:

```bash
python .github/scripts/grade.py
```

Each exercise is worth one point, for five points total. The grader prints a
summary and writes `grading-results.json`. Tests will fail until you complete
the starter code.

To run the full suite or check one exercise:

```bash
python -m pytest -q
python -m pytest -q -k test_EnvironmentVariables
python -m pytest -q -k test_ConfigurationSecrets
python -m pytest -q -k test_Subprocess
python -m pytest -q -k test_CommandLineScript
python -m pytest -q -k test_ArgparseScript
```

Edit the exercise files; leave `tests/` and `.github/` unchanged. Commit and
push your work to GitHub to run autograding.
