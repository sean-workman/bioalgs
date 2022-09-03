from sys import argv
from hamming_distance import hamming_distance


def approximate_pattern_count(pattern, genome, d):
    """
    Returns the number of times that a pattern appears in a string "genome"
    with at most d mismatches.
    """
    count = 0
    k = len(pattern)
    for ix, _ in enumerate(genome[: -k + 1]):
        if hamming_distance(genome[ix : ix + k], pattern) <= d:
            count += 1
    return count


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
            count = approximate_pattern_count(pattern, genome, d)
            out.write(str(count))

    else:
        return approximate_pattern_count(pattern, genome, d)


if __name__ == "__main__":
    # import time
    # start = time.perf_counter()
    # num = 1000
    # for i in range(num):
    #     main()
    # stop = time.perf_counter()
    # print(f"Elapsed time for {num} iterations: {stop-start:.3f} seconds")
    print(main())
