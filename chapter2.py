from chapter1 import *
from statistics import mode
from itertools import product
from random import randint, choices

def motif_enumeration(k, d, dna):
    kmers = set()
    for base_ix,_ in enumerate(dna[0][:-k+1]):
        base = dna[0][base_ix:base_ix+k]
        for kmer in neighbors(base, d):
            checks = []
            for sequence in dna:
                switch = False
                for query_ix,_ in enumerate(sequence[:-k+1]):
                    query = sequence[query_ix:query_ix+k]
                    if kmer in neighbors(query, d):
                        switch = True
                        break
                checks.append(switch)
            if all(checks):
                kmers.add(kmer)
    return kmers    



def d_pattern_string(pattern, dna):
    k = len(pattern)
    total_distance = 0
    for sequence in dna:
        sequence_distance = float('inf')
        for ix,_ in enumerate(sequence[:-k+1]):
            kmer = sequence[ix:ix+k]
            kmer_distance = hamming_distance(pattern, kmer)
            if sequence_distance > kmer_distance:
                sequence_distance = kmer_distance
        total_distance += sequence_distance
    return total_distance

def median_string(k, dna):
    distance = float('inf')
    patterns = [''.join(kmer) for kmer in (product('ACGT', repeat=k))]
    for pattern in patterns:
        pattern_distance = d_pattern_string(pattern, dna)
        if distance > pattern_distance:
            distance = pattern_distance
            median = pattern
    return median



def median_string(k, dna):
    distance = float('inf')
    patterns = [''.join(kmer) for kmer in (product('ACGT', repeat=k))]
    for pattern in patterns:
        pattern_distance = d_pattern_string(pattern, dna)
        if distance > pattern_distance:
            distance = pattern_distance
            median = pattern
    return median



def calculate_kmer_probability(kmer, profile):
    probability = 1
    for ix,nt in enumerate(kmer):
        probability *= profile[nt][ix]
    return probability

def profile_most_probable_kmer(text, k, profile):
    best_probability = 0
    most_probable_kmer = text[:k]
    for ix,_ in enumerate(text[:-k+1]):
        kmer = text[ix:ix+k]
        kmer_probability = calculate_kmer_probability(kmer, profile)
        if kmer_probability > best_probability:
            best_probability = kmer_probability
            most_probable_kmer = kmer
    return most_probable_kmer



def form_profile(motifs, k):
    profile = {'A':[], 'C':[], 'G':[], 'T':[]}
    for ix in range(k):
        base_ix = [sequence[ix] for sequence in motifs]
        probabilities = [base_ix.count(nt)/len(motifs) for nt in 'ACGT']
        for nt,prob in zip('ACGT', probabilities):
            profile[nt].append(prob)
    return profile


def score_motifs(motifs):
    score = 0
    for ix,_ in enumerate(motifs[0]):
        column = ''.join(sequence[ix] for sequence in motifs)
        score += min(hamming_distance(column, nt*len(column)) for nt in "ACGT")
    return score


def greedy_motif_search(k, t, dna):
    best_motifs = [seq[:k] for seq in dna]
    for ix,_ in enumerate(dna[0][:-k+1]):
        kmer = dna[0][ix:ix+k]
        motifs = [kmer]
        for sequence in dna[1:]:
            profile = form_profile(motifs, k)
            most_probable_motif = profile_most_probable_kmer(sequence, k, profile)
            motifs.append(most_probable_motif)
        if score_motifs(motifs) < score_motifs(best_motifs):
            best_motifs = motifs
    return best_motifs


def laplacian_form_profile(motifs, k):
    profile = {'A':[], 'C':[], 'G':[], 'T':[]}
    for ix in range(k):
        base_ix = [sequence[ix] for sequence in motifs]
        probabilities = [(base_ix.count(nt)+1)/(len(motifs)+1) for nt in 'ACGT']
        for nt,prob in zip('ACGT', probabilities):
            profile[nt].append(prob)
    return profile



def laplacian_greedy_motif_search(k, t, dna):
    best_motifs = [seq[:k] for seq in dna]
    for ix,_ in enumerate(dna[0][:-k+1]):
        kmer = dna[0][ix:ix+k]
        candidate_motifs = [kmer]
        for sequence in dna[1:]:
            profile = laplacian_form_profile(candidate_motifs, k)
            most_probable_motif = profile_most_probable_kmer(sequence, k, profile)
            candidate_motifs.append(most_probable_motif)
        if score_motifs(candidate_motifs) < score_motifs(best_motifs):
            best_motifs = candidate_motifs
    return best_motifs


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