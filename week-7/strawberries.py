# Task can be found here: https://github.com/HackBulgaria/Programming101-Python-2016/blob/master/week07/Strawberries/task_strawberries.pdf


def strawberries(rows, cols, days, dead_strawberries):
    field = [[True for x in range(cols)] for y in range(rows)]

    for day in range(days):
        dead_strawberries += kill_neighbours(field, dead_strawberries)

    print(count_alive(field))


def kill_neighbours(field, dead_strawberries):
    new_dead = []
    count = 0
    for s in dead_strawberries:
        count += 1
        # Up
        up = (s[0] - 1, s[1])
        if in_field(field, up):
            field[up[0]][up[1]] = False
            new_dead.append(up)
        # Down
        down = (s[0] + 1, s[1])
        if in_field(field, down):
            new_dead.append(down)
            field[down[0]][down[1]] = False
        # Left
        left = (s[0], s[1] - 1)
        if in_field(field, left):
            field[left[0]][left[1]] = False
            new_dead.append(left)
        # Right
        right = (s[0], s[1] + 1)
        if in_field(field, right):
            field[right[0]][right[1]] = False
            new_dead.append(right)
        # print(new_dead)
    print(count)
    return new_dead


def in_field(field, coords):
    return 0 <= coords[0] < len(field)\
            and 0 <= coords[1] < len(field[0])


def count_alive(field):
    alive = 0
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col]:
                alive += 1
    return alive


def main():
    pass
    # strawberries(8,10,2,[(4,8), (2,7)])
    # strawberries(80, 1000, 10, [(4,8), (2,7)])
    # strawberries(400, 803, 99, [(399, 200), (196, 202)])

if __name__ == '__main__':
    main()
