from src.domain.entities.user_entity import UserEntity

class UserRepository:
    file_path = './db/users.csv'

    def get_user_by_email(self, user_email):
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            for user_line in csv_file.readlines()[1:]:
                _id, name, role, email, password = user_line.strip().split(',')

                if email != user_email:
                    continue

                user_entity = UserEntity({
                    'id': int(_id),
                    'name': name,
                    'role': role,
                    'email': email,
                    'password': password
                })

                return user_entity

            csv_file.close()

            return None

    def create_user(self, user: UserEntity):
        with open(self.file_path, 'a', encoding='utf8') as csv_file:
            _id, name, role, email, password = user.values()

            line = ','.join([str(_id), name, role, email, password])

            csv_file.write(f'\n{line}')

            csv_file.close()

            return user

    def count(self):
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            count = len(csv_file.readlines()) - 1

            csv_file.close()

            return count
