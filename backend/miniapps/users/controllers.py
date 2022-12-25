from typing import List
from fastapi import APIRouter
from miniapps.users.models import *
from miniapps.users.schemas import *


router = APIRouter()


@router.get('', response_model=List[UserOut])
async def fetch_users():
    return await UserOut.from_queryset(User.all())


@router.get('/{id}', response_model=UserOut)
async def fetch_user(id: int):
    return await UserOut.from_queryset_single(User.get(id=id))


@router.put('/{id}', response_model=UserOut)
async def update_user(id: int, attrs: UserIn):
    await User.filter(id=id).update(**attrs.dict(exclude_unset=True))
    return await UserOut.from_queryset_single(User.get(id=id))


@router.delete('/{id}')
async def delete_user(id: int):
    await User.filter(id=id).delete()
    return 'OK'
