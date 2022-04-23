from sys import argv
import reverse_complement

def pattern_matching(pattern, genome):
    positions = []
    k = len(pattern)
    rc = reverse_complement(pattern)
    for ix,_ in enumerate(genome[:-k+1]):
        if genome[ix:ix+k] == (pattern or rc):
            positions.append(ix)
    return positions

if __name__ == "__main__":

    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            pattern = inputs[0]
            genome = inputs[1]

    except TypeError:
        pattern = argv[1]
        genome = argv[2] 

    if len(argv) == 3:
        output = argv[2]

        with open(output, 'wt') as out:
            positions = pattern_matching(pattern, genome)
            out.write(' '.join([str(p) for p in positions]))

    else:
        print(*pattern_matching(pattern, genome))
