from src.domain.entities.user_entity import UserEntity

class UserRepository:
    def get_user_by_email(self, user_email):
        with open('./db/users.csv', 'r', encoding='utf8') as csv_file:
            for user_line in csv_file.readlines()[1:]:
                _id, name, role, email, password = user_line.strip().split(',')

                if email != user_email:
                    continue

                user_entity = UserEntity(int(_id), name, role, email, password)

                return user_entity

            return None

    def create_user(self, name, role, email, password):
        with open('./db/users.csv', 'r+', encoding='utf8') as csv_file:
            _id = len(csv_file.readlines())

            csv_file.write(f'\n{_id},{name},{email},{password}')

            return UserEntity(_id, name, role, email, password)
