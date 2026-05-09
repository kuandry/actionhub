O ActionHub é um gerenciador de tarefas simples e intuitivo.
Ele permite que usuários se registrem, façam login e gerenciem suas tarefas pessoais com prioridade (baixa, normal, alta).
O objetivo é oferecer uma aplicação prática para organização diária, fazendo uso de conceitos adquiridos em sala de aula
e um pouco alem.
Construída com boas práticas de desenvolvimento web.

Tecnologias utilizadas
Python 3.10+

Flask (framework web)

SQLAlchemy (ORM para banco de dados)

Marshmallow (serialização/validação)

Flask-Login (autenticação de usuários)

SQLite (banco de dados local)

bcrypt (hash de senhas)

HTML + Jinja2 (templates)

CSS (estilização)

Como executar na sua máquina
1
Clonar o repositório
Baixe o código do projeto para sua máquina.

Abra o terminal

Rode 
```
git clone https://github.com/seuusuario/actionhub.git
```
Entre na pasta cd actionhub

2
Criar ambiente virtual
Isolar dependências do projeto.

Rode 
```
python -m venv venv
```

Ative com source 
```
venv/Scripts/activate (Windows Git Bash)
```
Ou 
```
source venv/bin/activate (Linux/Mac)
```
3
Instalar dependências
Instale todas as bibliotecas necessárias.

Com venv ativo, rode 
```
pip install -r requirements.txt
```
4
Inicializar banco de dados
Crie o banco SQLite com as tabelas.

Rode 
```
python init_db.py
```
Verifique se instance/database.db foi criado

5
Rodar aplicação
Inicie o servidor Flask.
```
Rode python app.py
```
Acesse http://127.0.0.1:5000 no navegador

 Funcionalidades
Cadastro e login de usuários

Criação, edição e exclusão de tarefas

Definição de prioridade (baixa, normal, alta)

Interface simples com templates Jinja2

Banco SQLite local para persistência
