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
