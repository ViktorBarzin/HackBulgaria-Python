from math import *
import re
# Link to problems -> https://github.com/HackBulgaria/Programming101-Python-2016/tree/master/week01/2-Dive-Into-Python


def count_substrings(haystack, needle):
    return len(re.findall(needle, haystack))


def sum_matrix(matrix):
    return sum([sum(x) for x in matrix])


def nan_expand(n):
    if n != 0:
        return ''.join(['Not a ' for x in range(n) if x != 0]) + 'NaN'
    else:
        return ''


def is_prime(n):
    for i in range(2, int(sqrt(n) + 1.0)):
        if n % i == 0:
            return False
    return True


def prime_factorization(n):
    primes_to_n = [x for x in range(2, n) if is_prime(x)]
    prime_delimiters = {}

    i = 0
    while not is_prime(n) and n >= 0:
        j = i
        while n % primes_to_n[j] == 0:
            if primes_to_n[j] not in prime_delimiters:
                prime_delimiters[primes_to_n[j]] = 1
            elif primes_to_n[j] in prime_delimiters:
                prime_delimiters[primes_to_n[j]] += 1

            n /= int(primes_to_n[j])
        i += 1

    if n in primes_to_n:
        prime_delimiters[n] = 1
    return sorted([(int(key), int(value)) for key, value in prime_delimiters.items()])


def group(items):
    groups = []
    j = 0
    groups.append([items[0]])
    for i in range(1, len(items)):
        if items[i] == items[i - 1]:
            groups[j].append(items[i])
        else:
            groups.append([items[i]])
            j += 1
    return groups


#print(count_substrings("This is a test string", "is"))
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(sum_matrix(m))
# print(nan_expand(0))
# print(prime_factorization(356))
print(group([1, 1, 1, 2, 3, 1, 1]))