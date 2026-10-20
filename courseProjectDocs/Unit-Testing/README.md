# New Unit Tests Execution Commands

Author: Daniel Arcega

Run these commands from the base directory

### To run tests for Graph Adjecency Matrix:
```bash
uv run --group test python -m pytest \
  graphs/graph_adjacency_matrix.py \
  graphs/tests/test_graph_adjacency_matrix.py \
  --cov=graphs.graph_adjacency_matrix \
  --cov-branch \
  --cov-report=term-missing
```

### To run doctests for Binary Search
```bash
uv run --group test python -m pytest \
  searches/binary_search.py \
  --cov=searches.binary_search \
  --cov-branch \
  --cov-report=term-missing
```

Author: Michael Berrios

## Unit Testing I - Doctests and Coverage
Test cases, mocking strategy, and coverage analysis are documented in [mocking.md](mocking-current-stock-price.md)

### To run tests for Binary to Decimal
```bash
uv run --group test python -m pytest \
  conversions/binary_to_decimal.py \
  conversions/tests/test_binary_to_decimal.py \
  --cov=conversions.binary_to_decimal \
  --cov-branch \
  --cov-report=term-missing
```

## Unit Testing II - Mocking and Stubbing
### To run doctests for Current Stock Price Before Mocking
```bash
uv run --group test python -m pytest \
  --doctest-modules web_programming/current_stock_price.py \
  --cov=web_programming.current_stock_price \
  --cov-report=term-missing \
  --cov-report=html:htmlcov/baseline
```

### To run tests for Current Stock Price After Mocking
```bash
uv run --group test python -m pytest \
  web_programming/tests/test_current_stock_price_mock.py \
  --cov=web_programming.current_stock_price \
  --cov-report=term-missing \
  --cov-report=html:htmlcov/mocking \
  -v
```