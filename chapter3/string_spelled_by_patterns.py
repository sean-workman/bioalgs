from sys import argv
from chapter1 import hamming_distance

def string_spelled_by_patterns(first_patterns, second_patterns):
    prefix_string = ''.join([p[:-1] for p in first_patterns[:-1]]) + first_patterns[-1]
    suffix_string = ''.join([p[:-1] for p in second_patterns[:-1]]) + second_patterns[-1]
    distances = []
    for p_ix,_ in enumerate(prefix_string[1:], 1):
        p_query = prefix_string[p_ix:]
        s_query = suffix_string[:-p_ix]
        distances.append((hamming_distance(p_query, s_query)))

    comp_ix = distances.index(min(distances))+1

    return prefix_string[:comp_ix] + suffix_string

def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split('\n')
            first_patterns = inputs[0].split(' ')
            second_patterns = inputs[1].split(' ')

    except:
        first_patterns = argv[1].split(',')
        second_patterns = argv[2].split(',')

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]

        with open(output, 'wt') as out:
            genome = string_spelled_by_patterns(first_patterns, second_patterns)
            out.write(genome)

    else:
        print(string_spelled_by_patterns(first_patterns, second_patterns))

if __name__ == "__main__":
    main()


