class UserEntity:
    def __init__(self, _id, name, role, email, password):
        self.id = _id
        self.name = name
        self.role = role
        self.email = email
        self.password = password

    def __str__(self):
        return f'id: {self.id}\nname: {self.name}\nrole: {self.role}\nemail: {self.email}'
