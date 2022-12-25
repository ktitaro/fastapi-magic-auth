import jwt
from datetime import *
from settings.auth import *

def issue_token(id: int, secret: str, lifespan: int):
    """ Helper function that keeps some constants inplace """
    exp = datetime.now(tz=timezone.utc) + timedelta(seconds=lifespan)
    return jwt.encode({ 'id': id, 'exp': exp }, secret, algorithm='HS256')

def decode_token(token: str, secret: str, **options):
    """ Helper function that keeps some constants inplace """
    return jwt.decode(token, secret, algorithms=['HS256'], options=options)

def issue_login_token(id: int):
    """ Don't use it directly, use LoginToken.issue insted """
    return issue_token(id, LOGIN_TOKEN_SECRET, LOGIN_TOKEN_LIFESPAN)

def issue_access_token(id: int):
    """
    You should use it directly, since access token
    does not need to be stored in the database
    """
    return issue_token(id, ACCESS_TOKEN_SECRET, ACCESS_TOKEN_LIFESPAN)

def issue_refresh_token(id: int):
    """ Don't use it directly, use RefreshToken.issue insted """
    return issue_token(id, REFRESH_TOKEN_SECRET, REFRESH_TOKEN_LIFESPAN)

def decode_login_token(token: str, **options):
    return decode_token(token, LOGIN_TOKEN_SECRET, **options)

def decode_access_token(token: str, **options):
    return decode_token(token, ACCESS_TOKEN_SECRET, **options)

def decode_refresh_token(token: str, **options):
    return decode_token(token, REFRESH_TOKEN_SECRET, **options)
