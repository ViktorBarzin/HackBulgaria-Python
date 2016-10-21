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
    pass


def is_palindrome(obj):
    obj = str(obj)
    return obj == obj[::-1]
