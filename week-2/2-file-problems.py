import sys
import random
import re
import os


def cat(path):
    with open(path, 'r') as f:
        print(f.read())


def cat_multiple_files(paths):
    for path in paths:
        cat(path)


def generate_numbers(filename, n):
    NEW_LINE = '\n'
    RANGE_START = 1
    RANGE_END = 1000

    with open(filename, 'w') as w:
        to_write = ''
        for x in range(n):
            to_write += str(random.randint(RANGE_START, RANGE_END)) + ' '

        w.write(to_write + NEW_LINE)


def sum_numbers(filename):
    with open(filename, 'r') as f:
        numbers = [int(x) for x in re.split('\s|\n', f.read()) if x != '']
    return sum(numbers)


def du(f, parameters):
    h, s = False, False
    if len(parameters) != 0:
        if 'h' in parameters:
            h = True
        if 's' in parameters:
            s = True

        if h and s:
            # both params
            pass
        elif h and not s:
            # only -h
            pass
        elif s and not h:
            # only -s
            pass
    else:
        # no params
        # print(os.path.getsize(f))
        # print(os.stat(f).st_size)
        # todo : fuck du because it's broken
        pass


def wc(file_path, param):
    # Hope that file closes after this function
    if 'chars' in param:
        # Do magic to count characters
        return sum([len(x) for x in re.split(' ', re.sub('\n', ' ', open(file_path, 'r').read()))])
    if 'words' in param:
        # words

        pass
    if 'lines' in param:
        # lines
        return len(open(file_path, 'r').readlines())


def main():
    # cat_multiple_files(sys.argv)
    # generate_numbers(sys.argv[1], int(sys.argv[2]))
    # print(sum_numbers(sys.argv[1]))
    # du(sys.argv[1], [])
    print(wc(sys.argv[2], sys.argv[1]))


    pass

if __name__ == '__main__':
    main()
