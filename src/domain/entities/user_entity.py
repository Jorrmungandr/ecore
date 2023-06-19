from schematics.types import StringType, IntType, EmailType

from src.domain.entities.base_entity import BaseEntity

user_roles = (
    'admin',
    'departamento_pessoal',
    'capital_humano',
    'marketing',
    'facilities',
    'controladoria',
    'conselho',
)

class UserEntity(BaseEntity):
    id = IntType(required=True)
    name = StringType(required=True)
    role = StringType(required=True, choices=user_roles)
    email = EmailType(required=True)
    password = StringType()

    def __str__(self):
        return f'ID: {self.id}\nNome: {self.name}\nTipo: {self.role}\nEmail: {self.email}'
