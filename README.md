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
git clone https://github.com/kuandry/actionhub.git
```
Entre na pasta cd actionhub

2
Criar ambiente virtual
Isolar dependências do projeto.

Rode 
```
python -m venv venv
```

Ative com source no windows
```
source venv/Scripts/activate
```
Ou para linux ou mac
```
source venv/bin/activate
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
python app.py
```
Acesse http://127.0.0.1:5000 no navegador

 Funcionalidades
Cadastro e login de usuários

Criação, edição e exclusão de tarefas

Definição de prioridade (baixa, normal, alta)

Interface simples com templates Jinja2

Banco SQLite local para persistência


## Colaboradores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/kuandry">
        <img src="https://github.com/kuandry.png" width="100px;" alt="Douglas da Silva Santos"/><br>
        <sub><b>Douglas da Silva Santos</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/natamdossantos6-gif">
        <img src="https://github.com/natamdossantos6-gif.png" width="100px;" alt="Natan dos Santos"/><br>
        <sub><b>Natam dos Santos Silva</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Feehf">
        <img src="https://github.com/Feehf.png" width="100px;" alt="Fernanda Feitosa"/><br>
        <sub><b>Fernanda Feitosa Simões Santos</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/felphs1003">
        <img src="https://github.com/felphs1003.png" width="100px;" alt="Luis Felype"/><br>
        <sub><b>Luis Fylipe Lopes da Silva</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/hiagogabriel2712-tech">
        <img src="https://github.com/hiagogabriel2712-tech.png" width="100px;" alt="Hiago Gabriel"/><br>
        <sub><b>Hiago Gabriel</b></sub>
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/kaua-menezes-dev">
        <img src="https://github.com/kaua-menezes-dev.png" width="100px;" alt="Kawan Menezes"/><br>
        <sub><b>Kauã Victor Ferreira Menezes</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/nicholasborba">
        <img src="https://github.com/nicholasborba.png" width="100px;" alt="Nicholas Borba"/><br>
        <sub><b>Nicholas Borba Batista</b></sub>
      </a>
    </td>
  </tr>
</table>


