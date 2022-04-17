from sys import argv
from chapter1 import hamming_distance

def approximate_pattern_count(text, pattern, d):
    count = 0
    k = len(pattern)

    for ix,_ in enumerate(text[:-k+1]):
        if hamming_distance(text[ix:ix+k], pattern) <= d:
            count += 1

    return count


if __name__ == "__main__":

    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            text = inputs[0]
            pattern = inputs[1]
            d = int(inputs[2])

    except:
        text = argv[1]
        pattern = argv[2] 
        d = int(argv[3])

    if len(argv) == 3:
        output = argv[2]

        with open(output, 'wt') as out:
            count = approximate_pattern_count(text, pattern, d)
            out.write(str(count))

    else:
        print(approximate_pattern_count(text, pattern, d))