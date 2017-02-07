from re import sub


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


def get_first_n_primes(n):
    primes = []
    i = 0
    while len(primes) < n:
        isprime = True
        for j in range(2, i):
            if i % j == 0:
                isprime = False
                break
        if isprime:
            primes.append(i)
        i += 1
    return primes


def run_length_encode(text):
    '''
    Doctest:
        >>> encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')
        '12W1B12W3B24W1B14W'
    '''
    return sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1),
               text)


def run_lenght_decode(text):
    '''
    Doctest:
        >>> decode('12W1B12W3B24W1B14W')
        'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
    '''
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)),
               text)
