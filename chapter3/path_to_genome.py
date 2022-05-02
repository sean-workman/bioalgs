from sys import argv

def path_to_genome(path):
    genome = path[0]
    for sequence in path[1:]:
        genome += sequence[-1]
    return genome

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
            genome = path_to_genome(path)
            out.write(genome)

    else:
        print(path_to_genome(path))
