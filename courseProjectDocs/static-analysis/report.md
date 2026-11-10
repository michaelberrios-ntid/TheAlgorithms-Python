# Static Analysis
author: Daniel Arcega

## Ruff
Ruff is the static analysis tool we used. We chose it due to its ease of installation and use.

### Installation and Execution
Install Ruff with:
    
    uv add --dev Ruff

Run Ruff with:

    uv run Ruff check .
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