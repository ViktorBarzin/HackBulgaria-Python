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


def max_consecutive(numbers):
    max_counter = 0
    current_counter = 1

    for i in range(len(numbers) - 1):
        # print(current_counter)
        if numbers[i] == numbers[i+1]:
            current_counter += 1
        else:
            current_counter = 1
        if current_counter > max_counter:
            max_counter = current_counter
    return max_counter


def word(word_to_find, table_size, table):
    counter = 0
    rows, cols = [int(x) for x in table_size.split(' ')]
    if len(word_to_find) > rows or len(word_to_find) > cols:
        return 'Invalid number of rows or columns!'

    '''
    (x - 1, y - 1) (x, y - 1) (x + 1, y - 1)
    (x - 1, y)     (x, y)     (x + 1, y)
    (x - 1, y + 1) (x, y + 1) (x + 1, y + 1)
    '''
    for row in table:
        for col in row:
            pass
    return counter
