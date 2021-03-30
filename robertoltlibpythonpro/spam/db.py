class Session:
    counter = 0
    users = []

    def save(self, user):
        Session.counter += 1
        user.id = Session.counter
        self.users.append(user)

    def list(self):
        return self.users

    def roll_back(self):
        pass

    def close(self):
        pass


class Connection:
    def generate_session(self):
        return Session()

    def close(self):
        pass