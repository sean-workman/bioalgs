from sys import argv

def debruijn_adjacency_from_kmers(patterns):
    adjacency_list = {node[:-1]:[] for node in patterns}
    for kmer in patterns:
        adjacency_list[kmer[:-1]].append(kmer[1:])
    return adjacency_list

if __name__ == "__main__":
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            patterns = inputs
    except:
        patterns = argv[1].split(',')

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]
        with open(output, 'wt') as out:
            adjacency_list = debruijn_adjacency_from_kmers(patterns)
            for k,v in adjacency_list.items():
                line = k+': '+' '.join(v)+'\n'
                out.write(line)

    else:
        adjacency_list = debruijn_adjacency_from_kmers(patterns)
        for k,v in adjacency_list.items():
            print(k+': '+' '.join(v))
