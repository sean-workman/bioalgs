from sys import argv
from chapter3 import debruijn_adjacency_from_kmers, eulerian_path, path_to_genome, eulerian_cycle

def string_reconstruction(patterns):
    db = debruijn_adjacency_from_kmers(patterns)
    path = eulerian_path(db)
    text = path_to_genome(path)
    return text

def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            patterns = inputs
    except:
        patterns = argv[1].split(',')

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]
        with open(output, 'wt') as out:
            out.write(string_reconstruction(patterns))

    else:
        print(string_reconstruction(patterns))

if __name__ == "__main__":
    main()