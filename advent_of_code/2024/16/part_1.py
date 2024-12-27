from common import _dijkstra_algorithm, _make_graph, _parse


def _solve(puzzle):
    matrix, source, target = _parse(puzzle)
    vertices, adj = _make_graph(matrix, target)
    dist, _ = _dijkstra_algorithm(vertices, adj, (source, (0, 1)), (target, (0, 1)))
    return dist[(target, (0, 1))]


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        print(_solve(f))
