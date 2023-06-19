# Projeto Ecore

O projeto Ecore é uma aplicação em Python que visa automatizar e unificar o fluxo de informações ESG do CESAR

## Instalação

Para configurar o projeto, siga as instruções abaixo:

1. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Clone o repositório do projeto:
   ```bash
   git clone https://github.com/Jorrmungandr/ecore
   cd ecore
   ```

3. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração

Antes de executar o projeto, é necessário configurar as tabelas e usuários. Execute o seguinte comando:
   ```bash
   python setup.py
   ```

## Executando o projeto

Para executar o projeto, utilize o seguinte comando:
   ```bash
   python cli.py
   ```

## Tecnologias utilizadas

O projeto Ecore utiliza as seguintes tecnologias:

- Versão simplificada da arquitetura limpa
- Orientação a objeto
- RBAC (Role-Based Access Control)
- Biblioteca externa: Schematics
- Biblioteca externa: Tabulate