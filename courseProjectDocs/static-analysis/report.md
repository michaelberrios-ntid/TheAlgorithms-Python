# Static Analysis
author: Daniel Arcega

## Ruff
Ruff is the static analysis tool we used. We chose it due to its ease of installation and use.

### Installation and Execution
Install Ruff with:
    
    uv add --dev Ruff

Run Ruff with:

```bash
uv run ruff check .
```

This will check every file in the repository. 
Replace the '.' with whichever directory you want to specifically test.
By default, Ruff will ingore files dictated in .gitignore

## Initial Findings
| Total Errors | Fixable | Unsafe Fixes |
|--------------|---------|--------------|
| 42           | 19      | 2            |
Fixable errors are those that can be fixed with `--fix`.
Unsafe fixes must be fixed with `--fix --unsafe-fixes`


## Error Identification and Rectifications
Impressively, all but one error found by Ruff were located in code created by our team.
After the automatic fixes, one frequent code smell was discovered in `test_graph_adjacency_matrix.py`.

When writing that code, I frequently put multiple lines under a `pytest.raises()` call:
```
with pytest.raises(ValueError, match=r"already exists in this graph"):
    for v in test_vertices:
        matrix.add_vertex(v)
```
Proper format states that a `pytest.raises()` block should only contain 1 statement:
```
for v in test_vertices:
    with pytest.raises(ValueError, match=r"already exists in this graph"):
        matrix.add_vertex(v)
```

After running `--fix` to automatically amend safe fixes and manually adjusting `test_graph_adjacency_matrix.py`, 
**17 errors** remain within
```
courseProjectCode/Metrics/loc_counter.py
courseProjectCode/Metrics/test_counter.py
maths/zellers_congruence.py
web_programming/tests/test_current_stock_price_mock.py
web_programming/tests/test_random_anime_character.py
```

# Static Analysis
author: Michael Berrios

B015: Pointless Comparison

Ruff identified a B015 code smell in `web_programming/tests/test_random_anime_character.py` at line 88.

The original code was:

```python
fake_soup.find.call_count == 3
```

This statement compares the number of calls to find() against the expected value of 3. However, without an assert statement, Python evaluates the comparison and discards the result. Consequently, the test could pass even if the number of calls was incorrect.

The statement was corrected to:

```python
assert fake_soup.find.call_count == 3
```

This ensures that pytest will fail the test if find() is not called exactly three times.

Verification

The unit tests were executed before and after the correction using:

```python
uv run --group test python -m pytest web_programming/tests/test_random_anime_character.py -v
```
Both executions passed. However, the corrected test now enforces the expected call count rather than evaluating an unused comparison.
