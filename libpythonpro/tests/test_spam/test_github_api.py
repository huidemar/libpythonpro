from libpythonpro import github_api
from unittest.mock import Mock
import pytest

def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('huidemar')
    assert avatar_url == url

@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars3.githubusercontent.com/u/13460065?v=4'
    resp_mock.json.return_value = {
        'avatar_url': url
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('huidemar')
    assert 'https://avatars3.githubusercontent.com/u/13460065?v=4' == url