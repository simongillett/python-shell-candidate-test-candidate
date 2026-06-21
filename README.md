# Python and Shell Practical Assessment

## Purpose

This exercise evaluates practical Python and Bash skills in a small, realistic data-processing task.

## Time guideline

Please spend no more than **75 minutes**.

Incomplete work is acceptable. Prioritize correctness, clarity, and explaining your decisions.

## Rules

- You may use Python's standard library.
- You may consult public documentation.
- Follow the hiring team's stated policy on AI-assisted tools.
- Do not add credentials, private data, or company information to this repository.
- Do not modify the sample input data solely to make tests pass.

## Tasks

### 1. Complete the Python program

Complete the TODO sections in:

```text
src/process_orders.py
```

The program must:

1. Read every `.csv` file in the supplied input directory.
2. Require these columns:
   - `order_id`
   - `sku`
   - `quantity`
   - `unit_price`
3. Skip malformed rows without terminating the entire run.
4. Calculate total quantity and total revenue by SKU.
5. Write a deterministic summary ordered by SKU.
6. Log useful errors to standard error.
7. Return a non-zero exit code when it cannot produce a valid result.

Expected output columns:

```csv
sku,total_quantity,total_revenue
```

### 2. Repair the Bash script

Repair:

```text
scripts/run.sh
```

It must:

1. Use appropriate safe Bash settings.
2. Work when launched from any current working directory.
3. Determine the repository path from the script's own location.
4. Create `output/` and `logs/` when needed.
5. Write program output and errors to a timestamped log file.
6. Preserve the Python program's exit status.
7. Compress the summary only after a successful run.
8. Correctly quote paths and filenames.

### 3. Improve or add tests

You may add tests that demonstrate your intended behavior and cover edge cases.

### 4. Record assumptions

Create a file named `NOTES.md` containing:

- assumptions you made;
- known limitations;
- what you would improve with more time.

## Setup in GitHub Codespaces

Open the repository in GitHub Codespaces. The environment will install Python development dependencies and `shellcheck`.

To install dependencies manually:

```bash
python -m pip install -r requirements-dev.txt
```

## Run the Python tests

```bash
pytest
```

## Run linting

```bash
ruff check .
shellcheck scripts/run.sh
```

## Run the complete workflow

```bash
./scripts/run.sh
```

A successful run should create:

```text
output/summary.csv.gz
logs/<timestamp>.log
```

## Run the visible shell test

```bash
bash tests/test_shell.sh
```

## Submission

Before finishing:

1. Create `NOTES.md`.
2. Commit all intended changes.
3. Push the final commit to the assigned repository.
4. Confirm that no credentials or personal data have been committed.
