from marshmallow import fields, validate, validates, ValidationError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from modules.todo_list.models.user import User

class UserSchemaPublic(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        fields = ('id', 'username')

class UserSchemaPrivate(SQLAlchemyAutoSchema):
    username = fields.String(
        required=True,
        validate=[
            validate.Length(min=3, max=150, error="Username deve ter entre 3 e 150 caracteres"),
            validate.Regexp(r'^[a-zA-Z0-9_@.-]+$', error="Username contém caracteres inválidos")
        ]
    )
    password = fields.String(
        required=True,
        validate=validate.Length(min=6, error="Senha deve ter no mínimo 6 caracteres")
    )
    
    class Meta:
        model = User
        load_instance = True
        fields = ('id', 'username', 'password')