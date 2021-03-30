class Sender:
    def send(self, shipper, receiver, assunto, corpo):
        if '@' not in shipper:
            raise InvalidEmail(f'Invalid shipper email: {shipper}')
        return shipper


class InvalidEmail(Exception):
    pass
