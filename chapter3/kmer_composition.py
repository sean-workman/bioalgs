from sys import argv

def kmer_composition(k, text):
    return [text[ix:ix+k] for ix,_ in enumerate(text[:-k+1])]

if __name__ == "__main__":

    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            k = int(inputs[0])
            text = inputs[1]

    except:
        k = int(argv[1])
        text = argv[2]

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]

        with open(output, 'wt') as out:
            composition = kmer_composition(k, text)
            out.write(' '.join(composition))

    else:
        print(*kmer_composition(k, text))