from sys import argv
import frequency_table

def find_clumps(text, k, L, t):
    patterns = set()
    n = len(text)
    for ix in range(n-L+1):
        window = text[ix:ix+L]
        freq_map = frequency_table(window, k)
        for seq,count in freq_map.items():
            if count >= t:
                patterns.add(seq)
    return patterns

if __name__ == "__main__":

    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            text = inputs[0]
            k = int(inputs[1])
            L = int(inputs[2])
            t = int(inputs[3])

    except:
        text = argv[1]
        k = int(argv[2])
        L = int(argv[3])
        t = int(argv[4])

    if len(argv) == 3:
        output = argv[2]

        with open(output, 'wt') as out:
            patterns = find_clumps(text, k, L, t)
            out.write(' '.join(patterns))

    else:
        print(*find_clumps(text, k, L, t))

