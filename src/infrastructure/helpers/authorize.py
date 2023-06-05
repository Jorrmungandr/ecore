from src.domain.entities.user_entity import user_roles
from src.domain.controllers.cli_controller import CLIController

def authorize(*allowed_roles: list[str]):
    for role in allowed_roles:
        if role not in user_roles:
            raise TypeError(f'Invalid user role "{role}"')

    def decorator(cls):
        def wrapper(*args, **kwargs):
            instance: CLIController = cls(*args, **kwargs)

            instance.allowed_roles = allowed_roles or []

            return instance

        return wrapper

    return decorator
