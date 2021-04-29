class SpamSender:
    def __init__(self, session, sender):
        self.session = session
        self.sender = sender

    def enviar_emails(self, remente, assunto, corpo):
        for user in self.session.list():
            self.sender.send(
                remente,
                user.email,
                assunto,
                corpo
            )
