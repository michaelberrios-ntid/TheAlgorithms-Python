# New Unit Tests Execution Commands

Author: Daniel Arcega

Run these commands from the base directory

### To run tests for Graph Adjecency Matrix:
    pytest graphs/tests/test_graph_adjacency_matrix.py
### To run doctests for Binary Search
    pytest --doctest-modules searches/binary_search.py
### To run tests for Binary to Decimal
```bash
uv run --group test python -m pytest \
  conversions/binary_to_decimal.py \
  conversions/tests/test_binary_to_decimal.py \
  --cov=conversions.binary_to_decimal \
  --cov-branch \
  --cov-report=term-missing
```
