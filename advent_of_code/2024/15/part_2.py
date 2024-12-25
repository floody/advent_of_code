from common import _parse_puzzle, _calculate_gps_coordinates


def _move(
    direction: tuple[int, int],
    matrix: list[list[int]],
    need_to_move: set[tuple[int, int]],
) -> tuple[int, int]:
    if direction in ((0, -1), (0, 1)):
        for i, j in need_to_move:
            v = j + direction[1]
            if matrix[i][v] == 2:
                _move(direction, matrix, {(i, v)})
            if matrix[i][v] == 1:
                _move(direction, matrix, {(i, v)})

    if direction in ((1, 0), (-1, 0)):
        n: set[tuple[int, int]] = set()
        for i, j in need_to_move:
            u = i + direction[0]
            if matrix[u][j] == -1:
                n = set()
                break
            if matrix[u][j] == 1:
                n.add((u, j))
                n.add((u, j + 1))
            if matrix[u][j] == 2:
                n.add((u, j - 1))
                n.add((u, j))
        if n:
            _move(direction, matrix, n)

    if all(matrix[i + direction[0]][j + direction[1]] == 0 for i, j in need_to_move):
        for i, j in need_to_move:
            u, v = i + direction[0], j + direction[1]
            matrix[u][v], matrix[i][j] = matrix[i][j], matrix[u][v]
        return direction

    return 0, 0


def _read_matrix(line: str, matrix: list[list[int]]) -> tuple[int, int] | None:
    m = []
    robot = None
    for l in line:
        match l:
            case "#":
                m.append(-1)
                m.append(-1)
            case ".":
                m.append(0)
                m.append(0)
            case "O":
                m.append(1)
                m.append(2)
            case "@":
                robot = len(matrix), len(m)
                m.append(3)
                m.append(0)

    matrix.append(m)
    return robot


# pylint: disable=R0801
def _solve(puzzle) -> int:
    matrix, directions, robot = _parse_puzzle(puzzle, _read_matrix)

    for direction in directions:
        n = _move(direction, matrix, {robot})
        robot = (robot[0] + n[0], robot[1] + n[1])

    return _calculate_gps_coordinates(matrix)


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        print(_solve(f))
