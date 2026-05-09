import enum
from core.base_models import BaseModel
from core.extensions import db


class PriorityLevel(enum.Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"


class Task(BaseModel):
    __tablename__ = 'task'

    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    priority = db.Column(
        db.Enum(PriorityLevel, values_callable=lambda e: [v.value for v in e]),
        default=PriorityLevel.NORMAL
    )
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)