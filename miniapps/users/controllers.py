from typing import List
from fastapi import APIRouter, Depends
from miniapps.auth.models import *
from miniapps.users.models import *
from miniapps.users.schemas import *
from miniapps.users.injectables import *

router = APIRouter()

@router.get('/me', response_model=UserOut)
async def fetch_current_user(current_user: User = Depends(get_current_user)):
    return await UserOut.from_tortoise_orm(current_user)

@router.put('/me', response_model=UserOut)
async def update_current_user(attrs: UserIn, current_user: User = Depends(get_current_user)):
    await current_user.update_from_dict(attrs.dict(exclude_unset=True)).save()
    return await UserOut.from_tortoise_orm(current_user)

@router.delete('/me', response_model=DeleteOut)
async def delete_current_user(current_user: User = Depends(get_current_user)):
    await RefreshToken.invalidate_by_email(current_user.email)
    await current_user.delete()
    return DeleteOut(success=True)

@router.get('', response_model=List[UserOut])
async def fetch_users():
    return await UserOut.from_queryset(User.all())

@router.get('/{id}', response_model=UserOut)
async def fetch_user(id: int):
    return await UserOut.from_queryset_single(User.get(id=id))
