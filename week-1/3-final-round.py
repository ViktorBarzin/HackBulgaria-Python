import re

def is_number_balanced(n):
    n = str(n)
    if len(n) % 2 == 1:
        return False
    left = n[:(int(len(n) / 2)):]
    right = n[int(len(n) / 2)::]

    left_sum = sum([int(x) for x in left])
    right_sum = sum([int(x) for x in right])
    return left_sum == right_sum


def increasing_or_decreasing(seq):
    is_up = True
    is_down = True
    for index in range(len(seq) - 1):
        if seq[index] < seq[index + 1]:
            is_down = False
        if seq[index] > seq[index + 1]:
            is_up = False

    if is_up:
        return 'Up!'
    elif is_down:
        return 'Down!'
    return False


def get_largest_palindrome(n):
    def is_palindrome(obj):
        obj = str(obj)
        return obj == obj[::-1]

    for x in range(n-1, 0, -1):
        if is_palindrome(x):
            return x


def sum_of_numbers(str):
    return sum([int(x) for x in re.findall('[\d]+', str)])


def birthday_ranges(birthdays, ranges):
    counter_dict = {range: 0 for range in ranges}
    for bday in birthdays:
        for range in ranges:
            if range[1] >= bday >= range[0]:
                counter_dict[range] += 1
    return [counter_dict[x] for x in ranges]



