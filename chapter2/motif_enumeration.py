from sys import argv
from chapter1 import neighbors

def motif_enumeration(k, d, dna):
    kmers = set()
    for base_ix,_ in enumerate(dna[0][:-k+1]):
        base = dna[0][base_ix:base_ix+k]
        for kmer in neighbors(base, d):
            checks = []
            for sequence in dna:
                switch = False
                for query_ix,_ in enumerate(sequence[:-k+1]):
                    query = sequence[query_ix:query_ix+k]
                    if kmer in neighbors(query, d):
                        switch = True
                        break
                checks.append(switch)
            if all(checks):
                kmers.add(kmer)
    return kmers    

if __name__ == "__main__":

    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            k = int(inputs[0])
            d = int(inputs[1])
            dna = inputs[2:]

    except:
        k = int(argv[1])
        d = int(argv[2])
        dna = argv[3]

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]

        with open(output, 'wt') as out:
            patterns = motif_enumeration(k, d, dna)
            out.write(' '.join(patterns))

    else:
        print(*motif_enumeration(k, d, dna))