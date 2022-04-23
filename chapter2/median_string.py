from sys import argv
from itertools import product
from chapter2 import d_pattern_string

def median_string(k, dna):
    distance = float('inf')
    patterns = [''.join(kmer) for kmer in (product('ACGT', repeat=k))]
    for pattern in patterns:
        pattern_distance = d_pattern_string(pattern, dna)
        if distance > pattern_distance:
            distance = pattern_distance
            median = pattern
    return median


if __name__ == "__main__":

    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            k = int(inputs[0])
            dna = inputs[1:]

    except:
        k = int(argv[1])
        dna = argv[2:]

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]

        with open(output, 'wt') as out:
            median = median_string(k, dna)
            out.write(median)

    else:
        print(median_string(k, dna))