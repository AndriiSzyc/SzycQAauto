import pytest
import requests

"""Tests that send request to the GitHub server.
Testing code status, response body testing, header testing.
"""


@pytest.mark.http
def test_first_request():
    r = requests.get("http://api.github.com/zen")
    print(f"Response is {r.text}")


@pytest.mark.http
def test_second_request():
    r = requests.get("http://api.github.com/users/defunkt")
    body = r.json()
    headers = r.headers

    assert body["name"] == "Chris Wanstrath"
    assert r.status_code == 200
    assert headers["server"] == "GitHub.com"


@pytest.mark.http
def test_status_code():
    r = requests.get("http://api.github.com/users/sergii_butenko")

    assert r.status_code == 404
