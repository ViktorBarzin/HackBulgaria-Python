from datetime import datetime


def accepts(*args):
    def accepter(func):
        def check_type(*func_args, **func_kwargs):
            for i in range(len(args)):
                if type(func_args[i]).__name__ != args[i].__name__:
                    raise TypeErro?!?jedi=1, r('Argument {0} o?!? (*args, **kwargs) ?!?jedi?!?'f {1} is not {2}'
                            .format(i, func.__name__, args[i].__name__))
            return func(*func_args, **func_kwargs)
        return check_type
    return accepter

def encrypt(key):
    def get_func(func):
        def encryption_process(string_to_encrypt):
            result = ''
            small_letters = [chr(x) for x in range(97, 123)]
            capital_letters = [chr(x) for x in range(65, 91)]

            for s in string_to_encrypt:
                if s in small_letters:
                    # encrypt as small letter
                    result += small_letters[(small_letters.index(s) + key)
                            % len(small_letters)]
                elif s in capital_letters:
                    # encrypt as capital
                    result  += capital_letters[(capital_letters.index(s) + key)
                        % len(small_letters)]
            return func(result)
        return encryption_process
    return get_func

def log(file_name):
    def get_func(func, *args, **kwargs):
        def log_process(*args): # Why the *args?
            with open(file_name, 'a') as w:
                w.write('{0} was called at {1}\n'.format(func.__name__, datetime.now()))
            return func(*args, **kwargs)
        return log_process
    return get_func

def performance(file_name):
    def get_func(func, *args, **kwargs):
        def performance_logging(*args, **kwargs):
            with open(file_name, 'a') as w:
                before_method_time = datetime.now()
                result =  func(*args, **kwargs)
                after_method_time = datetime.now()
                w.write('{} took {} seconds to execute\n'.format(
               func.__name__ ,(after_method_time - before_method_time).total_seconds()))
            return result 
        return performance_logging
    return get_func

