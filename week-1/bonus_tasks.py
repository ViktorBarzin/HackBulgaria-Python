import re
from math import *


def are_anagrams(s1, s2):
    # works for current purpose, but I guess there are more efficient solutions
    return hash(str(sorted(s1.lower()))) == hash(str(sorted(s2.lower())))


def gas_stations(distance, tank_size, stations):
    res = [0]
    stations.append(distance)
    for i in range(len(stations) - 1):
        diff = stations[i + 1] - stations[i]
        size = tank_size - (stations[i] - res[-1])
        print(size)
        if size < diff:
            res.append(stations[i])
            size = tank_size
    return res[1:]


def reduce_file_path(path):
    print(path)
    splited = path.split('/')
    result = []
    for x in splited:
        if x != '.' and x != '' and x != '..':
            result.append(x)
        elif x == '..' and len(result) > 0:
            result.pop()

    if len(result) == 0:
        return '/'
    elif len(result) == 1 and re.match('[a-zA-Z]', result[0]):
        return '/' + result[0]
    return '/' + '/'.join(result)


def goldbach(number):
    # Check if given number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n) + 1.0)):
            if n % i == 0:
                return False
        return True

    # Find all primes up to input number
    primes_to_number = [x for x in range(2, number + 1) if is_prime(x)]
    results = []

    # Algorithm for finding Goldbach numbers
    for prime in primes_to_number:
        if is_prime(number - prime):
            results.append((prime, number - prime))

    # Format output so only unique values are returned
    if len(results) % 2 == 0:
        return sorted(results)[:len(results)//2:]
    return sorted(results)[:len(results)//2 + 1:]


def is_credit_card_valid(number):
    def extract_digits(n):
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        return digits

    reversed_number = list(reversed([int(x) for x in str(number)]))

    if len(reversed_number) % 2 == 0:
        return False

    doubles = [x * 2 for x in reversed_number[1::2]]
    evens = [x for x in reversed_number[::2]]
    reversed_number = [None] * (len(doubles) + len(evens))
    reversed_number[1::2] = doubles
    reversed_number[::2] = evens

    return (sum([sum(extract_digits(x)) for x in reversed_number])) % 10 == 0
