#!/usr/bin/env bash

# Candidate task:
# Repair this script so it:
# - uses safe Bash settings;
# - works regardless of the caller's current directory;
# - creates output and log directories;
# - logs to a timestamped file;
# - preserves the Python program's exit status;
# - compresses the CSV only after a successful run;
# - handles paths containing spaces.

python src/process_orders.py data output/summary.csv
gzip -f output/summary.csv
