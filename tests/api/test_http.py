import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print((f"Response is {r.text}").encode("utf-8"))


@ pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    r.status_code == 200
    headers['Server'] == 'GitHub.com'


@ pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/Nataliia_Potii') 

    assert r.status_code == 404
