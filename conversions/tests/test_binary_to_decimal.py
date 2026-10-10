import pytest

from conversions.binary_to_decimal import bin_to_decimal


def test_single_bit_one():
    assert bin_to_decimal("1") == 1


def test_leading_zeros():
    assert bin_to_decimal("000101") == 5


def test_negative_zero():
    assert bin_to_decimal("-0") == 0


def test_internal_whitespace():
    with pytest.raises(ValueError, match="Non-binary value"):
        bin_to_decimal("10 01")


def test_standalone_negative_sign():
    with pytest.raises(ValueError, match="Non-binary value"):
        bin_to_decimal("-")