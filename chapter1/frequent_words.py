from sys import argv
from pattern_count import pattern_count


def frequent_words(text, k):
    """Finds the most frequent k-mers in a given text."""
    frequent_patterns = set()
    count = []
    for i, _ in enumerate(text[: -k + 1]):
        pattern = text[i : i + k]
        count.append(pattern_count(text, pattern))
    max_count = max(count)
    for i, _ in enumerate(text[: -k + 1]):
        if count[i] == max_count:
            frequent_patterns.add(text[i : i + k])
    return frequent_patterns


def main():
    with open(argv[1]) as data:
        inputs = data.read().split()
        text = inputs[0]
        k = int(inputs[1])

    return frequent_words(text, k)


if __name__ == "__main__":
    # import time
    # start = time.perf_counter()
    # num = 1000
    # for i in range(num):
    #     main()
    # stop = time.perf_counter()
    # print(f"Elapsed time for {num} iterations: {stop-start:.3f} seconds")
    print(*main())
