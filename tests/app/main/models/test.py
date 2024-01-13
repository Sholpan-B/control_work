from tortoise.models import Model
from tortoise import fields


class Test(Model):
    id = fields.IntField(pk=True)
    question = fields.TextField()
    answer = fields.CharField(max_length=255)
    material = fields.ForeignKeyField("models.Material", related_name="tests")

