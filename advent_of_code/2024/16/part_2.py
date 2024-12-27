from common import _dijkstra_algorithm, _make_graph, _parse


def _find_unique_vertices_on_all_shortest_paths(prev, target):
    s = [target]
    discovered = set()
    unique_vertices = set()

    while s:
        v = s.pop()
        if v not in discovered:
            discovered.add(v)
            unique_vertices.add(v[0])
            if prev[v]:
                for w in prev[v]:
                    s.append(w)

    return len(unique_vertices)


def _solve(puzzle):
    matrix, start, end = _parse(puzzle)
    vertices, adj = _make_graph(matrix, end)
    _, prev = _dijkstra_algorithm(vertices, adj, (start, (0, 1)), (end, (0, 1)))

    return _find_unique_vertices_on_all_shortest_paths(prev, (end, (0, 1)))


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        print(_solve(f))
