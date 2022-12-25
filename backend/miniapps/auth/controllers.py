from fastapi import APIRouter
from jwt.exceptions import ExpiredSignatureError
from miniapps.auth.models import *
from miniapps.users.models import *
from miniapps.auth.schemas import *
from toolbox.tokens import *
from toolbox.mailer import *


router = APIRouter()


@router.post('/login', response_model=LoginOut)
async def login(input: LoginIn):
    user, _ = await User.get_or_create(email=input.email)
    ltok = await LoginToken.issue(owner=user)
    send_magic_link(ltok.token)
    return LoginOut(success=True)


@router.post('/verify', response_model=VerifyOut)
async def verify(input: VerifyIn):
    user: User

    try:
        payload = decode_login_token(input.token)
        ltok = await LoginToken.get_or_none(id=payload['id'])
        if ltok is None: return VerifyOut(success=False);
        user = await ltok.owner
    except ExpiredSignatureError:
        payload = decode_login_token(input.token, verify_exp=False)
        await LoginToken.invalidate_by_id(id=payload['id'])
        return VerifyOut(success=False)
    except Exception as err:
        return VerifyOut(success=False)

    await LoginToken.invalidate_by_email(email=user.email)
    await RefreshToken.invalidate_by_email(email=user.email)

    atok = issue_access_token(user.id)
    rtok = await RefreshToken.issue(owner=user)
    return VerifyOut(
        success=True,
        access_token=atok,
        refresh_token=rtok.token,
    )


@router.post('/refresh', response_model=RefreshOut)
async def refresh(input: RefreshIn):
    user: User

    try:
        payload = decode_refresh_token(input.token)
        rtok = await RefreshToken.get_or_none(id=payload['id'])
        if rtok is None: return RefreshOut(success=False)
        user = await rtok.owner
    except ExpiredSignatureError:
        payload = decode_refresh_token(input.token, verify_exp=False)
        await RefreshToken.invalidate_by_id(id=payload['id'])
        return RefreshOut(success=False)
    except Exception:
        return RefreshOut(success=False)

    await RefreshToken.invalidate_by_email(email=user.email)
    atok = issue_access_token(user.id)
    rtok = await RefreshToken.issue(owner=user)
    return RefreshOut(
        success=True,
        access_token=atok,
        refresh_token=rtok.token,
    )
