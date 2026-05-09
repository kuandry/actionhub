from marshmallow import fields, validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from modules.todo_list.models.task import Task

class TaskSchema(SQLAlchemyAutoSchema):
    priority = fields.String(
        validate=validate.OneOf(["low", "normal", "high"])
    ) 
    
    class Meta:
        model = Task
        load_instance = True
        fields = ('id', 'description', 'completed', 'user_id', 'priority')