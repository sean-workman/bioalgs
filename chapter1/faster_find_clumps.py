from sys import argv


def fast_find_clumps(text, k, L, t):
    pos_map = position_table(text, k)
    clumps = set()
    for pattern in pos_map:
        positions = pos_map[pattern]
        if len(positions) >= t:
            if is_clump(positions, k, L, t):
                clumps.add(pattern)
    return clumps


def position_table(text, k):
    pos_map = {}
    for ix, _ in enumerate(text[: -k + 1]):
        pattern = text[ix : ix + k]
        if pattern in pos_map:
            pos_map[pattern].append(ix)
        else:
            pos_map[pattern] = [ix]
    return pos_map


def is_clump(positions, k, L, t):
    for ix, _ in enumerate(positions[: -t + 1]):
        if positions[ix + t - 1] - positions[ix] <= L - k:
            return True
    return False


def main():
    try:
        with open(argv[1]) as data:
            lines = " ".join([l.rstrip() for l in data.readlines()]).split()
            text = lines[0]
            k = int(lines[1])
            L = int(lines[2])
            t = int(lines[3])

    except:
        text = argv[1]
        k = int(argv[2])
        L = int(argv[3])
        t = int(argv[4])

    if len(argv) == 3:
        output = argv[2]

        with open(output, "wt") as out:
            patterns = fast_find_clumps(text, k, L, t)
            out.write(" ".join(patterns))

    else:
        return fast_find_clumps(text, k, L, t)


if __name__ == "__main__":
    # print(main())
    import time

    start = time.perf_counter()
    for i in range(1):
        main()
    stop = time.perf_counter()
    print(f"Elapsed time: {stop-start:.2f} seconds")
