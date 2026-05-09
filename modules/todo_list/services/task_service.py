from core.extensions import db
from modules.todo_list.schemas.task_schema import TaskSchema

from modules.todo_list.repositorys.task_repository import (
    save_task,
    get_task_by_id,
    get_all_tasks,
    update_task as repo_update_task,
    delete_task
)
from modules.todo_list.schemas.task_schema import TaskSchema

def create_task(data: dict):
    """Cria uma nova tarefa"""
    schema = TaskSchema(session=db.session)  # passa a sessão para o schema
    task = schema.load(data)  # valida e cria objeto Task
    saved = save_task(task)
    return schema.dump(saved)

def list_tasks(filters: dict = None):
    """Lista tarefas com filtros opcionais"""
    tasks = get_all_tasks(filters)
    return TaskSchema(many=True).dump(tasks)

def update_task(task_id: str, data: dict):
    """Atualiza uma tarefa existente"""
    task = get_task_by_id(task_id)
    if not task:
        return None
    updated = repo_update_task(task, data)
    return TaskSchema().dump(updated)

def remove_task(task_id: str):
    """Remove uma tarefa"""
    task = get_task_by_id(task_id)
    if not task:
        return None
    delete_task(task)
    return True
