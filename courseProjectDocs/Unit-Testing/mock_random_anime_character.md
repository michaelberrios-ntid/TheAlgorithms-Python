# Unit Testing II - Mocking and Stubbing
Author: Daniel Arcega

## Selected Component
File: web_programming/random_anime_character.py

### Function: random_anime_character()
The `random_anime_character()` function returns an image title and url of a random anime character from "https://www.mywaifulist.moe/random"

### Test Results Before Mocking
```bash
uv run --group test python -m pytest \
  --doctest-modules web_programming/random_anime_character.py \
  --cov=web_programming.random_anime_character \
  --cov-report=term-missing \
  --cov-report=html:htmlcov/baseline
```
| Metric | Before Mocking |
|--------|----------------|
| Test Executed | 0              |
| Tests Passed | 0              |
| Tests Failed | 0              |
| Total Statements | 23             |
| Missing Statements | 14             |
| Statement Coverage | 39%            |
| External HTTP Requests | Yes            |

## New Test Cases and Rationale