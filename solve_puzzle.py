import queue


def find_index(puzzle, item):
    row = -1
    column = -1

    for z in puzzle:
        try:
            column = list(z).index(item)
            row = puzzle.index(z)
        except ValueError:
            pass

    return row, column


def solve_puzzle(puzzle):
    print(puzzle)

    p = list(puzzle).copy()

    if check_answer(p):
        print("Solved!")
        return p

    possible_ways = queue.Queue()
    parent = ""

    while not check_answer(p):
        p = solve(p, possible_ways, parent)


def check_answer(puzzle):
    answer = [
        ["",  1,  2,  3],
        [4,  5,   6,  7],
        [8,  9, 10,  11],
        [12, 13, 14, 15]
    ]

    if puzzle == answer:
        return True
    else:
        return False


def get_available_ways(puzzle):
    hole_row, hole_column = find_index(puzzle, "")

    if hole_column == 0 and hole_row == 0:
        return ['R', 'D']
    elif hole_column == 3 and hole_row == 0:
        return ['L', 'D']
    elif hole_column == 0 and hole_row == 3:
        return ['R', 'U']
    elif hole_column == 3 and hole_row == 3:
        return ['L', 'U']

    elif hole_row == 0:
        return ['R', 'L', 'D']
    elif hole_row == 3:
        return ['R', 'L', 'U']
    elif hole_column == 0:
        return ['R', 'U', 'D']
    elif hole_column == 3:
        return ['L', 'U', 'D']

    else:
        return ['R', 'L', 'U', 'D']


def move(puzzle, select, row, col):
    if select == 'R':
        r2 = row
        c2 = col + 1

        temp = puzzle[row][col]
        puzzle[row][col] = puzzle[r2][c2]
        puzzle[r2][c2] = temp

    elif select == 'L':
        r2 = row
        c2 = col - 1

        temp = puzzle[row][col]
        puzzle[row][col] = puzzle[r2][c2]
        puzzle[r2][c2] = temp

    elif select == 'U':
        r2 = row - 1
        c2 = col

        temp = puzzle[row][col]
        puzzle[row][col] = puzzle[r2][c2]
        puzzle[r2][c2] = temp

    elif select == 'D':
        r2 = row + 1
        c2 = col

        temp = puzzle[row][col]
        puzzle[row][col] = puzzle[r2][c2]
        puzzle[r2][c2] = temp

    return puzzle


def solve(p, possible_ways, parent):

    for w in get_available_ways(p):
        possible_ways.put(parent + w)

    select = possible_ways.get()

    print("Select: ", select)

    row, column = find_index(p, "")

    p = move(p, select, row, column)

    print("P: ", p)

    return p
