from robertoltlibpythonpro.spam.modules import User


def test_save_user(session):
    user = User(name='Roberto', email='rl.beto.lorenzoni@gmail.com')
    session.save(user)
    assert isinstance(user.id, int)




def test_list_user(session):
    users = [User(name='Roberto',email='rl.beto.lorenzoni@gmail.com'),
             User(name='Janine', email='js.lorenzoni@gmail.com')
             ]
    for user in users:
        session.save(user)
    assert users == session.list()
