from sys import argv
from frequency_table import frequency_table


def find_clumps(text, k, L, t):
    """
    Finds kmer patterns that occur t or more times in a window L in length for
    a given text.
    """
    patterns = set()
    for ix, _ in enumerate(text[: -L + 1]):
        window = text[ix : ix + L]
        freq_map = frequency_table(window, k)
        for seq, count in freq_map.items():
            if count >= t:
                patterns.add(seq)
    return patterns


def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            text = inputs[0]
            k = int(inputs[1])
            L = int(inputs[2])
            t = int(inputs[3])

    except:
        text = argv[1]
        k = int(argv[2])
        L = int(argv[3])
        t = int(argv[4])

    if len(argv) == 3:
        output = argv[2]

        with open(output, "wt") as out:
            patterns = find_clumps(text, k, L, t)
            out.write(" ".join(patterns))

    else:
        return find_clumps(text, k, L, t)


if __name__ == "__main__":
    # import time
    # start = time.perf_counter()
    # num = 1000
    # for i in range(num):
    #     main()
    # stop = time.perf_counter()
    # print(f"Elapsed time for {num} iterations: {stop-start:.3f} seconds")
    print(*main())
