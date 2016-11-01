def sum_of_digit(n):
    n = str(n)
    if n[0] == '-':
        n = n[1:]
    sum_of_digits = 0
    for i in n:
        sum_of_digits += int(i)
    return sum_of_digits

def to_digits(n):
    digits = []
    while n > 0:
        digit_to_add = n % 10
        n /= 10
        digits.append(digit_to_add)
    digits = digits[::-1]
    return digits


def to_number(digits):
    digits = digits[::-1]
    final_number = 0
    for i in range(len(digits)):
        final_number += int(digits[i]) * 10**i
    return final_number


def count_vowels(string):
    vowels = 'aeiouy'
    counter = 0
    for x in string:
        if x in vowels:
            counter += 1
    return counter

def count_consonants(string):
    vowels = 'aeiouy'
    counter = 0
    for x in string:
        if x not in vowels and x.isalpha():
            counter += 1
    return counter

def is_prime_number(number):
    for x in range(2, number):
        if number % x == 0:
            return False
    return True

def fact_digits(number):
    digits = to_digits(number)
    sum_of_facts  = 0
    for digit in digits:
        fact = 1
        for numb in range(1,int(digit) + 1):
            fact *= numb
        sum_of_facts += fact
    return sum_of_facts

def fibonacci(number):
    a = 0
    b = 1
    c = a + b
    numbers = [1]
    for i in range(number):
        numbers.append(c)
        a = b
        b = c
        c = a + b
    return numbers

def fib_number(n):
    fibonaccis = fibonacci(n)
    concat = ''
    for dig in fibonaccis:
        concat += str(dig)
    return concat

def is_palindrome(obj):
    obj = str(obj)
    return obj == obj[::-1]

def char_histogram(string):
    string = str(string)
    hist = {}
    for char in string:
        if char not in hist:
            hist[char] = 1
        else:
            hist[char] += 1
    return hist

print(sum_of_digit(1325132435356))
print(to_digits(123))
print(to_number(['1','2','3']))
print(count_vowels('Github is the second best thing that happend to programmers, after the keyboard!'))
print(count_consonants('Github is the second best thing that happend to programmers, after the keyboard!'))
print(is_prime_number(98))
print(fact_digits(145))
print(fibonacci(10))
print(fib_number(10))
print(is_palindrome(121))
print()(char_histogram('aabbbccccd'))

