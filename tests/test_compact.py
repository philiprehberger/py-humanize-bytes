"""Tests for compact() and format_throughput()."""

from __future__ import annotations

import pytest

from philiprehberger_humanize_bytes import compact, format_throughput


def test_compact_small_si_uses_bytes() -> None:
    assert compact(500) == "500B"


def test_compact_si_kilo() -> None:
    assert compact(1500) == "1.5K"


def test_compact_binary_kilo_rounds() -> None:
    # 1500 / 1024 = 1.4648... -> .1f rounds to "1.5K"
    assert compact(1500, binary=True) == "1.5K"


def test_compact_binary_exact_kilo() -> None:
    assert compact(1024, binary=True) == "1K"


def test_compact_zero() -> None:
    assert compact(0) == "0B"


def test_compact_negative_raises() -> None:
    with pytest.raises(ValueError):
        compact(-1)


def test_compact_si_mega() -> None:
    assert compact(10_000_000) == "10M"


def test_format_throughput_mega() -> None:
    result = format_throughput(1_000_000)
    assert result.endswith("/s")
    assert "MB" in result


def test_format_throughput_zero() -> None:
    assert format_throughput(0) == "0 B/s"


def test_format_throughput_binary() -> None:
    result = format_throughput(1_048_576, binary=True)
    assert result.endswith("/s")
    assert "MiB" in result
