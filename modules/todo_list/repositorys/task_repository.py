from core.extensions import db
from modules.todo_list.models import Task

def save_task(task):
    """Salva ou atualiza uma tarefa no banco"""
    db.session.add(task)
    db.session.commit()
    return task

def get_task_by_id(task_id):
    """Busca uma tarefa pelo ID"""
    return db.session.get(Task, task_id)

def get_all_tasks(filters=None):
    """Lista tarefas, com filtros opcionais"""
    query = Task.query
    if filters:
        if "completed" in filters:
            query = query.filter_by(completed=filters["completed"].lower() == "true")
        if "priority" in filters:
            query = query.filter_by(priority=filters["priority"])
        if "user_id" in filters:
            query = query.filter_by(user_id=filters["user_id"])
    return query.all()

def update_task(task, data: dict):
    """Atualiza os campos de uma tarefa"""
    for key, value in data.items():
        setattr(task, key, value)
    db.session.commit()
    return task

def delete_task(task):
    """Remove uma tarefa"""
    db.session.delete(task)
    db.session.commit()
