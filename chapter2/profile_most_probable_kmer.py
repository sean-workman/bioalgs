from sys import argv

def calculate_kmer_probability(kmer, profile):
    probability = 1
    for ix,nt in enumerate(kmer):
        probability *= profile[nt][ix]
    return probability


def profile_most_probable_kmer(text, k, profile):
    best_probability = 0
    most_probable_kmer = ''
    for ix,_ in enumerate(text[:-k+1]):
        kmer = text[ix:ix+k]
        kmer_probability = calculate_kmer_probability(kmer, profile)
        if kmer_probability > best_probability:
            best_probability = kmer_probability
            most_probable_kmer = kmer        
    return most_probable_kmer


if __name__ == "__main__":

    with open(argv[1]) as data:
        inputs = data.read().split('\n')
        text = inputs[0]
        k = int(inputs[1])
        profile = {nt:[float(p) for p in probs.split()] for nt,probs in zip('ACGT', inputs[2:])}
        # profile = [[float(p) for p in nt.split()] for nt in inputs[2:]]

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]

        with open(output, 'wt') as out:
            median = profile_most_probable_kmer(text, k, profile)
            out.write(median)

    else:
        print(profile_most_probable_kmer(text, k, profile))
