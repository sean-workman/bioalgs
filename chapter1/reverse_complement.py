from sys import argv


def reverse_complement(pattern):
    """Returns the reverse complement of a sequence."""
    translation = pattern.maketrans("ACGT", "TGCA")
    return pattern.translate(translation)[::-1]


if __name__ == "__main__":

    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            pattern = inputs[0]

    except:
        pattern = argv[1]

    if len(argv) == 3:
        output = argv[2]

        with open(output, "wt") as out:
            rc = reverse_complement(pattern)
            out.write(rc)

    else:
        print(reverse_complement(pattern))
