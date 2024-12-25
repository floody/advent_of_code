from common import _parse_puzzle, _calculate_gps_coordinates


def _move(
    direction: tuple[int, int], matrix: list[list[int]], need_to_move: tuple[int, int]
) -> tuple[int, int]:
    ni, nj = need_to_move[0] + direction[0], need_to_move[1] + direction[1]

    if matrix[ni][nj] == 1:
        _move(direction, matrix, (ni, nj))
    if matrix[ni][nj] == -1:
        return 0, 0
    if matrix[ni][nj] == 0:
        matrix[ni][nj], matrix[need_to_move[0]][need_to_move[1]] = (
            matrix[need_to_move[0]][need_to_move[1]],
            matrix[ni][nj],
        )
        return direction

    return 0, 0


def _read_matrix(line: str, m: list[list[int]]) -> tuple[int, int] | None:
    row = []
    robot = None
    for l in line:
        match l:
            case "#":
                row.append(-1)
            case ".":
                row.append(0)
            case "O":
                row.append(1)
            case "@":
                robot = len(m), len(row)
                row.append(2)

    m.append(row)
    return robot


# pylint: disable=R0801
def _solve(puzzle) -> int:
    matrix, directions, robot = _parse_puzzle(puzzle, _read_matrix)

    for direction in directions:
        n = _move(direction, matrix, robot)
        robot = (robot[0] + n[0], robot[1] + n[1])
    return _calculate_gps_coordinates(matrix)


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        print(_solve(f))
