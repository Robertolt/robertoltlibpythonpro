from unittest.mock import Mock

from robertoltlibpythonpro import github_api


def test_search_for_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'robertolt', 'id': 69603400,
        'avatar': 'https://avatars3.githubusercontent.com/u/69603400?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.search_for_avatar('robertolt')
    assert 'https://avatars.githubusercontent.com/u/69603400?v=4' == url
