from sys import argv

def frequency_table(text, k):
    freq_map = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        if pattern in freq_map:
            freq_map[pattern] += 1
        else:
            freq_map[pattern] = 1
    return freq_map

if __name__ == "__main__":

    with open(argv[1]) as data:
        inputs = data.read().split()
        text = inputs[0]
        k = int(inputs[1])

        print(frequency_table(text, k))