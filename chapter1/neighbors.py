from sys import argv
import hamming_distance

def neighbors(pattern, d):
    if d == 0:
        return pattern

    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']

    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for sfx_nbr in suffix_neighbors:
        if hamming_distance(pattern[1:], sfx_nbr) < d:
            for nt in 'ACGT':
                neighborhood.add(nt+sfx_nbr)
        else:
            neighborhood.add(pattern[0]+sfx_nbr)
            
    return list(neighborhood)


if __name__ == "__main__":

    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            pattern = inputs[0]
            d = int(inputs[1])

    except:
        pattern = argv[1]
        d = int(argv[2])

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]

        with open(output, 'wt') as out:
            neighborhood = neighbors(pattern, d)
            out.write(' '.join(neighborhood))

    else:
        print(*neighbors(pattern, d))