from unittest.mock import Mock

import pytest

from robertoltlibpythonpro import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/69603400?v=4'
    resp_mock.json.return_value = {
        'login': 'Robertolt',
        'id': 69603400,
        'avatar_url': url,
    }
    original_get = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = original_get


def test_search_for_avatar(avatar_url):
    url = github_api.search_for_avatar('Robertolt')
    assert avatar_url == url


def test_search_for_avatar_integration():
    url = github_api.search_for_avatar('Robertolt')
    assert 'https://avatars.githubusercontent.com/u/69603400?v=4' == url
