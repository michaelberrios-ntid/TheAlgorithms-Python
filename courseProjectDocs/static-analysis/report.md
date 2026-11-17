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

## Michael's Initial Findings

| Total Errors | Fixable | Unsafe Fixes |
|--------------|---------|--------------|
| 16           | 0       | 2            |

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

## Extra Fixes
### E501: Line Too Long

Ruff identified two E501 violations in `web_programming/tests/test_current_stock_price_mock.py` at lines 30 and 42.

- **Line 30:** Split a lengthy comment into two lines.
- **Line 42:** Wrapped the assertion across multiple lines using parentheses.

Both corrections improve code readability and comply with Ruff's 88-character limit without changing the test's functionality.

### Verification

Executed Ruff and pytest:

```bash
uv run ruff check web_programming/tests/test_current_stock_price_mock.py
uv run --group test python -m pytest web_programming/tests/test_current_stock_price_mock.py -v
```

**Results:** Ruff checks passed, and all 4 unit tests passed (1 unrelated GIL warning). Both E501 violations were successfully resolved.

## Michael's Post-Fix Findings

| Total Errors | Fixable | Unsafe Fixes |
|--------------|---------|--------------|
| 13 | 0 | 2 |

After correcting one B015 violation and two E501 violations, Ruff reported 13 remaining errors, compared to the initial 16.

All three corrections were verified through Ruff and pytest without introducing test failures. The remaining violations are outside the scope of these corrections.
