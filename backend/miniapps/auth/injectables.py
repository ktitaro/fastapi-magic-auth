from fastapi import Depends
from fastapi.security import HTTPBearer
from fastapi.exceptions import HTTPException
from miniapps.users.models import *
from toolbox.tokens import *


# Middleware that ensures that the
# "Authorization" header is provided,
# and its a valid Bearer token.
auth_scheme = HTTPBearer()


async def ensure_auth(auth: str = Depends(auth_scheme)):
    """
    Middleware that ensures that authorization token is provided,
    and that we have an existing user associated with this token.
    """
    try:
        payload = decode_access_token(auth.credentials)
        return await User.get(id=payload['id'])
    except Exception:
        raise HTTPException(status_code=403)
