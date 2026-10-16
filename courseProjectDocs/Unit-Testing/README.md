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
### To run tests for Binary to Decimal
```bash
uv run --group test python -m pytest \
  conversions/binary_to_decimal.py \
  conversions/tests/test_binary_to_decimal.py \
  --cov=conversions.binary_to_decimal \
  --cov-branch \
  --cov-report=term-missing
```
