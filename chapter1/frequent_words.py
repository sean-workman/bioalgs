from ast import keyword
from sys import argv
from chapter1 import pattern_count


def frequent_words(text, k):
    frequent_patterns = set()
    count = []
    for i,_ in enumerate(text[:-k+1]):
        pattern = text[i:i+k]
        count.append(pattern_count(text, pattern))
    max_count = max(count)
    for i,_ in enumerate(text[:-k+1]):
        if count[i] == max_count:
            frequent_patterns.add(text[i:i+k])
    return frequent_patterns




if __name__ == "__main__":

    with open(argv[1]) as data:
        inputs = data.read().split()
        text = inputs[0]
        k = int(inputs[1])

    print(*frequent_words(text, k))