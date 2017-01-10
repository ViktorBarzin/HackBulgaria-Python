import re
import hashlib


def check_password_requirments(func):
    def accepter(*args, **kwargs):  # Taking username because all the funs do..
        password = kwargs['password']
        username = kwargs['username']

        if len(password) < 8:
            raise ValueError('Password is too short')
        if re.match('\b', password) is None and re.match('[A-Z]', password) is not None and re.match('[^a-zA-Z0-9]') is not None:
            raise ValueError('Password must contain a digit, an upper case and lower case letter and a special symbol')
        if username.lower() in password.lower():
            raise ValueError('The password cannot contain the username')
        return func(*args, **kwargs)
    return accepter


def check_username_requirements(func):
    def accepter(*args, **kwargs):
        username = kwargs['username']
        if username == '' or username == ' ':
            raise ValueError('Username cannot be empty!')
        # Do some more username varification

        return func(*args, **kwargs)


def hash_password(func):
    def accepter(password):
        _hash = hashlib.sha512(bytes(password.encode('utf-8')))
        password = _hash.hexdigest()
        return func(password)
    return accepter

