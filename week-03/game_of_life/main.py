import os
import re

white_square = '■'
black_square = '□'


def get_initial_alive_cells_positions(initial_alive_cells):
    initial_alive_cells_positions = []
    for x in range(initial_alive_cells):
        initial_alive_cells_positions.append([int(x) for x in input('Cell ' + str(x) + ' position :').split(' ')])
    return initial_alive_cells_positions


def paint_cell(m, x, y, color):
    m[x][y] = color
    return m


def paint_matrix(m1, color):
    for row in range(len(m1[0])):
        for col in range(row):
            m1 = paint_cell(m1, row, col, color)
    return m1


def matrix_to_string(matrix, matrix_size):
    matrix_to_str = ''
    for row in range(matrix_size):
        c_list = []
        for col in range(matrix_size):
            c_list.append(black_square)
            matrix_to_str += matrix[row][col]
        matrix_to_str += '\n'
        list_of_lists.append(c_list)
    return matrix_to_str


def initiate_matrix(matrix_size, color):
    matrix = []
    for row in range(matrix_size):
        c_list = []
        matrix.append(c_list)
        for col in range(matrix_size):
            c_list.append(black_square)
            print(row,col)
            matrix[row][col] = color
        matrix.append(c_list)
        list_of_lists.append(c_list)
    return matrix
# Read input
# alive_cells = int(input('Enter initial alive cells:'))
# initial_alive_cells_positions = get_initial_alive_cells_positions(alive_cells)

initial_alive_cells_positions = [(2, 3), (4, 5), (20, 4)]
m_size = max([max(x, y) for x, y in initial_alive_cells_positions])

list_of_lists = []
print(matrix_to_string(initiate_matrix(m_size, black_square)))

