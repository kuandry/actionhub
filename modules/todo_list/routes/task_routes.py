from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from modules.todo_list.services.task_service import (
    create_task,
    list_tasks,
    update_task,
    remove_task
)

task_bp = Blueprint("task_bp", __name__, url_prefix="/tasks")

@task_bp.route("/", methods=["GET"])
@login_required
def list_all():
    """Lista todas as tarefas do usuário autenticado"""
    filters = {"user_id": current_user.id}
    tasks = list_tasks(filters)
    return render_template("todo_list.html", tasks=tasks)

@task_bp.route("/create", methods=["POST"])
@login_required
def create():
    """Cria uma nova tarefa para o usuário autenticado"""
    description = request.form.get("description", "").strip()
    priority = request.form.get("priority", "normal")
    
    # Validações básicas
    if not description:
        flash("Descrição da tarefa é obrigatória", "error")
        return redirect(url_for('task_bp.list_all'))
    
    if len(description) > 200:
        flash("Descrição não pode ter mais de 200 caracteres", "error")
        return redirect(url_for('task_bp.list_all'))
    
    try:
        create_task({
            "description": description,
            "priority": priority,
            "user_id": current_user.id
        })
        flash("Tarefa criada com sucesso!", "success")
    except Exception as e:
        flash(f"Erro ao criar tarefa: {str(e)}", "error")
    
    return redirect(url_for('task_bp.list_all'))

@task_bp.route("/<string:task_id>/update", methods=["POST"])
@login_required
def update(task_id):
    """Atualiza uma tarefa existente"""
    description = request.form.get("description", "").strip()
    completed = request.form.get("completed") == "on"
    priority = request.form.get("priority")
    
    # Validações
    if not description:
        flash("Descrição da tarefa não pode estar vazia", "error")
        return redirect(url_for('task_bp.list_all'))
    
    try:
        result = update_task(task_id, {
            "description": description,
            "completed": completed,
            "priority": priority
        })
        
        if result is None:
            flash("Tarefa não encontrada", "error")
        else:
            flash("Tarefa atualizada!", "success")
    except Exception as e:
        flash(f"Erro ao atualizar: {str(e)}", "error")
    
    return redirect(url_for('task_bp.list_all'))

@task_bp.route("/<string:task_id>/delete", methods=["POST"])
@login_required
def delete(task_id):
    """Remove uma tarefa"""
    try:
        result = remove_task(task_id)
        
        if result is None:
            flash("Tarefa não encontrada", "error")
        else:
            flash("Tarefa removida!", "success")
    except Exception as e:
        flash(f"Erro ao remover: {str(e)}", "error")
    
    return redirect(url_for('task_bp.list_all'))
