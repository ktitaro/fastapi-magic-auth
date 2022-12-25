from pydantic import BaseModel
from miniapps.users.models import User
from tortoise.contrib.pydantic import pydantic_model_creator

UserIn = pydantic_model_creator(User, name='UserIn', exclude_readonly=True, optional=('*'))
UserOut = pydantic_model_creator(User, name='UserOut', exclude_readonly=False)

class DeleteOut(BaseModel):
    success: bool
