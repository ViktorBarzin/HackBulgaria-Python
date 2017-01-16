import os


def chain(iter_one, iter_two):
    for i in iter_one:
        yield i
    for i in iter_two:
        yield i


def compress(iter_one, mask):
    for i in range(len(iter_one)):
        if mask[i]:
            yield iter_one[i]


def cycle(iter_one):
    result = ''
    while True:
        for el in iter_one:
            result += str(el)
            yield result


def book_reader(book_files):
    for book_file in book_files:
        with open('books/' + book_file, 'r') as r:
            result = ''
            while True:
                line = r.readline()
                if line == '':
                    # eof
                    break
                result += line
                next_line = r.readline()
                while '#' not in next_line and next_line:
                    result += next_line
                    next_line = r.readline()
                    if '#' in next_line:
                        yield result
                        result = next_line

                yield result


for chapter in book_reader(sorted(os.listdir('books'))):
    if input() == ' ':
        os.system('clear')
        print('here')
        print(chapter)
