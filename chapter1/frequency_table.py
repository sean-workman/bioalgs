from sys import argv


def frequency_table(text, k):
    """Generates a frequency table of all kmers in the provided text."""
    freq_map = {}
    for ix in range(len(text) - k + 1):
        pattern = text[ix : ix + k]
        if pattern in freq_map:
            freq_map[pattern] += 1
        else:
            freq_map[pattern] = 1
    return freq_map


def main():
    with open(argv[1]) as data:
        inputs = data.read().split()
        text = inputs[0]
        k = int(inputs[1])

        return frequency_table(text, k)


if __name__ == "__main__":
    # import time
    # start = time.perf_counter()
    # num = 1000
    # for i in range(num):
    #     main()
    # stop = time.perf_counter()
    # print(f"Elapsed time for {num} iterations: {stop-start:.3f} seconds")
    print(main())
