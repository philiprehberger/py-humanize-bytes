"""Convert byte counts to human-readable strings and back, with formatting options."""

from __future__ import annotations

import math
import re

__all__ = ["format_bytes", "parse_bytes"]

_BINARY_UNITS = ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB"]
_SI_UNITS = ["B", "KB", "MB", "GB", "TB", "PB", "EB"]

_PARSE_MAP: dict[str, int | float] = {
    # Binary units
    "b": 1,
    "kib": 1024,
    "mib": 1024**2,
    "gib": 1024**3,
    "tib": 1024**4,
    "pib": 1024**5,
    "eib": 1024**6,
    # SI units
    "kb": 1000,
    "mb": 1000**2,
    "gb": 1000**3,
    "tb": 1000**4,
    "pb": 1000**5,
    "eb": 1000**6,
    # Shorthands (treated as SI)
    "k": 1000,
    "m": 1000**2,
    "g": 1000**3,
    "t": 1000**4,
    "p": 1000**5,
    "e": 1000**6,
}

_PARSE_PATTERN = re.compile(
    r"^\s*([+-]?\d+(?:\.\d+)?)\s*([a-zA-Z]*)\s*$",
)


def format_bytes(
    n: int | float,
    *,
    si: bool = False,
    precision: int = 1,
) -> str:
    """Format a byte count to a human-readable string.

    Args:
        n: Number of bytes (may be negative).
        si: Use SI units (base 1000) instead of binary (base 1024).
        precision: Number of decimal places in the output.

    Returns:
        A formatted string such as ``"1.5 GiB"`` or ``"1.5 GB"``.
    """
    if n == 0:
        return "0 B"

    negative = n < 0
    n = abs(n)

    base = 1000 if si else 1024
    units = _SI_UNITS if si else _BINARY_UNITS

    if n < 1:
        return f"{'-' if negative else ''}{n:.{precision}f} B"

    exponent = min(int(math.log(n, base)), len(units) - 1)
    value = n / base**exponent
    formatted = f"{value:.{precision}f}"

    # Strip trailing zeros after the decimal point if precision > 0
    if "." in formatted:
        formatted = formatted.rstrip("0").rstrip(".")

    prefix = "-" if negative else ""
    return f"{prefix}{formatted} {units[exponent]}"


def parse_bytes(s: str) -> int:
    """Parse a human-readable byte string to an integer byte count.

    Supports formats like ``"1.5 GB"``, ``"1.5 GiB"``, ``"500 KB"``,
    ``"10M"`` (shorthand), and ``"1024"`` (plain number).

    Args:
        s: The string to parse (case-insensitive).

    Returns:
        The number of bytes as an integer.

    Raises:
        ValueError: If the string cannot be parsed.
    """
    match = _PARSE_PATTERN.match(s)
    if match is None:
        raise ValueError(f"Cannot parse byte string: {s!r}")

    number_str, unit_str = match.groups()
    number = float(number_str)

    if not unit_str:
        return int(number)

    unit_lower = unit_str.lower()
    if unit_lower not in _PARSE_MAP:
        raise ValueError(f"Unknown unit: {unit_str!r}")

    return int(number * _PARSE_MAP[unit_lower])
