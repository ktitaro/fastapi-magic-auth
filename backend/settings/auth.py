import os

# Secret used to cryptographically sign tokens
LOGIN_TOKEN_SECRET = os.getenv('LOGIN_TOKEN_SECRET', 'login-token-secret')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET', 'access-token-secret')
REFRESH_TOKEN_SECRET = os.getenv('REFRESH_TOKEN_SECRET', 'refresh-token-secret')

# For how long the token is considered to be valid
# after its creation, numberical measured in seconds
LOGIN_TOKEN_LIFESPAN = int(os.getenv('LOGIN_TOKEN_LIFESPAN', 5 * 60))
ACCESS_TOKEN_LIFESPAN = int(os.getenv('ACCESS_TOKEN_LIFESPAN', 60 * 60))
REFRESH_TOKEN_LIFESPAN = int(os.getenv('REFRESH_TOKEN_LIFESPAN', 7 * 24 * 60 * 60))

# The link where we'd like to redirect the user, we'll include it in the email
LOGIN_CALLBACK_URL = os.getenv('LOGIN_CALLBACK_URL', 'http://localhost:3000/auth/verify')
