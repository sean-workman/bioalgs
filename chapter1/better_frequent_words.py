from sys import argv
from chapter1 import frequency_table

def better_frequent_words(text, k):
    frequent_patterns = []
    freq_map = frequency_table(text, k)
    longest = max(list(freq_map.values()))
    for key,value in freq_map.items():
        if value == longest:
            frequent_patterns.append(key)
    return frequent_patterns

if __name__ == "__main__":

    with open(argv[1]) as data:
        inputs = data.read().split()
        text = inputs[0]
        k = int(inputs[1])

        print(*better_frequent_words(text, k))