from unittest.mock import Mock

import pytest

from robertoltlibpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/69603400?v=4'
    resp_mock.json.return_value = {
        'login': 'Robertolt',
        'id': 69603400,
        'avatar_url': url,
    }
    get_mock = mocker.patch('robertoltlibpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url



def test_search_for_avatar(avatar_url):
    url = github_api.search_for_avatar('Robertolt')
    assert avatar_url == url


def test_search_for_avatar_integration():
    url = github_api.search_for_avatar('Robertolt')
    assert 'https://avatars.githubusercontent.com/u/69603400?v=4' == url
