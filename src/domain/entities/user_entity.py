user_roles = (
    'admin',
    'departamento_pessoal',
    'capital_humano',
    'cesar_school',
    'marketing',
    'cultura',
    'facilities',
    'controladoria',
    'conselho',
    'c_level'
)


class UserEntity:
    id: int
    name: str
    role: str
    email: str
    password: str

    def __init__(self, _id: int, name: str, role: str, email: str, password: str):
        self.id = _id
        self.name = name

        if role not in user_roles:
            raise TypeError(f'Invalid user role "{role}"')

        self.role = role
        self.email = email
        self.password = password

    def __str__(self):
        return f'id: {self.id}\nname: {self.name}\nrole: {self.role}\nemail: {self.email}'
