# Task Management System

Este é um sistema de gerenciamento de tarefas desenvolvido em Django, semelhante ao Trello, que permite aos usuários criar, visualizar, editar e excluir tarefas, além de acompanhar o progresso das mesmas.

## Tecnologias Utilizadas

- **Django** - Framework de desenvolvimento web em Python.
- **Tailwind CSS** - Framework de CSS para estilização.
- **SQLite** - Banco de dados padrão do Django.

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.10 ou superior
- Node.js e npm (para compilar o Tailwind CSS)
- Git

### Passos para Rodar

1. **Clone o Repositório**

   Clone o repositório para a sua máquina local:

   ```bash
   git clone git@github.com:Joao-Messias/task-management-system.git
   cd task-management-system
   
2. **Crie um Ambiente Virtual**

   Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux e Mac
   .venv\Scripts\activate     # Windows

3. **Instale as Dependências do Python**

   Instale as dependências do Django e outros pacotes necessários executando o comando abaixo:

   ```bash
   pip install -r requirements.txt
   
4. **Instale as Dependências do Tailwind CSS**

   Para configurar o Tailwind CSS, navegue até o diretório do tema do Tailwind (`theme/static_src`) e instale as dependências necessárias com o npm:

   ```bash
   cd theme/static_src
   npm install

5. **Execute as Migrações do Banco de Dados**

   Antes de iniciar o servidor, você precisa aplicar as migrações do banco de dados para criar as tabelas necessárias. Execute o comando abaixo para aplicar as migrações:

   ```bash
   cd ../..
   python manage.py migrate

6. **Compile o CSS com Tailwind**

   Para compilar o CSS utilizando o Tailwind e observar as mudanças em tempo real durante o desenvolvimento, execute o seguinte comando:

   ```bash
   python manage.py tailwind start

7. **Inicie o Servidor do Django**

   Com todas as configurações prontas e as migrações aplicadas, você pode iniciar o servidor do Django para executar a aplicação. Use o comando abaixo:

   ```bash
   python manage.py runserver

8. **Acesso http://127.0.0.1:8000**

