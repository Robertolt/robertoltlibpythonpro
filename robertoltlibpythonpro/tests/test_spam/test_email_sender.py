from robertoltlibpythonpro.spam.email_sender import Sender


def test_criate_email_sender():
    sender= Sender()
    assert sender is not None

def test_receiver():
    sender= Sender()
    result = sender.send('rl.beto.lorenzoni@gmail.com',
                'janine.slorenzoni@gmail.com',
                'Curso Python Pro',
                'Inicio das turmas Von Rossom'
    )
    assert 'rl.beto.lorenzoni@gmail.com' in result