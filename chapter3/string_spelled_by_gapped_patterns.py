from sys import argv

def string_spelled_by_patterns(patterns, k):
    return ''.join([p[:-k+1] for p in patterns[:-1]]) + patterns[-1]

def string_spelled_by_gapped_patterns(k, d, gapped_patterns):
    first_patterns = [p[0] for p in gapped_patterns]
    second_patterns = [p[1] for p in gapped_patterns]
    prefix_string = string_spelled_by_patterns(first_patterns, k)
    suffix_string = string_spelled_by_patterns(second_patterns, k)
    for i in range(k+d+1, len(prefix_string)):
        if prefix_string[i] != suffix_string[i-k-d]:
            return "There is no string spelled by the gapped patterns"
    return prefix_string + suffix_string[-(k+d):]

def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            k = int(inputs[0])
            d = int(inputs[1])
            gapped_patterns = [p.split('|') for p in inputs[2:]]


    except:
        k = int(argv[1])
        d = int(argv[2])
        gapped_patterns = [p.split('|') for p in argv[3].split(',')]

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]

        with open(output, 'wt') as out:
            string = string_spelled_by_gapped_patterns(k, d, gapped_patterns)
            out.write(string)

    else:
        print(string_spelled_by_gapped_patterns(k, d, gapped_patterns))
    
if __name__ == "__main__":
    main()