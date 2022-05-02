from sys import argv

def overlap_adjacency(patterns):
    adjacency_list = {}
    for kmer in patterns:
        kmer_list = []
        kmer_suffix= kmer[1:]
        for query in patterns:
            if query[:-1] == kmer_suffix:
                kmer_list.append(query)
        if kmer_list:
            adjacency_list[kmer] = kmer_list
    return adjacency_list

if __name__ == "__main__":
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            path = inputs
    except:
        path = argv[1].split(',')

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]
        with open(output, 'wt') as out:
            adjacency_list = overlap_adjacency(path)
            for k,v in adjacency_list.items():
                line = k+': '+' '.join(v)+'\n'
                out.write(line)

    else:
        print(overlap_adjacency(path))
