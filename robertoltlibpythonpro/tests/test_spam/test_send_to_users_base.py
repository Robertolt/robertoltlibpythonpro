from robertoltlibpythonpro.spam.email_sender import Sender
from robertoltlibpythonpro.spam.main import SpamSender


def test_spam_sender(session):
    spam_sender = SpamSender(session, Sender())
    spam_sender.enviar_emails(
        'rl.beto.lorenzoni@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )