from marshmallow import fields, validate, pre_load, post_dump
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from modules.todo_list.models.task import Task, PriorityLevel

class TaskSchema(SQLAlchemyAutoSchema):
    priority = fields.String(
        validate=validate.OneOf(["low", "normal", "high"])
    ) 
    
    class Meta:
        model = Task
        load_instance = True
        include_fk = True
        fields = ('id', 'description', 'completed', 'user_id', 'priority')

    @pre_load
    def normalize_priority(self, data, **kwargs):
        """Normalize priority field to lowercase before validation."""
        if "priority" in data and isinstance(data["priority"], str):
            data["priority"] = data["priority"].lower()
        return data

    @post_dump
    def serialize_priority(self, data, **kwargs):
        """Ensure priority is serialized as a plain lowercase string."""
        if "priority" in data and data["priority"] is not None:
            value = data["priority"]
            if isinstance(value, PriorityLevel):
                data["priority"] = value.value
            elif isinstance(value, str) and "." in value:
                data["priority"] = value.split(".")[-1].lower()
            elif isinstance(value, str):
                data["priority"] = value.lower()
        return data