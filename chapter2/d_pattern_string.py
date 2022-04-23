from sys import argv
from chapter1 import hamming_distance

def d_pattern_string(pattern, dna):
    k = len(pattern)
    total_distance = 0
    for sequence in dna:
        sequence_distance = float('inf')
        for ix,_ in enumerate(sequence[:-k+1]):
            kmer = sequence[ix:ix+k]
            kmer_distance = hamming_distance(pattern, kmer)
            if sequence_distance > kmer_distance:
                sequence_distance = kmer_distance
        total_distance += sequence_distance
    return total_distance


if __name__ == "__main__":

    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            pattern = inputs[0]
            dna = inputs[1:]

    except:
        pattern = argv[1]
        dna = argv[2:]

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]

        with open(output, 'wt') as out:
            median = d_pattern_string(pattern, dna)
            out.write(median)

    else:
        print(d_pattern_string(pattern, dna))