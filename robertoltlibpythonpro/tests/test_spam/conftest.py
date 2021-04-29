import pytest

from robertoltlibpythonpro.spam.db import Connection


@pytest.fixture(scope='session')
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
