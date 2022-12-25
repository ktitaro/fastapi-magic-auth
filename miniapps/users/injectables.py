from fastapi import Depends
from fastapi.exceptions import HTTPException
from miniapps.auth.injectables import *
from miniapps.users.models import *
from toolbox.tokens import *

async def get_current_user(auth: str = Depends(auth_scheme)):
    """
    Injectable that ensures that authorization token is provided,
    and that we have an existing user associated with this token.
    """
    try:
        payload = decode_access_token(auth.credentials)
        return await User.get(id=payload['id'])
    except Exception:
        raise HTTPException(status_code=403)
