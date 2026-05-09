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
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
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
    logout_user()
    return redirect(url_for('user_bp.login'))
