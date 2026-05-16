# ActionHub

O ActionHub é um gerenciador de tarefas simples e intuitivo.
Ele permite que usuários se registrem, façam login e gerenciem suas tarefas pessoais com prioridade (baixa, normal, alta).
O objetivo é oferecer uma aplicação prática para organização diária, fazendo uso de conceitos adquiridos em sala de aula e um pouco além.
Construída com boas práticas de desenvolvimento web.

## Tecnologias Utilizadas

- **Python 3.10+**
- **Flask** (framework web)
- **SQLAlchemy** (ORM para banco de dados)
- **Marshmallow** (serialização/validação)
- **Flask-Login** (autenticação de usuários)
- **SQLite** (banco de dados local)
- **bcrypt** (hash de senhas)
- **HTML + Jinja2** (templates)
- **CSS** (estilização)

## Como Executar na Sua Máquina

### Clonar o Repositório
Baixe o código do projeto para sua máquina.

```bash
git clone https://github.com/kuandry/actionhub.git
cd actionhub
```

### Criar Ambiente Virtual
Isolar dependências do projeto.

```bash
python -m venv venv
```

**Ativar no Windows:**
```bash
source venv/Scripts/activate
```

**Ativar no Linux/Mac:**
```bash
source venv/bin/activate
```

### Instalar Dependências
Instale todas as bibliotecas necessárias.

```bash
pip install -r requirements.txt
```

### Inicializar Banco de Dados
Crie o banco SQLite com as tabelas.

```bash
python init_db.py
```

Verifique se `instance/database.db` foi criado.

### Rodar Aplicação
Inicie o servidor Flask.

```bash
python app.py
```

Acesse [http://127.0.0.1:5000](http://127.0.0.1:5000) no navegador.

## Gerenciamento do Banco de Dados

### Visualizar Dados do Banco

Para visualizar os dados armazenados no banco SQLite, você pode usar o script `list_db.py`:

```bash
python list_db.py
```

Este script exibe:

Um menu iterativo onde é possivel consultar os dados do banco e até mesmo fazer consultar livre SQL

### Resetar o Banco de Dados

Se precisar limpar todos os dados e recomeçar:

```bash
rm instance/database.db
python init_db.py
```

⚠️ **Atenção:** Isso apagará todos os usuários e tarefas cadastrados.

## Funcionalidades

- ✅ Cadastro e login de usuários
- ✅ Criação, edição e exclusão de tarefas
- ✅ Definição de prioridade (baixa, normal, alta)
- ✅ Modal de confirmação para exclusão
- ✅ Interface moderna com templates Jinja2
- ✅ Banco SQLite local para persistência
- ✅ Validação de dados no frontend e backend
- ✅ Senhas criptografadas com bcrypt

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
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/hiagogabriel2712-tech">
        <img src="https://github.com/hiagogabriel2712-tech.png" width="100px;" alt="Hiago Gabriel"/><br>
        <sub><b>Hiago Gabriel</b></sub>
      </a>
    </td>
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

## Licença

Este projeto foi desenvolvido para fins educacionais.
