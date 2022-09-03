from sys import argv
from neighbors import neighbors
from reverse_complement import reverse_complement


def frequent_words_mismatch_rc(text, k, d):
    """
    Returns the most frequent kmers in a given text with up to d mismatches
    taking into account the reverse complement of the text.
    """
    frequent_patterns = []
    freq_map = {}
    for ix, _ in enumerate(text[: -k + 1]):
        pattern = text[ix : ix + k]
        neighborhood = neighbors(pattern, d) + neighbors(reverse_complement(pattern), d)
        for neighbor in neighborhood:
            if neighbor in freq_map:
                freq_map[neighbor] += 1
            else:
                freq_map[neighbor] = 1
    m = max(freq_map.values())
    for seq, count in freq_map.items():
        if count == m:
            frequent_patterns.append(seq)
    return frequent_patterns


def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            text = inputs[0]
            k = int(inputs[1])
            d = int(inputs[2])
    except:
        text = argv[1]
        k = int(argv[2])
        d = int(argv[3])
    if len(argv) == 3 and argv[2].endswith(".txt"):
        output = argv[2]

        with open(output, "wt") as out:
            frequent_patterns = frequent_words_mismatch_rc(text, k, d)
            out.write(" ".join(frequent_patterns))
    else:
        return frequent_words_mismatch_rc(text, k, d)


if __name__ == "__main__":
    # import time
    # start = time.perf_counter()
    # num = 1000
    # for i in range(num):
    #     main()
    # stop = time.perf_counter()
    # print(f"Elapsed time for {num} iterations: {stop-start:.3f} seconds")
    print(*main())
