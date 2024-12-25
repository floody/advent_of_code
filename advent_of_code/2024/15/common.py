from collections.abc import Callable


def _read_directions(line: str) -> list[tuple[int, int]]:
    result = []
    for l in line:
        match l:
            case "^":
                result.append((-1, 0))
            case ">":
                result.append((0, 1))
            case "v":
                result.append((1, 0))
            case "<":
                result.append((0, -1))

    return result


def _parse_puzzle(
    file, read_matrix: Callable[[str, list[list[int]]], tuple[int, int] | None]
) -> tuple[list[list[int]], list[tuple[int, int]], tuple[int, int]]:
    matrix: list[list[int]] = []
    directions = []
    robot = None
    reads_matrix = True
    for line in file:
        if line.rstrip() != "" and reads_matrix:
            r = read_matrix(line.rstrip(), matrix)
            if r:
                robot = r
        if line.rstrip() == "" and reads_matrix:
            reads_matrix = False
        if not reads_matrix:
            directions += _read_directions(line.rstrip())

    assert robot, "Missing robot position"

    return matrix, directions, robot


def _calculate_gps_coordinates(matrix):
    total = 0
    for i, m in enumerate(matrix):
        for j, v in enumerate(m):
            if v == 1:
                total += 100 * i + j
    return total
