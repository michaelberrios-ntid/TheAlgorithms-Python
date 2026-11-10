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


# Additional Tests for Kill Surviving Mutants
def test_empty_string_error_message():
    with pytest.raises(ValueError) as exc_info:
        bin_to_decimal("")

    assert str(exc_info.value) == "Empty string was passed to the function"


def test_invalid_character_error_message():
    with pytest.raises(ValueError) as exc_info:
        bin_to_decimal("10X1")

    assert str(exc_info.value) == "Non-binary value was passed to the function"


def test_negative_binary_conversion():
    assert bin_to_decimal("-101") == -5
