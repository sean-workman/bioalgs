from sys import argv

def debruijn_adjacency(k, text):
    all_kmers = [text[ix:ix+k] for ix,_ in enumerate(text[:-k+1])]
    adjacency_list = {node[:-1]:[] for node in all_kmers}
    for kmer in all_kmers:
        adjacency_list[kmer[:-1]].append(kmer[1:])
    return adjacency_list

if __name__ == "__main__":
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            k = int(inputs[0])
            text = inputs[1]
    except:
        k = int(argv[1])
        text = argv[2]
        print(k)
        print(text)

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]
        with open(output, 'wt') as out:
            adjacency_list = debruijn_adjacency(k, text)
            for k,v in adjacency_list.items():
                line = k+': '+' '.join(v)+'\n'
                out.write(line)

    else:
        adjacency_list = debruijn_adjacency(k, text)
        for k,v in adjacency_list.items():
            print(k+': '+' '.join(v))
