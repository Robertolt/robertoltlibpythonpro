import pytest

from robertoltlibpythonpro.spam.db import Connection
from robertoltlibpythonpro.spam.modules import User


@pytest.fixture
def connection():
    connection_obj = Connection()
    yield connection_obj
    connection_obj.close()


@pytest.fixture
def session(connection):
    session_obj = connection.generate_session()
    yield session_obj
    session_obj.roll_back()
    session_obj.close()


def test_save_user(session):
    user = User(name='Roberto')
    session.save(user)
    assert isinstance(user.id, int)




def test_list_user(session):
    users = [User(name='Roberto'), User(name='Janine')]
    for user in users:
        session.save(user)
    assert users == session.list()
