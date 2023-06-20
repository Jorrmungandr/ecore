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
            'mes',
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
        ],
    },
    {
        'name': 'facilities_data',
        'columns': [
            'id',
            'mes',
            'consumo_mensal_de_energia_eletrica',
            'prop_energia_mercado_livre',
            'prop_energia_mercado_cativo',
            'peso_residuos_solidos',
            'gravimetria_residuo_organico',
            'gravimetria_residuo_papel',
            'gravimetria_residuo_plastico',
            'gravimetria_residuo_metais',
            'gravimetria_residuo_eletronicos',
            'gravimetria_residuo_pilhas',
            'prop_residuos_aterrados',
            'prop_residuos_reciclados',
            'consumo_agua_mes',
            'prop_agua_tratada_consumida',
            'consumo_combustivel_mes',
            'qualidade_ar_trabalho',
            'residuos_eletronicos',
            'pilhas',
        ],
    },
    {
        'name': 'marketing_data',
        'columns': [
            'id',
            'mes',
            'quantidade_empresas',
            'projetos_executados_por_ano',
            'nota_glassdoor',
            'recomendam_cesar_amigo',
            'perspectiva_positiva_cesar',
            'indice_sistema_b',
            'comunicacao_questoes_chave',
            'atividades',
        ],
    },
    {
        'name': 'council_data',
        'columns': [
            'id',
            'mes',
            'governanca_estrutura_composicao',
            'presidente_conselho',
            'papel_presidente_conselho_gestao_impacto',
            'delegacao_responsabilidade_gestao_impacto',
        ],
    },
    {
        'name': 'controlling_data',
        'columns': [
            'id',
            'mes',
            'ebitda',
            'faturamento',
        ],
    },
]

has_user_table = os.path.exists('./db/users.csv')

# Setup tables
for table in tables:
    if os.path.exists(f'./db/{table["name"]}.csv'):
        print(f'Skipping {table["name"]} table (already set)')
    else:
        with open(f'./db/{table["name"]}.csv', 'w', encoding='utf8') as table_file:
            table_file.write(f'{",".join(table["columns"])}')

            print(f'Setup {table["name"]} table\n')

            table_file.close()

if not has_user_table:
    with open('./db/users.csv', 'w', encoding='utf8') as users_file:
        admin_user = ['1', 'Admin', 'admin', 'admin@cesar.school', 'Password!123']
        users_file.write(f'\n{",".join(admin_user)}')

        print('Registered admin user:')
        print(f'- Email: {admin_user[3]}')
        print(f'- Password: {admin_user[4]}')
