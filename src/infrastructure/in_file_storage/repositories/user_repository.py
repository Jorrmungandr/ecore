from src.domain.entities.user_entity import UserEntity

class UserRepository:
    file_path = './db/users.csv'

    def get_user_by_email(self, user_email) -> UserEntity | None:
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

    def create_user(self, user: UserEntity) -> UserEntity:
        with open(self.file_path, 'a', encoding='utf8') as csv_file:
            _id, name, role, email, password = user.values()

            line = ','.join([str(_id), name, role, email, password])

            csv_file.write(f'\n{line}')

            csv_file.close()

            return user

    def count(self) -> int:
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            count = len(csv_file.readlines()) - 1

            csv_file.close()

            return count

    def get_user_by_id(self, _id) -> UserEntity | None:
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            users = csv_file.readlines()

            users.remove(users[0])

            csv_file.close()

            for user in users:
                user_data = user.strip().split(',')

                if user_data[0] == str(_id):
                    user_id, name, role, email, password = user_data

                    return UserEntity({
                        'id': user_id,
                        'name': name,
                        'role': role,
                        'email': email,
                        'password': password
                    })

    def update_user_by_id(self, _id, name, email) -> UserEntity:
        updated_user = None

        with open(self.file_path, 'r+', encoding='utf8') as csv_file:
            users = csv_file.readlines()

            header = users[0]

            users.remove(header)

            for index, user in enumerate(users):
                user_data = user.strip().split(',')

                if user_data[0] == str(_id):
                    user_data[1] = name
                    user_data[3] = email

                    updated_user = UserEntity({
                        'id': _id,
                        'name': name,
                        'role': user_data[2],
                        'email': email,
                        'password': user_data[4]
                    })

                    users[index] = ','.join(user_data)

                    if '\n' in user:
                        users[index] += '\n'

            csv_file.truncate(0)
            csv_file.seek(0)
            csv_file.write(header)
            csv_file.writelines(users)
            csv_file.close()

        return updated_user

    def get_users(self) -> list[UserEntity]:
        with open(self.file_path, 'r', encoding='utf8') as csv_file:
            file_lines = csv_file.readlines()

            file_lines.remove(file_lines[0])

            users = []

            for line in file_lines:
                user_data = line.strip().split(',')

                user_id, name, role, email, password = user_data

                user_entity = UserEntity({
                    'id': int(user_id),
                    'name': name,
                    'role': role,
                    'email': email,
                    'password': password
                })

                users.append(user_entity)

            csv_file.close()

            return users

    def delete_user(self, _id: str) -> None:
        with open(self.file_path, 'r+', encoding='utf8') as csv_file:
            users = csv_file.readlines()

            header = users[0]

            users.remove(header)

            for index, user in enumerate(users):
                user_data = user.strip().split(',')

                if user_data[0] == str(_id):
                    users.remove(users[index])

            users[-1] = users[-1].replace('\n', '')

            csv_file.truncate(0)
            csv_file.seek(0)
            csv_file.write(header)
            csv_file.writelines(users)
            csv_file.close()
