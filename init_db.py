"""Script para inicializar o banco de dados SQLite"""
from app import app
from core.extensions import db

with app.app_context():
    db.create_all()
    print("✅ Banco de dados criado com sucesso!")
    print("📁 Localização: instance/database.db")
