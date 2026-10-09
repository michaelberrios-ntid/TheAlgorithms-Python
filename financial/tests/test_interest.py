import math
import pytest

from financial.interest import simple_interest, compound_interest, apr_interest

def test_compound_interest_zero_rate():
    # Zero interest should produce zero earnings.
    assert compound_interest(1000, 0, 5) == 0.0


def test_compound_interest_zero_principal():
    # Exactly zero principal should be rejected.
    with pytest.raises(ValueError, match="principal must be > 0"):
        compound_interest(0, 0.05, 5)


def test_simple_interest_zero_days():
    # Exactly zero days should be rejected.
    with pytest.raises(ValueError, match="days_between_payments must be > 0"):
        simple_interest(1000, 0.05, 0)


def test_apr_interest_zero_years():
    # Exactly zero years should be rejected.
    with pytest.raises(ValueError, match="number_of_years must be > 0"):
        apr_interest(1000, 0.05, 0)

def test_compound_interest_fractional_periods():
    # Verify that fractional compounding periods are accepted.
    result = compound_interest(1000, 0.05, 0.5)

    assert result == pytest.approx(24.69507659596)