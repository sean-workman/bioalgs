from sys import argv


def pattern_count(text, pattern):
    """
    Counts the number of times that a pattern is found in a string.

    The commented out implementation works but is much slower. The "find"
    pattern that is implemented below carries out the string comparison in C,
    leading to a huge speedup.
    """
    # count = 0
    # k = len(pattern)
    # for i,_ in enumerate(text[:-k+1]):
    #     if text[i:i+k] == pattern:
    #         count += 1
    # return count
    count = start = 0
    while True:
        start = text.find(pattern, start) + 1
        if start:
            count += 1
        else:
            return count


def main():
    with open(argv[1]) as data:
        inputs = data.read().split()
        text = inputs[0]
        pattern = inputs[1]

    return pattern_count(text, pattern)


if __name__ == "__main__":
    # import time
    # start = time.perf_counter()
    # num = 1000
    # for i in range(num):
    #     main()
    # stop = time.perf_counter()
    # print(f"Elapsed time for {num} iterations: {stop-start:.3f} seconds")
    print(main())
