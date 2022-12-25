from settings.auth import *

def send_magic_link(token: str):
    callback_url = f'{LOGIN_CALLBACK_URL}?token={token}'
    message = f'Hi, there! Follow the link to login: {callback_url}'
    print(message)
