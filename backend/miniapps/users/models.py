from tortoise import models, fields


class User(models.Model):
    id = fields.IntField(pk=True)
    bio = fields.TextField(max_length=255, null=True)
    email = fields.CharField(max_length=320, unque=True, null=True)
    username = fields.CharField(max_length=32, unique=True, null=True)
    fullname = fields.CharField(max_length=64, null=True)
    joined_at = fields.DatetimeField(auto_now_add=True)
