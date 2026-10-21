import pytest

from app import main


@pytest.mark.parametrize(
    ("internet_connection", "valid_url", "expected_result"),
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page_requires_valid_url_and_connection(
    monkeypatch, internet_connection, valid_url, expected_result
):
    url = "https://www.google.com"
    monkeypatch.setattr(main, "has_internet_connection", lambda: internet_connection)
    monkeypatch.setattr(main, "valid_google_url", lambda received_url: valid_url)

    assert main.can_access_google_page(url) == expected_result
