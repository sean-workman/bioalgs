from sys import argv
from chapter1 import reverse_complement, hamming_distance

def approximate_pattern_matching(pattern, genome, d):
    positions = []
    k = len(pattern)
    rc = reverse_complement(pattern)
    for ix,_ in enumerate(genome[:-k+1]):
        if hamming_distance(genome[ix:ix+k], pattern) <= d:
            positions.append(ix)
    return positions

if __name__ == "__main__":

    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            pattern = inputs[0]
            genome = inputs[1]
            d = int(inputs[2])

    except:
        pattern = argv[1]
        genome = argv[2] 
        d = int(argv[3])

    if len(argv) == 3:
        output = argv[2]

        with open(output, 'wt') as out:
            positions = approximate_pattern_matching(pattern, genome, d)
            out.write(' '.join([str(p) for p in positions]))

    else:
        print(approximate_pattern_matching(pattern, genome, d))
