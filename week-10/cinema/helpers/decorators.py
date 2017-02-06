import datetime
import os
import hashlib


def log(log_file_path, string_to_log):
    def accepter(func):
        def write_to_log(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                with open(log_file_path, 'a') as w:
                    w.write('{} Current time: {}{}'.format(string_to_log, str(datetime.datetime.now()), '\n'))
            except IOError as e:
                print(e)
            return result
        return write_to_log
    return accepter


def hash_password(func):
    def __hash_password(self, username, password):  # Takes username, because register and login do as well
        # TODO: fix those ugly arguments ;/
        # Hash password
        hash_obj = hashlib.sha512(bytes(password, 'utf-8'))
        password = hash_obj.hexdigest()
        return func(self, username, str(password))
    return __hash_password


# Clear console for better UX
def clear_screen(func):
    def clear(*args, **kwargs):
        os.system('clear')
        return func(*args, **kwargs)
    return clear
