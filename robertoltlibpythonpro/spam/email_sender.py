class Sender:
    def __init__(self):
        self.amt_sent_email = 0

    def send(self, shipper, receiver, assunto, corpo):
        if '@' not in shipper:
            raise InvalidEmail(f'Invalid shipper email: {shipper}')
        self.amt_sent_email += 1
        return shipper


class InvalidEmail(Exception):
    pass
