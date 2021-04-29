import pytest

from robertoltlibpythonpro.spam.email_sender import Sender
from robertoltlibpythonpro.spam.main import SpamSender
from robertoltlibpythonpro.spam.modules import User


@pytest.mark.parametrize(
    'users',
    [
        [
             User(name='Roberto',email='rl.beto.lorenzoni@gmail.com'),
             User(name='Janine', email='js.lorenzoni@gmail.com')
        ],
        [
             User(name='Roberto',email='rl.beto.lorenzoni@gmail.com')
        ]
    ]
)
def test_spam_amt(session, users):

    for user in users:
        session.save(user)
    sender = Sender()
    spam_sender = SpamSender(session, sender)
    spam_sender.enviar_emails(
        'rl.beto.lorenzoni@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    assert len(users) == sender.amt_sent_email
