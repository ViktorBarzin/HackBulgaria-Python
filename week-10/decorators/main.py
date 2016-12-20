from decorators import *
from time import sleep

@accepts(str)
def say_hello(name):
    return 'Hello, I am {}'.format(name)

@accepts(str, int)
def deposit(name, age):
    return '{0} sends {1}'.format(name, age)

@performance("performance.txt")
@log('log.txt')
@encrypt(0)
def get_low(string):
    return string

def main():
    # print(say_hello('gosho'))
    print(deposit('gosho', 20))
    print(get_low('gosho'))


if __name__ == '__main__':
    main()

