from sys import argv
from random import randint, choices
from chapter2 import laplacian_form_profile, score_motifs, calculate_kmer_probability, consensus


def generate_biased_probabilities(text, k, profile):
    probabilities = []
    for ix,_ in enumerate(text[:-k+1]):
        kmer = text[ix:ix+k]
        probabilities.append(calculate_kmer_probability(kmer, profile))
    denominator = sum(probabilities)
    return [probability/denominator for probability in probabilities]


def gibbs_sampler(k, t, N, dna):
    min_len = min([len(sequence) for sequence in dna])
    initial_motifs = []
    for sequence in dna:
        ix = randint(0, min_len-k)
        initial_motifs.append(sequence[ix:ix+k])

    best_motifs = initial_motifs

    for n in range(N):
        motifs = best_motifs.copy()
        ix = randint(0,t-1)
        selected_sequence = dna[ix]
        motifs_prefix = motifs[:ix]
        motifs_suffix = motifs[ix+1:]
        sampling_profile = laplacian_form_profile(motifs_prefix+motifs_suffix, k)
        biased_probabilities = generate_biased_probabilities(selected_sequence, k, sampling_profile)
        profile_random_index = choices(range(0, len(selected_sequence)-k+1), weights=biased_probabilities)[0]
        profile_random_kmer = selected_sequence[profile_random_index:profile_random_index+k]
        motifs = motifs_prefix + [profile_random_kmer] + motifs_suffix
        if score_motifs(motifs) < score_motifs(best_motifs):
            best_motifs = motifs
    return best_motifs

def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            k = int(inputs[0])
            t = int(inputs[1])
            N = int(inputs[2])
            dna = inputs[3:]
    except:
        k = int(argv[1])
        t = int(argv[2])
        N = int(argv[3])
        dna = argv[4]
    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]

        with open(output, 'wt') as out:
            best_motifs = gibbs_sampler(k, t, N, dna)
            out.write(' '.join(best_motifs))

    else:
        best_candidates = [gibbs_sampler(k, t, N, dna) for i in range(100)]
        scores = [score_motifs(motif) for motif in best_candidates]
        if '-consensus' in argv:
            top_candidates = best_candidates[scores.index(min(scores))]
            print(consensus(top_candidates))
            print(f"Score: {min(scores)}")
        else:
            print(*best_candidates[scores.index(min(scores))])



if __name__ == "__main__":
    # main()
    import cProfile, pstats
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats.print_stats()