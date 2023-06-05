import os

if not os.path.exists('./db'):
    os.mkdir('./db')

# Setup tables
if os.path.exists('./db/users.csv'):
    print('Skipping users table (already set)')
else:
    with open('./db/users.csv', 'w', encoding='utf8') as users_table:
        columns = ['id', 'name', 'role', 'email', 'password']

        users_table.write(f'{",".join(columns)}')
        print('Setup users table\n')

        admin_user = ['1', 'Admin', 'admin', 'admin@cesar.school', 'Password!123']
        users_table.write(f'\n{",".join(admin_user)}')

        print('Registered admin user:')
        print(f'- Email: {admin_user[3]}')
        print(f'- Password: {admin_user[4]}')

        users_table.close()
