import jwt
from time import *
from datetime import *

secret = 'hello-world'
expires = datetime.now(tz=timezone.utc) + timedelta(seconds=5)
payload = { 'id': 1, 'exp': expires }

token = jwt.encode(payload, secret, algorithm='HS256')

sleep(3)

try:
    payload = jwt.decode(token, secret, algorithms=['HS256'])
    print('The token is perfectly valid!')
    print('Now lets remove it from the db.')
    print('Here is the data you might need to do that:', payload)
except jwt.exceptions.ExpiredSignatureError:
    print('Token is expired, lets remove it from the db.')
    payload = jwt.decode(token, secret, algorithms=['HS256'], options={'verify_exp': False})
    print('Here is the data you might need to do that:', payload)
except Exception as err:
    print('Token in not valid for some unexpected reason.')
    print('Just chill, you do not need to do anything.')
