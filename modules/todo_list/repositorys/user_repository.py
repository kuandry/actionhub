from core.extensions import db
from modules.todo_list.models.user import User

def save_user(user):
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_id(user_id):
    return db.session.get(User, user_id)

def get_all_users():
    return User.query.all()

def update_user(user, data: dict):
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return user

def delete_user(user):
    db.session.delete(user)
    db.session.commit()

def get_user_by_username(username: str):
    return User.query.filter_by(username=username).first()
