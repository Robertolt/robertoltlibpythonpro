from unittest.mock import Mock

import pytest

from robertoltlibpythonpro.spam.email_sender import Sender
from robertoltlibpythonpro.spam.main import SpamSender
from robertoltlibpythonpro.spam.modules import User


class SenderMock(Sender):

    def __init__(self):
        super().__init__()
        self.amt_email_sent = 0
        self.send_parameters = None

    def send(self, shipper, receiver, assunto, corpo):
        self.send_parameters = (shipper, receiver, assunto, corpo)
        self.amt_email_sent += 1


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
    sender = Mock()
    spam_sender = SpamSender(session, sender)
    spam_sender.enviar_emails(
        'rl.beto.lorenzoni@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    assert len(users) == sender.send.call_count


def test_spam_parameter(session):
    user = User(name='Roberto', email='rl.beto.lorenzoni@gmail.com')
    session.save(user)
    sender = Mock()
    spam_sender = SpamSender(session, sender)
    spam_sender.enviar_emails(
        'js.janine@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    sender.send.assert_called_once_with(
        'js.janine@gmail.com',
        'rl.beto.lorenzoni@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos',
    )
