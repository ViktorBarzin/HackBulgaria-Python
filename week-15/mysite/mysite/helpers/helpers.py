def fact(number):
    number = int(number)
    prod = 1
    for i in range(1, number + 1):
        prod *= i
    return prod


def fib(number):
    number = int(number)
    a = 0
    b = 0
    c = 1
    for i in range(number - 1):
        a = c
        c = a + b
        b = a
    return c

