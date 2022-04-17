from sys import argv

def hamming_distance(seq1, seq2):
    distance = 0
    for n1,n2 in zip(seq1,seq2):
        if n1 != n2:
            distance += 1
    return distance


if __name__ == "__main__":

    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            seq1 = inputs[0]
            seq2 = inputs[1]

    except:
        seq1 = argv[1]
        seq2 = argv[2]

    print(hamming_distance(seq1, seq2))