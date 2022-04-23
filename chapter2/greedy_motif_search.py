from sys import argv
from math import prod
from chapter1 import hamming_distance
from chapter2 import profile_most_probable_kmer

def form_profile(motifs, k):
    profile = {'A':[], 'C':[], 'G':[], 'T':[]}
    for ix in range(k):
        base_ix = [sequence[ix] for sequence in motifs]
        probabilities = [base_ix.count(nt)/len(motifs) for nt in 'ACGT']
        for nt,prob in zip('ACGT', probabilities):
            profile[nt].append(prob)
    return profile


def score_motifs(motifs, ):
    score = 0
    for ix,_ in enumerate(motifs[0]):
        column = ''.join(sequence[ix] for sequence in motifs)
        score += min(hamming_distance(column, nt*len(column)) for nt in "ACGT")
    return score


def greedy_motif_search(k, t, dna):
    best_motifs = [seq[:k] for seq in dna]
    for ix,_ in enumerate(dna[0][:-k+1]):
        kmer = dna[0][ix:ix+k]
        candidate_motifs = [kmer]
        for sequence in dna[1:]:
            profile = form_profile(candidate_motifs, k)
            most_probable_motif = profile_most_probable_kmer(sequence, k, profile)
            candidate_motifs.append(most_probable_motif)
        if score_motifs(candidate_motifs) < score_motifs(best_motifs):
            best_motifs = candidate_motifs
    return best_motifs


if __name__ == "__main__":

    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            k = int(inputs[0])
            t = int(inputs[1])
            dna = inputs[2:]

    except:
        k = int(argv[1])
        t = int(argv[2])
        dna = argv[3]

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]

        with open(output, 'wt') as out:
            patterns = greedy_motif_search(k, t, dna)
            out.write(' '.join(patterns))

    else:
        print(*greedy_motif_search(k, t, dna))