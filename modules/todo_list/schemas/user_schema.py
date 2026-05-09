from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from modules.todo_list.models.user import User

class UserSchemaPublic(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        fields = ('id', 'username')

class UserSchemaPrivate(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        fields = ('id', 'username', 'password')