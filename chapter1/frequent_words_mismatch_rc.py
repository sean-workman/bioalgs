from sys import argv
from chapter1 import neighbors, reverse_complement


def frequent_words_mismatch_rc(text, k, d):
    frequent_kmers = []
    freq_map = {}
    n = len(text)
    for ix in range(n-k+1):
        pattern = text[ix:ix+k]
        neighborhood = neighbors(pattern, d) + neighbors(reverse_complement(pattern), d)
        for j in range(len(neighborhood)):
            neighbor = neighborhood[j]
            if neighbor in freq_map:
                freq_map[neighbor] += 1
            else:
                freq_map[neighbor] = 1
    m = max(freq_map.values())
    for seq,count in freq_map.items():
        if count == m:
            frequent_kmers.append(seq)
    return frequent_kmers


if __name__ == "__main__":

    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            text = inputs[0]
            k = int(inputs[1])
            d = int(inputs[2])

    except:
        text = argv[1]
        k = int(argv[2])
        d = int(argv[3])

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]

        with open(output, 'wt') as out:
            frequent_patterns = frequent_words_mismatch_rc(text, k, d)
            out.write(' '.join(frequent_patterns))

    else:
        print(*frequent_words_mismatch_rc(text, k, d))