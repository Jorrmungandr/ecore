from src.domain.entities.user_entity import user_roles

def authorize(allowed_roles: list[str]):
    for role in allowed_roles:
        if role not in user_roles:
            raise TypeError(f'Invalid user role "{role}"')

    def decorator(cls):
        def wrapper(*args, **kwargs):
            instance = cls(*args, **kwargs)

            return instance

        return wrapper

    return decorator
