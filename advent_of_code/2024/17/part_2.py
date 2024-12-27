from common import _parse_puzzle, _execute


def _solve(puzzle):
    program, _ = _parse_puzzle(puzzle)

    a = 0
    for i in reversed(range(len(program))):
        a <<= 3
        while _execute(program, {"A": a, "B": 0, "C": 0})[1] != program[i:]:
            a += 1
    return a


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        print(_solve(f))
