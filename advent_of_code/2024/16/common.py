import math
from heapq import heappush, heappop


def _parse(puzzle):
    matrix = []
    source = None
    target = None
    for line in puzzle:
        row = []
        for i in list(line.rstrip()):
            match i:
                case "#":
                    row.append(-1)
                case ".":
                    row.append(0)
                case "S":
                    source = (len(matrix), len(row))
                    row.append(0)
                case "E":
                    target = (len(matrix), len(row))
                    row.append(0)
        matrix.append(row)

    return matrix, source, target


def _make_graph(matrix, target):
    vertices = set()
    adj = {}

    height, width = len(matrix), len(matrix[0])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i, r in enumerate(matrix):
        for j, v in enumerate(r):
            if v != 0:
                continue

            if (i, j) == target:
                vertices.add((target, (0, 1)))
                adj[(target, (0, 1))] = {}
            else:
                for d in directions:
                    vertices.add(((i, j), d))

                    if adj.get(((i, j), d)) is None:
                        adj[((i, j), d)] = {}
                    adj[((i, j), d)][((i, j), (d[1], -d[0]))] = 1000
                    adj[((i, j), d)][((i, j), (-d[1], d[0]))] = 1000

                    if ((i + d[0]), j + d[1]) == target:
                        adj[((i, j), d)][(target, (0, 1))] = 1
                    elif (
                        0 <= i + d[0] < height
                        and 0 <= j + d[1] < width
                        and matrix[i + d[0]][j + d[1]] == 0
                    ):
                        adj[((i, j), d)][((i + d[0], j + d[1]), d)] = 1

    return vertices, adj


def _dijkstra_algorithm(vertices, adj, source, target):
    dist = {v: math.inf for v in vertices}
    prev = {v: None for v in vertices}

    q = []
    heappush(q, (0, source))

    dist[source] = 0

    while q:
        _, u = heappop(q)

        if u == target:
            break

        for v in adj[u]:
            alt = dist[u] + adj[u][v]
            if alt == dist[v]:
                prev[v].append(u)
            elif alt < dist[v]:
                dist[v] = alt
                prev[v] = [u]
                heappush(q, (alt, v))

    return dist, prev
