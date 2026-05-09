from core.extensions import db
from modules.todo_list.schemas.user_schema import UserSchemaPublic, UserSchemaPrivate
from modules.todo_list.repositorys.user_repository import (
    save_user,
    get_user_by_id,
    get_all_users,
    update_user as repo_update_user,
    delete_user,
    get_user_by_username
)
import bcrypt

def create_user(data: dict):
    schema = UserSchemaPrivate(session=db.session)  # passa a sessão
    user = schema.load(data)  # valida e cria objeto User
    
    # Hash da senha antes de salvar
    user.password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    saved = save_user(user)
    return UserSchemaPublic().dump(saved)  # Nunca retornar senha

def list_users():
    users = get_all_users()
    return UserSchemaPublic(many=True).dump(users)

def update_user(user_id: str, data: dict):
    user = get_user_by_id(user_id)
    if not user:
        return None
    
    # Se estiver atualizando senha, fazer hash
    if 'password' in data:
        data['password'] = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    updated = repo_update_user(user, data)
    return UserSchemaPublic().dump(updated)  # Nunca retornar senha

def remove_user(user_id: str):
    user = get_user_by_id(user_id)
    if not user:
        return None
    delete_user(user)
    return True

def authenticate_user(username: str, password: str):
    """Autentica usuário verificando username e senha"""
    user = get_user_by_username(username)
    if not user:
        return None
    
    # Verifica senha com bcrypt
    if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return user
    return None
