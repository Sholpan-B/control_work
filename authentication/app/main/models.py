from tortoise.models import Model
from tortoise import fields
from passlib.hash import bcrypt


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password_hash = fields.CharField(max_length=255)

    async def set_password(self, password: str):
        self.password_hash = bcrypt.hash(password)

    def verify_password(self, password: str) -> bool:
        return bcrypt.verify(password, self.password_hash)


class UserMaterial(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="materials")
    material = fields.ForeignKeyField("models.Material", related_name="users")


class UserTest(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="tests")
    test = fields.ForeignKeyField("models.Test", related_name="users")
    is_passed = fields.BooleanField(default=False)
