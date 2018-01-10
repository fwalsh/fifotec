import requests


def test_signup_button():
    resp = requests.get('http://nginx:8000/')
    assert 'Try it now' in resp.text
