from core.base_models import BaseModel
from core.extensions import db
from flask_login import UserMixin

class User(BaseModel, UserMixin):
    __tablename__ = 'user'

    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    tasks = db.relationship('Task', backref='user', lazy=True)
