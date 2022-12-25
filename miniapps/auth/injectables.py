from fastapi.security import HTTPBearer

# Injectable that ensures that the
# "Authorization" header is provided,
# and its a valid Bearer token.
auth_scheme = HTTPBearer()
