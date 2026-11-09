# Static Analysis
author: Daniel Arcega

## Ruff
Ruff is the static analysis tool we used. We chose it due to its ease of installation and use.

### Installation and Execution
Install Ruff with:
    
    uv add --dev ruff

Run Ruff with:

    uv run ruff check .
This will check every file in the repository. 
Replace the '.' with whichever directory you want to specifically test.
By default, ruff will ingore files dictated in .gitignore

## Initial Findings
| Total Errors | Fixable | Unsafe Fixes |
|--------------| ------- | ---------- |
| 238          | 39 | 6 |
Fixable errors are those that can be fixed with `--fix`.
Unsafe fixes must be fixed with `--fix --unsafe-fixes`


## Error Identification and Rectifications