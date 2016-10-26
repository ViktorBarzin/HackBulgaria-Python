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
        # ATTENTION!The solution below is really messed up so it is commented as legacy due to newer and better solution
        # ----------------------------------------------
        # Do magic to count characters
        # and add the magic one which fixes a bug with original wc implementation
        # return sum([len(x) for x in re.split(' ', re.sub('\n', ' ', open(file_path, 'r').read()))]) + int(open(file_path, 'r').read().count(' ')) + 1
        # ---------------------------------------------

        return len(re.sub('\n', ' ', open(file_path, 'r').read()))
    if 'words' in param:
        # words
        return len([x for x in re.split('\s+', open(file_path, 'r').read()) if x != ''])
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
