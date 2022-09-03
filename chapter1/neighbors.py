from sys import argv
from hamming_distance import hamming_distance


def neighbors(pattern, d):
    """
    Returns a list containing all possible "neighbours" of a given pattern with
    at most d mismatches.
    """
    # Returns the input pattern if the allowed number of mismatches is 0.
    if d == 0:
        return pattern
    # If the length of the pattern is 1, the only variations possible on
    # the input pattern are the 4 nucleotides, no matter the value of d.
    # This represents the base case of the recursion.
    if len(pattern) == 1:
        return ["A", "C", "G", "T"]
    # Initialize an empty set so as not to deal with duplicates
    neighborhood = set()
    # Recursively call the neighbors function
    suffix_neighbors = neighbors(pattern[1:], d)
    for sfx_nbr in suffix_neighbors:
        # Check the Hamming distance of each suffix neighbor and if the
        # distance is less than d, try to add all possible nucleotide + suffix
        # strings to the neighborhood.
        if hamming_distance(pattern[1:], sfx_nbr) < d:
            for nt in "ACGT":
                neighborhood.add(nt + sfx_nbr)
        # Otherwise we take the first character of the pattern being checked
        # recurively and add it + suffix to the neighborhood.
        else:
            neighborhood.add(pattern[0] + sfx_nbr)
    return list(neighborhood)


def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            pattern = inputs[0]
            d = int(inputs[1])

    except:
        pattern = argv[1]
        d = int(argv[2])

    if len(argv) == 3 and argv[2].endswith(".txt"):
        output = argv[2]

        with open(output, "wt") as out:
            neighborhood = neighbors(pattern, d)
            out.write(" ".join(neighborhood))

    else:
        return neighbors(pattern, d)


if __name__ == "__main__":
    # import time
    # start = time.perf_counter()
    # num = 1000
    # for i in range(num):
    #     main()
    # stop = time.perf_counter()
    # print(f"Elapsed time for {num} iterations: {stop-start:.3f} seconds")
    print(*main())
