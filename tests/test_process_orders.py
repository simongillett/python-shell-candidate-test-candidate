from decimal import Decimal
from pathlib import Path

import pytest

from src.process_orders import Totals, parse_row


def test_parse_valid_row() -> None:
    sku, quantity, revenue = parse_row(
        {
            "order_id": "1001",
            "sku": "ABC-100",
            "quantity": "2",
            "unit_price": "19.99",
        },
        Path("orders.csv"),
        2,
    )

    assert sku == "ABC-100"
    assert quantity == 2
    assert revenue == Decimal("39.98")


@pytest.mark.parametrize(
    "row",
    [
        {"order_id": "1", "sku": "", "quantity": "1", "unit_price": "1.00"},
        {"order_id": "1", "sku": "ABC", "quantity": "0", "unit_price": "1.00"},
        {"order_id": "1", "sku": "ABC", "quantity": "two", "unit_price": "1.00"},
        {"order_id": "1", "sku": "ABC", "quantity": "1", "unit_price": "-1.00"},
        {"order_id": "1", "sku": "ABC", "quantity": "1", "unit_price": "bad"},
    ],
)
def test_parse_invalid_rows(row: dict[str, str]) -> None:
    with pytest.raises(ValueError):
        parse_row(row, Path("orders.csv"), 2)


def test_totals_defaults() -> None:
    totals = Totals()
    assert totals.quantity == 0
    assert totals.revenue == Decimal("0.00")
