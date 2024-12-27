from common import _parse_puzzle, _execute


def _solve(puzzle):
    program, register = _parse_puzzle(puzzle)
    _, output = _execute(program, register)
    return ",".join(str(i) for i in output)


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        print(_solve(f))
