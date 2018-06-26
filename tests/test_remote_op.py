import pytest
import requests

@pytest.fixture
def stub_request():
    return { 'title': 'First title' }

def make_request():
    return requests.get('https://jsonplaceholder.typicode.com/posts/1')

def test_request(mocker):
    mocker.patch.object(requests.get, 'req_get', return_value=stub_request())
    res = make_request()
    result = res.json()
    print(result)
    assert result['title'] == 'First title'