#!/usr/bin/env python3
"""Aggregate order CSV files by SKU.

Candidate task:
- Complete the TODO items.
- Use the Python standard library.
- Preserve useful error messages and exit codes.
"""

from __future__ import annotations

import argparse
import csv
import logging
import sys
from collections import defaultdict
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Iterable

REQUIRED_COLUMNS = {"order_id", "sku", "quantity", "unit_price"}


@dataclass
class Totals:
    quantity: int = 0
    revenue: Decimal = Decimal("0.00")


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
        stream=sys.stderr,
    )


def discover_csv_files(input_dir: Path) -> list[Path]:
    """Return CSV files in deterministic order."""
    # TODO: validate the input path and return all .csv files.
    raise NotImplementedError


def parse_row(row: dict[str, str], source: Path, line_number: int) -> tuple[str, int, Decimal]:
    """Validate and parse one CSV row.

    Return:
        (sku, quantity, line_revenue)

    Raise:
        ValueError for malformed data.
    """
    # TODO: validate SKU, quantity, and unit price.
    # Quantity must be a positive integer.
    # Unit price must be a non-negative decimal value.
    raise NotImplementedError


def process_file(path: Path, totals: dict[str, Totals]) -> tuple[int, int]:
    """Process one CSV file.

    Return:
        (valid_rows, invalid_rows)
    """
    # TODO:
    # - Open the file safely.
    # - Validate the header.
    # - Continue after malformed rows.
    # - Log row-level errors.
    raise NotImplementedError


def write_summary(output_file: Path, totals: dict[str, Totals]) -> None:
    """Write a deterministic summary CSV ordered by SKU."""
    # TODO:
    # - Create the parent directory.
    # - Write sku,total_quantity,total_revenue.
    # - Format revenue to two decimal places.
    raise NotImplementedError


def run(input_dir: Path, output_file: Path) -> int:
    """Run the aggregation and return a process exit code."""
    # TODO:
    # - Discover files.
    # - Return non-zero if no CSV files are found.
    # - Process all files.
    # - Write output if at least one valid row exists.
    # - Log a short completion summary.
    return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Aggregate order CSV files by SKU.")
    parser.add_argument("input_dir", type=Path, help="Directory containing CSV files")
    parser.add_argument("output_file", type=Path, help="Output summary CSV")
    return parser


def main() -> int:
    configure_logging()
    args = build_parser().parse_args()
    return run(args.input_dir, args.output_file)


if __name__ == "__main__":
    raise SystemExit(main())
