def _parse_locks_and_keys(puzzle):
    is_lock = True
    heights = [0, 0, 0, 0, 0]
    locks, keys = [], []
    for i, line in enumerate(puzzle):
        match i % 8:
            case 0:
                is_lock = line.rstrip() == "#" * 5
                heights = [0, 0, 0, 0, 0]
            case 1 | 2 | 3 | 4 | 5:
                for j, v in enumerate(list(line.rstrip())):
                    heights[j] += 1 if v == "#" else 0
            case 6:
                if is_lock:
                    locks.append(heights)
                else:
                    keys.append(heights)

    return locks, keys


def _solve(puzzle) -> int:
    (locks, keys) = _parse_locks_and_keys(puzzle)

    pairs = 0
    for lock in locks:
        for key in keys:
            for i in range(5):
                if 5 < lock[i] + key[i]:
                    break
            else:
                pairs += 1

    return pairs


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        print(_solve(f))
