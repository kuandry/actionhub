from core.extensions import db
from modules.todo_list.models.user import User

def save_user(user):
    """Salva ou atualiza um usuário no banco"""
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_id(user_id):
    """Busca um usuário pelo ID"""
    return db.session.get(User, user_id)

def get_all_users():
    """Lista todos os usuários"""
    return User.query.all()

def update_user(user, data: dict):
    """Atualiza os campos de um usuário"""
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return user

def delete_user(user):
    """Remove um usuário"""
    db.session.delete(user)
    db.session.commit()

def get_user_by_username(username: str):
    """Busca um usuário pelo username"""
    return User.query.filter_by(username=username).first()
