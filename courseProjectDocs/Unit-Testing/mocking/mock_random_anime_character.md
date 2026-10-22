# Unit Testing II - Mocking and Stubbing
Author: Daniel Arcega

## Selected Component
File: web_programming/random_anime_character.py

### Function: random_anime_character()
The `random_anime_character()` function returns an image title and url of a random anime character from "https://www.mywaifulist.moe/random"

**Testing results before and after test additions are stored in `Unit-Testing/metrics-collected/web_programming`**

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
The new test cases cover the two existing functions, save_image() and random_anime_character()
Both of these functions make http requests to fulfill their behaviors. Beyond them needing to be tested, using mocking is a good strategy to test them without requiring a proper http response. 

### Mocking Strategy
The main mocked items were `httpx.get()` and `BeautifulSoup`. httpx.get is the function that makes requests to a provided URL. BeautifulSoup is a class that can scrape websites for data.
Stubs were used for expected HTTP responses. Mocked functions were asserted to be called; in particular, `soup.find()` was asserted to be called exactly 3 times during execution.

## Post-Test Results 
```bash
$ uv run --group test python -m pytest  \
 web_programming/tests/test_random_anime_character.py \
  --cov=web_programming.random_anime_character  \
  --cov-report=term-missing \
  --cov-report=html:htmlcov/mocking   -v
```

| Metric | Before Mocking |
|--------|----------------|
| Test Executed | 2              |
| Tests Passed | 2              |
| Tests Failed | 0              |
| Total Statements | 23             |
| Missing Statements | 2              |
| Statement Coverage | 91%            |
| External HTTP Requests | No             |

# Conclusion
By adding test utilizing mocking, coverage has increased by 52% while avoiding lengthy testing that would come with making real http requests.
