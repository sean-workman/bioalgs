from sys import argv


def minimum_skew(genome):
    """
    Returns the positions in the genome with the minimum skew value. Skew is
    defined here as the difference between the total number of occurrences of
    G and the total number of occurrences of C in the genome at a position
    downstream from the genome start.
    """
    skew = minskew = 0
    positions = []
    for ix, nt in enumerate(genome):
        if nt == "G":
            skew += 1
        elif nt == "C":
            skew -= 1
        if skew == minskew:
            positions.append(ix + 1)
        elif skew < minskew:
            minskew = skew
            positions = []
            positions.append(ix + 1)
    return positions


def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            genome = inputs[0]

    except:
        genome = argv[1]

    if len(argv) == 3:
        output = argv[2]

        with open(output, "wt") as out:
            positions = minimum_skew(genome)
            out.write(" ".join(positions))

    else:
        return minimum_skew(genome)


if __name__ == "__main__":
    # import time
    # start = time.perf_counter()
    # num = 1000
    # for i in range(num):
    #     main()
    # stop = time.perf_counter()
    # print(f"Elapsed time for {num} iterations: {stop-start:.3f} seconds")
    print(*main())
