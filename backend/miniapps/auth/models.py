from tortoise import models, fields
from miniapps.users.models import *
from toolbox.tokens import *


class BaseToken(models.Model):
    id = fields.UUIDField(pk=True)
    owner = fields.OneToOneField('models.User')
    token = fields.CharField(max_length=320, unique=True, null=True)

    class Meta:
        abstract = True


class LoginToken(BaseToken):
    @staticmethod
    async def issue(owner: User):
        ltok, fresh = await LoginToken.get_or_create(owner=owner)
        if fresh:
            token = issue_login_token(str(ltok.id))
            ltok.token = token
            await ltok.save()
        return ltok

    @staticmethod
    async def invalidate_by_id(id: str):
        ltok = await LoginToken.get_or_none(id=id)
        if ltok != None:
            await ltok.delete()
            return True
        return False

    @staticmethod
    async def invalidate_by_email(email: str):
        ltok = await LoginToken.get_or_none(owner__email=email)
        if ltok != None:
            await ltok.delete()
            return True
        return False


class RefreshToken(BaseToken):
    @staticmethod
    async def issue(owner: User):
        rtok, fresh = await RefreshToken.get_or_create(owner=owner)
        if fresh:
            token = issue_refresh_token(str(rtok.id))
            rtok.token = token
            await rtok.save()
        return rtok

    @staticmethod
    async def invalidate_by_id(id: str):
        rtok = await RefreshToken.get_or_none(id=id)
        if rtok != None:
            await rtok.delete()
            return True
        return False

    @staticmethod
    async def invalidate_by_email(email: str):
        rtok = await RefreshToken.get_or_none(owner__email=email)
        if rtok != None:
            await rtok.delete()
            return True
        return False
