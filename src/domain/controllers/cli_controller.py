from src.domain.entities.user_entity import UserEntity

class CLIController:
    allowed_roles: list[str]
    user_requester: UserEntity

    def execute(self):
        '''Gather the data and execute the usecase'''
