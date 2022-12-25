from settings.auth import *

def send_magic_link(token: str):
    """
    This function meant to send an email with auth link.
    I won't implement the actual email sending logic here,
    since its ok for me to check console prompt for getting
    token in this proof of concept project. 
    """
    callback_url = f'{LOGIN_CALLBACK_URL}?token={token}'
    message = f'Hi, there! Follow the link to login: {callback_url}'
    print(message)
