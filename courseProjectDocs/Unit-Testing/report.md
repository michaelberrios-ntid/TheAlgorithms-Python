## Binary to Decimal — Unit Testing Report

**Algorithm:** `conversions/binary_to_decimal.py`

### Testing Approach and Rationale

Five additional pytest tests were developed using Boundary Value Analysis (BVA), equivalence partitioning, and edge-case testing. These tests examine minimum valid inputs, leading zeros, negative zero, internal whitespace, and incomplete negative numbers not explicitly covered by existing doctests.

### Test Cases and Results

| Test Case | Expected Result | Status |
|---|---|---|
| Single-bit `"1"` | `1` | PASS |
| Leading zeros `"000101"` | `5` | PASS |
| Negative zero `"-0"` | `0` | PASS |
| Internal whitespace `"10 01"` | `ValueError` | PASS |
| Standalone negative sign `"-"` | `ValueError` | FAIL (returned `0`) |

**Execution summary:** 6 tests collected, 5 passed, 1 failed (including the existing doctest).

### Coverage Improvement Analysis

| Metric | Baseline | After Testing |
|---|---|---|
| Pytest items | 1 | 6 |
| Statement coverage | 87.5% | 87.5% |
| Combined statement and branch coverage | 88% | 88% |
| Missing lines | 41–43 | 41–43 |

Coverage remained unchanged because the existing doctests already exercised the algorithm's executable statements and branches. The uncovered lines belong to the standalone doctest runner rather than the conversion logic.

### Test Execution

From the repository root:

```bash
uv run --group test python -m pytest \
  conversions/binary_to_decimal.py \
  conversions/tests/test_binary_to_decimal.py \
  --cov=conversions.binary_to_decimal \
  --cov-branch \
  --cov-report=term-missing
```

**Environment:** Ubuntu Linux, Python 3.14.8, pytest 9.1.1, pytest-cov 7.1.0.

### Defect Identified and Conclusion

The standalone negative sign (`"-"`) revealed an input-validation defect. After removing the negative sign, the function evaluates an empty string using `all()`, which returns `True`, causing the function to return `0` instead of raising `ValueError`.

The defect remains unresolved in the original implementation. The failing test is retained as evidence and can serve as a regression test once the defect is corrected.

Although coverage remained at 88%, the additional tests identified a defect that the existing doctests missed, demonstrating the value of boundary-value and edge-case testing beyond code coverage.