from robertoltlibpythonpro.spam.db import Connection
from robertoltlibpythonpro.spam.modules import User


def test_save_user():
    connection = Connection()
    session = connection.generate_session()
    user = User(name='Roberto')
    session.save(user)
    assert isinstance(user.id, int)
    session.roll_back()
    session.close()
    connection.close()


def test_list_user():
    connection = Connection()
    session = connection.generate_session()
    users = [User(name='Roberto'), User(name='Janine')]
    for user in users:
        session.save(user)
    assert users == session.list()
    session.roll_back()
    session.close()
    connection.close()