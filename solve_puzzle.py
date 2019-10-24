def solve_puzzle(puzzle):
    print(puzzle)

    p = list(puzzle).copy()

    if check_answer(p):
        print("Solved!")
        return p


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
