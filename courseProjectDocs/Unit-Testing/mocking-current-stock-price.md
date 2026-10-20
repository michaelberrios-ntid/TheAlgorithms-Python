# Unit Testing II - Mocking and Stubbing
Author: Michael Berrios

## Selected Component
File: web_programming/current_stock_price.py

Function: stock_price()

The `stock_price()` function retrieves stock prices from Yahoo Finance using HTTP requests. This component was selected because it depends on an external service, which can affect test reliability and execution time. Mocking and stubbing allow us to test the function without making actual HTTP requests.

### Test Results Before Mocking
```bash
uv run python -m pytest \
  --doctest-modules web_programming/current_stock_price.py \
  --cov=web_programming.current_stock_price \
  --cov-report=term-missing \
  --cov-report=html:htmlcov/baseline
```

| Metric | Before Mocking |
|--------|-------|
| Test Executed | 1 |
| Tests Passed | 1 |
| Tests Failed | 0 |
| Total Statements | 15 |
| Missing Statements | 4 |
| Statement Coverage | 73% |
| Execution Time | 41.35 seconds |
| External HTTP Requests | Yes |

## New Test Cases and Rationale
Four unit tests were implemented in `web_programming/tests/test_current_stock_price_mock.py`

The test cases were developed by examining the source code using white-box testing to identify the function's conditional statements, return paths, input parameters, and external dependencies. We identified the following scenarios to test:
| Category | What? |
| -------- | ------- |
| Input | **symbol**, a string defaulting to "AAPL" |
| Processing | Construct URL, request HTML, parse HTML, find stock price |
| Output | Stock price string or missing-element message |
| External Dependency | Yahoo Finance through httpx.get() |
| Decision | Whether the expected HTML element exists |

| Test Case | Description | Rationale |
|---|---|---|
| 01 | Successful stock price retrieval | Verify that the function extracts and returns the expected stock price. |
| 02 | Missing stock price element | Verify that the function returns the expected message when the price element is missing. |
| 03 | Default stock symbol | Verify that the function uses `AAPL` by default and constructs the HTTP request correctly. |
| 04 | HTTP request failure | Verify that the function propagates an `httpx.RequestError` when the request fails. |

## Mocking Strategy
Python's `unittest.mock` library was used to replace `httpx.get()` with a mock to avoid actual HTTP requests.

Predetermined HTML responses were used as stubs to test successful and missing stock price scenarios. Mock assertions verified HTTP request arguments and call counts. For request failures, `side_effect` was used to raise an `httpx.RequestError`, which was verified using `pytest.raises()`.

## Coverage Improvement Analysis
Coverage was measured before and after implementing the mocked unit tests using `pytest-cov`.

Before and after metrics were collected and stored in `courseProjectDocs/Unit-Testing/metrics-collected/web_programming`

## Test Results After Mocking
```bash
uv run python -m pytest web_programming/tests/test_current_stock_price_mock.py \
    --cov=web_programming.current_stock_price \
    --cov-report=term-missing \
    --cov-report=html:htmlcov/mocking \
    -v \
    -vv
```

| Metric | Before Mocking | After Mocking |
|---|---|---|
| Tests executed | 1 | 4 |
| Tests passed | 1 | 4 |
| Tests failed | 0 | 0 |
| Total statements | 15 | 15 |
| Missing statements | 4 | 4 |
| Statement coverage | 73% | 73% |
| Execution time | 41.35 seconds | 0.13 seconds |
| External HTTP requests | Yes | No |

## Conclusion
Statement coverage remained at 73% because the original doctest already covered both return paths of `stock_price()`. The remaining uncovered statements (lines 43–48) belong to the `__main__` block.

Although coverage did not increase, the mocked tests provided additional behavioral verification and reduced execution time by approximately **99.69% (318 times faster)**. They also eliminated the dependency on Yahoo Finance during testing.

Mocking and stubbing improved test reliability, isolation, and execution speed without changing production code. All four tests passed, and statement coverage remained at 73%.