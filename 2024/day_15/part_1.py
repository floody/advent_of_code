from common import _parse_puzzle, _calculate_gps_coordinates


def _move(
    coordinate: tuple[int, int], direction: tuple[int, int], m: list[list[int]]
) -> tuple[int, int]:
    ni, nj = coordinate[0] + direction[0], coordinate[1] + direction[1]

    if m[ni][nj] == 1:
        _move((ni, nj), direction, m)
    if m[ni][nj] == -1:
        return 0, 0
    if m[ni][nj] == 0:
        m[ni][nj], m[coordinate[0]][coordinate[1]] = (
            m[coordinate[0]][coordinate[1]],
            m[ni][nj],
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


def _solve(
    matrix: list[list[int]], directions: list[tuple[int, int]], robot: tuple[int, int]
) -> int:
    for direction in directions:
        n = _move(robot, direction, matrix)
        robot = (robot[0] + n[0], robot[1] + n[1])

    return _calculate_gps_coordinates(matrix)


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        matrix, directions, robot = _parse_puzzle(f, _read_matrix)
        print(_solve(matrix, directions, robot))
