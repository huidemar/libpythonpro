from libpythonpro import github_api
from unittest.mock import Mock

def test_buscar_avatar():

    resp_mock = Mock()
    resp_mock.json.return_value = {
        'avatar_url': 'https://avatars3.githubusercontent.com/u/13460065?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('huidemar')
    assert 'https://avatars3.githubusercontent.com/u/13460065?v=4' == url