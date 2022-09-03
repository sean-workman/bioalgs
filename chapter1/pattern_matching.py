from sys import argv
from reverse_complement import reverse_complement


def pattern_matching(pattern, genome):
    positions = []
    k = len(pattern)
    rc = reverse_complement(pattern)
    for ix, _ in enumerate(genome[: -len(pattern) + 1]):
        if genome[ix : ix + k] == (pattern or rc):
            positions.append(ix)
    return positions


def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            pattern = inputs[0]
            genome = inputs[1]
    except:
        pattern = argv[1]
        genome = argv[2]

    if len(argv) == 3:
        output = argv[2]
        with open(output, "wt") as out:
            positions = pattern_matching(pattern, genome)
            out.write(" ".join([str(p) for p in positions]))
    else:
        return pattern_matching(pattern, genome)


if __name__ == "__main__":
    # import time
    # start = time.perf_counter()
    # num = 1000
    # for i in range(num):
    #     main()
    # stop = time.perf_counter()
    # print(f"Elapsed time for {num} iterations: {stop-start:.3f} seconds")
    print(*main())
