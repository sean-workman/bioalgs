from sys import argv
from random import randint
from statistics import mode
from chapter2 import laplacian_form_profile, profile_most_probable_kmer, score_motifs
from time import perf_counter

def consensus(motifs):
    return  ''.join([mode(position) for position in zip(*motifs)])

def randomized_motif_search(k, t, dna):
    min_len = min([len(sequence) for sequence in dna])
    best_motifs = []
    for sequence in dna:
        ix = randint(0, min_len-k)
        best_motifs.append(sequence[ix:ix+k])
    while True:
        profile = laplacian_form_profile(best_motifs, k)
        candidate_motifs = [profile_most_probable_kmer(dna[ix], k, profile) for ix in range(t)]
        if score_motifs(candidate_motifs) < score_motifs(best_motifs):
            best_motifs = candidate_motifs
        else:
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
            best_candidates = [randomized_motif_search(k,t,dna) for i in range(1000)]
            scores = [score_motifs(motif) for motif in best_candidates]
            out.write(' '.join(best_candidates[scores.index(min(scores))]))

    else:
        start = perf_counter()
        best_candidates = [randomized_motif_search(k,t,dna) for i in range(10000)]
        scores = [score_motifs(motif) for motif in best_candidates]
        if '-consensus' in argv:
            top_candidates = best_candidates[scores.index(min(scores))]
            print(consensus(top_candidates))
            print(f"Score: {min(scores)}")
        else:
            print(*best_candidates[scores.index(min(scores))])
        end = perf_counter()
        print(end-start)


