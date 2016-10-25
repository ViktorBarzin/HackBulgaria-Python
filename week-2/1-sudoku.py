
def sudoku_solved(sudoku, characters = range(1, 10)):
    def check_for_repeating(sudoku):
        for row in sudoku:
            if len(row) != len(set(row)):
                return False

    def rotate(sudoku):
        cols = []

        for row in range(len(sudoku)):
            col = []

            for x in range(len(sudoku)):
                col.append(sudoku[x][row])
            cols.append(col)
        return cols

    def get_sub_matrix(matrix, size):
        sub_matrix = []

        for row in range(size):
            c_row = []
            for col in range(size):
                c_row.append(matrix[row, col])
            sub_matrix.append(c_row)
    # print(get_sub_matrix(sudoku))

# todo : finish logic and implementation
print(sudoku_solved([
[4, 5, 2, 3, 8, 9, 7, 1, 6],
[3, 8, 7, 4, 6, 1, 2, 9, 5],
[6, 1, 9, 2, 5, 7, 3, 4, 8],
[9, 3, 5, 1, 2, 6, 8, 7, 4],
[7, 6, 4, 9, 3, 8, 5, 2, 1],
[1, 2, 8, 5, 7, 4, 6, 3, 9],
[5, 7, 1, 8, 9, 2, 4, 6, 3],
[8, 9, 6, 7, 4, 3, 1, 5, 2],
[2, 4, 3, 6, 1, 5, 9, 8, 7]
]))

