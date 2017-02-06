'''
Solveable position:
     neighbour frogs which are not looking the same direction
    if moving causes an invalid position - dont move
negithbours of same type -> move first
'''
from collections import deque


class Frog:
    def __init__(self, value, parent=None, children=[]):
        self.value = value
        self.parent = parent
        self.children = children


class Lake:
    def __init__(self, root):
        self.root = Frog(root)

    def find_solution(self):
        stack = self.generate_possible_moves(self.root.value)
        current_height, max_height = 0, 0
        current_sol, best_sol = [], []
        while stack:
            # print(current_sol)
            current = stack.pop()
            current_sol.append(current.value)
            current_height += 1

            current.children = self.generate_possible_moves(current.value)
            for child in current.children:
                stack.append(child)

            if not current.children:
                if current_height > max_height:
                    max_height = current_height
                    best_sol = current_sol
                current_sol.pop()
                current_height -= 1
        return best_sol[::]

    @staticmethod
    def generate_possible_moves(position):
        # >>_><<<
        moves = []
        for i in range(len(position)):
            if position[i] == '>':
                if i + 1 < len(position) and position[i + 1] == '_':
                    new_move = list(position)
                    new_move[i] = '_'
                    new_move[i + 1] = '>'
                    moves.append(''.join(new_move))
                if i + 2 < len(position) and position[i + 2] == '_':
                    new_move = list(position)
                    new_move[i] = '_'
                    new_move[i + 2] = '>'
                    moves.append(''.join(new_move))
            elif position[i] == '<':
                if i - 1 >= 0 and position[i - 1] == '_':
                    new_move = list(position)
                    new_move[i] = '_'
                    new_move[i - 1] = '<'
                    moves.append(''.join(new_move))
                if i - 2 >= 0 and position[i - 2] == '_':
                    new_move = list(position)
                    new_move[i] = '_'
                    new_move[i - 2] = '<'
                    moves.append(''.join(new_move))
        return deque(Frog(x) for x in moves)

def main():
    l = Lake('>>>_<<<')
    print(l.find_solution())
    # print(l.generate_possible_moves('>>_<<'))
if __name__ == '__main__':
    main()