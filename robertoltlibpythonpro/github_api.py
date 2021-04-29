import requests


def search_for_avatar(user: str) -> str:
    """
    Buscar o avatar de um user do github
    :param user:str
    :return:str
    """
    url = f'https://api.github.com/users/{user}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


