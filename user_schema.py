from tbl_user import User
from marshmallow_sqlalchemy import ModelSchema


class UserSchema(ModelSchema):
    class Meta:
        model = User
