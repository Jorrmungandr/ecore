import os

if not os.path.exists('./db'):
    os.mkdir('./db')

tables = [
    {
        'name': 'users',
        'columns': ['id', 'name', 'role', 'email', 'password'],
    },
    {
        'name': 'human_capital_data',
        'columns': [
            'id',
            'colaboradores_lgbtqia',
            'colaboradores_negros',
            'colaboradoras_mulheres',
            'idade_media_colaboradores',
            'colaboradores_pcd',
            'colaboradores_minorizados',
            'mulheres_lideranca_tecnica',
            'mulheres_media_lideranca',
            'mulheres_alta_lideranca',
            'pessoas_negras_lideranca_tecnica',
            'pessoas_negras_media_lideranca',
            'pessoas_negras_alta_lideranca',
            'total_colaboradores',
            'total_estagiarios',
            'pcds',
            'pessoas_pardas',
            'pessoas_pretas',
            'mulheres',
            'cinquenta_mais',
            'e_nps',
            'turnover_ate_julho_2022',
            'indice_recrutamento_interno',
            'vagas_recrutamento_interno',
            'detalhes_organizacionais',
            'periodo_frequencia_relatorio',
        ]
    }
]

# Setup tables
for table in tables:
    if os.path.exists(f'./db/{table["name"]}.csv'):
        print(f'Skipping {table["name"]} table (already set)')
    else:
        with open(f'./db/{table["name"]}.csv', 'w', encoding='utf8') as table_file:
            table_file.write(f'{",".join(table["columns"])}')

            print(f'Setup {table["name"]} table\n')

            table_file.close()

if not os.path.exists('./db/users.csv'):
    with open('./db/users.csv', 'w', encoding='utf8') as users_file:
        admin_user = ['1', 'Admin', 'admin', 'admin@cesar.school', 'Password!123']
        users_file.write(f'\n{",".join(admin_user)}')

        print('Registered admin user:')
        print(f'- Email: {admin_user[3]}')
        print(f'- Password: {admin_user[4]}')
