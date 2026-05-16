from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError
from modules.todo_list.services.user_service import (
    create_user,
    list_users,
    update_user,
    remove_user,
    authenticate_user
)

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/login", methods=["GET", "POST"])
def login():
    """Autentica usuário e inicia sessão"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        user = authenticate_user(username, password)
        if user:
            login_user(user)
            return redirect(url_for('task_bp.list_all'))
        else:
            flash("Credenciais inválidas", "error")
    
    return render_template("login.html")

@user_bp.route("/register", methods=["GET", "POST"])
def register():
    """Registra um novo usuário no sistema"""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        
        # Validações básicas no backend
        if not username:
            flash("Username é obrigatório", "error")
            return render_template("register.html")
        
        if len(username) < 3:
            flash("Username deve ter no mínimo 3 caracteres", "error")
            return render_template("register.html")
        
        if not password:
            flash("Senha é obrigatória", "error")
            return render_template("register.html")
        
        if len(password) < 6:
            flash("Senha deve ter no mínimo 6 caracteres", "error")
            return render_template("register.html")
        
        try:
            create_user({"username": username, "password": password})
            flash("Usuário criado com sucesso! Faça login.", "success")
            return redirect(url_for('user_bp.login'))
        except IntegrityError:
            flash("Este usuário já existe. Escolha outro nome.", "error")
        except Exception as e:
            flash(f"Erro ao criar usuário: {str(e)}", "error")
    
    return render_template("register.html")

@user_bp.route("/logout")
@login_required
def logout():
    """Encerra a sessão do usuário"""
    logout_user()
    return redirect(url_for('user_bp.login'))
