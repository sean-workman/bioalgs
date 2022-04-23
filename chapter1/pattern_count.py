from sys import argv

def pattern_count(text, pattern):
    count = 0
    k = len(pattern)
    for i, nt in enumerate(text[:-k+1]):
        if text[i:i+k] == pattern:
            count += 1
    return count


if __name__ == "__main__":

    with open(argv[1]) as data:
        inputs = data.read().split()
        text = inputs[0]
        pattern = inputs[1]

    print(*pattern_count(text,pattern))