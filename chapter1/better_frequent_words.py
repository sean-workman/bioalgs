from sys import argv
from frequency_table import frequency_table


def better_frequent_words(text, k):
    """
    An implementation of the frequent words problem that generates a frequency
    table of kmers in the provided text and adds the kmers that have the
    highest count to a set that is subsequently returned.
    """
    frequent_patterns = set()
    freq_map = frequency_table(text, k)
    longest = max(freq_map.values())
    for key, value in freq_map.items():
        if value == longest:
            frequent_patterns.add(key)
    return frequent_patterns


def main():
    with open(argv[1]) as data:
        inputs = data.read().split()
        text = inputs[0]
        k = int(inputs[1])

        return better_frequent_words(text, k)


if __name__ == "__main__":
    # import time
    # start = time.perf_counter()
    # num = 1000
    # for i in range(num):
    #     main()
    # stop = time.perf_counter()
    # print(f"Elapsed time for {num} iterations: {stop-start:.3f} seconds")
    print(*main())
