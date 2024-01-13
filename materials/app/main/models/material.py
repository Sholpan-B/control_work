from tortoise.models import Model
from tortoise import fields


class Material(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    content = fields.TextField()

