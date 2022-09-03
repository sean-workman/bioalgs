from sys import argv
from hamming_distance import hamming_distance


def approximate_pattern_matching(pattern, genome, d):
    """
    Returns indices of positions in the string "genome" that match the given
    substring pattern with at most d mismatches.
    """
    positions = []
    k = len(pattern)
    for ix, _ in enumerate(genome[: -k + 1]):
        if hamming_distance(genome[ix : ix + k], pattern) <= d:
            positions.append(ix)
    return positions


def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            pattern = inputs[0]
            genome = inputs[1]
            d = int(inputs[2])

    except:
        pattern = argv[1]
        genome = argv[2]
        d = int(argv[3])

    if len(argv) == 3:
        output = argv[2]

        with open(output, "wt") as out:
            positions = approximate_pattern_matching(pattern, genome, d)
            out.write(" ".join([str(p) for p in positions]))

    else:
        return approximate_pattern_matching(pattern, genome, d)


if __name__ == "__main__":
    # import time
    # start = time.perf_counter()
    # num = 1000
    # for i in range(num):
    #     main()
    # stop = time.perf_counter()
    # print(f"Elapsed time for {num} iterations: {stop-start:.3f} seconds")
    print(*main())
