import re
import json
import hashlib
import datetime
from settings import WRONG_PASSWORD_ATTEPMTS, BAN_TIME, BAN_LIST_FILE
import sql_manager as sql_man


def check_password_requirements(func):
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
    return accepter


def hash_password(func):
    def accepter(*args, **kwargs):
        password = kwargs['password']
        _hash = hashlib.sha512(bytes(password.encode('utf-8')))
        kwargs['password'] = _hash.hexdigest()
        return func(*args, **kwargs)
    return accepter


def check_if_banned(file_to_check_in):
    def check_if_banned(func):
        def accepter(*args, **kwargs):
            with open(file_to_check_in, 'r') as r:
                username = kwargs['username']
                try:
                    data = json.load(r)
                except json.decoder.JSONDecodeError:
                    raise ValueError('Empty or invalid ban-list file')
            if username not in [x['username'] for x in data]:
                # User is not in the ban list therefore allow him to log in
                return func(*args, **kwargs)

            # Check if user has exceeded than max allowed attempts and check if
            # he is still banned
            user = [x for x in data if x['username'] == username][0]
            current_time = datetime.datetime.now()
            user_ban_start_time = datetime.datetime.strptime(user['ban-start-date'], '%Y-%m-%d %H:%M:%S')
            print(user['wrong-attempts'])
            if user['wrong-attempts'] >= WRONG_PASSWORD_ATTEPMTS:
                # print(user_ban_start_time + datetime.timedelta(seconds=BAN_TIME))
                if (user_ban_start_time + datetime.timedelta(seconds=BAN_TIME)) > current_time:
                    # Do some calculation to show remaining time of ban
                    time_left_from_ban = (user_ban_start_time + datetime.timedelta(seconds=BAN_TIME)) - current_time
                    print('You have entered an invalid password too many times!\nYou must wait {} seconds until trying in again'.format(time_left_from_ban))
                    return False

                # Have to reset failed attempts
                # Bad practice but oh well
                db = sql_man.Db_Manager()
                db.clear_login_ban_records(user['username'])
                # Should be ok to login cuz his ban has timed out
                return func(*args, **kwargs)
            # User is allowed to log in
            return func(*args, **kwargs)
        return accepter
    return check_if_banned


def check_ban_list_file(func):
    def fix_ban_file(*args, **kwargs):
        # File is empty and can't read anything
        with open(BAN_LIST_FILE, 'r+') as r:
            if len(r.read().strip()) == 0:
                # Solution is to add "[]"
                r.write('[]')
        return func(*args, **kwargs)
    return fix_ban_file


def check_email_requirements(func):
    def accepter(*args, **kwargs):
        email = kwargs['email']
        if re.match('.*\w+@\w+.\w+.*', email):
            return func(*args, **kwargs)
        raise ValueError('Invalid email address!')
    return accepter
