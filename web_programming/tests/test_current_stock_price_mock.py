from unittest.mock import Mock, patch

from web_programming.current_stock_price import stock_price


def test_stock_price_success():
    html = '<html><span data-testid="qsp-price">228.43</span></html>'

    mock_response = Mock()
    mock_response.text = html

    with patch(
        "web_programming.current_stock_price.httpx.get", return_value=mock_response
    ) as mock_get:
        result = stock_price("AAPL")

    assert result == "228.43"

    mock_get.assert_called_once_with(
        "https://finance.yahoo.com/quote/AAPL?p=AAPL",
        headers={"USER-AGENT": "Mozilla/5.0"},
        timeout=10,
        follow_redirects=True,
    )

def test_stock_price_missing_element():
    # Create HTML that does not contain the expected <span> element with data-testid="qsp-price"
    # Simulates stock price information is unavaialble
    html = "<html><body><p>Stock information unavaialble</p></body></html>"

    mock_response = Mock()
    mock_response.text = html

    with patch(
        "web_programming.current_stock_price.httpx.get", return_value=mock_response
    ) as mock_get:
        result = stock_price("AAPL")

    assert result == ("No <fin-streamer> tag with the specified data-testid attribute found.")

    mock_get.assert_called_once()

def test_stock_price_default_symbol():
    # Test stock price without specifying stock symbol, default should be AAPL
    html = '<html><span data-testid="qsp-price">228.43</span></html>'

    mock_response = Mock()
    mock_response.text = html

    with patch(
        "web_programming.current_stock_price.httpx.get", return_value=mock_response
    ) as mock_get:
        result = stock_price() # << no symbol provided

    assert result == "228.43"

    mock_get.assert_called_once_with(
        "https://finance.yahoo.com/quote/AAPL?p=AAPL",
        headers={"USER-AGENT": "Mozilla/5.0"}, 
        timeout=10, 
        follow_redirects=True
    )