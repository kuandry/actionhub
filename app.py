from flask import Flask, render_template
from dotenv import load_dotenv
from core.extensions import db, login_manager, ma
import os

load_dotenv()

app = Flask(__name__)
print(app)

#Basic Configurations
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

if not app.config['SECRET_KEY']:
    raise ValueError("SECRET_KEY is not set in the environment variables. Please set it in the .env file.") 

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializations
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'user_bp.login'
ma.init_app(app)

# User loader para Flask-Login
from modules.todo_list.models.user import User

@login_manager.user_loader
def load_user(user_id):
    """Carrega usuário da sessão para Flask-Login"""
    return db.session.get(User, user_id)

# Registrar blueprints
from modules.todo_list.routes.task_routes import task_bp 
from modules.todo_list.routes.user_routes import user_bp 

app.register_blueprint(task_bp)
app.register_blueprint(user_bp)

# Routes test
@app.route('/health')
def health():
    """Endpoint de health check"""
    return {"status": "ok"}, 200

@app.route('/')
def index():
    """Rota raiz redireciona para login"""
    return render_template('login.html')

if __name__ == '__main__': # Nunca rodar em produção com debug=True
    app.run(debug=True)