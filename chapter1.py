def approximate_pattern_count(text, pattern, d):
    count = 0
    k = len(pattern)

    for ix,_ in enumerate(text[:-k+1]):
        if hamming_distance(text[ix:ix+k], pattern) <= d:
            count += 1

    return count



def approximate_pattern_matching(pattern, genome, d):
    positions = []
    k = len(pattern)
    rc = reverse_complement(pattern)
    for ix,_ in enumerate(genome[:-k+1]):
        if hamming_distance(genome[ix:ix+k], pattern) <= d:
            positions.append(ix)
    return positions



def better_frequent_words(text, k):
    frequent_patterns = []
    freq_map = frequency_table(text, k)
    longest = max(list(freq_map.values()))
    for key,value in freq_map.items():
        if value == longest:
            frequent_patterns.append(key)
    return frequent_patterns



def find_clumps(text, k, L, t):
    patterns = set()
    n = len(text)
    for ix in range(n-L+1):
        window = text[ix:ix+L]
        freq_map = frequency_table(window, k)
        for seq,count in freq_map.items():
            if count >= t:
                patterns.add(seq)
    return patterns



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



def frequent_words_mismatch_rc(text, k, d):
    frequent_kmers = []
    freq_map = {}
    n = len(text)
    for ix in range(n-k+1):
        pattern = text[ix:ix+k]
        neighborhood = neighbors(pattern, d) + neighbors(reverse_complement(pattern), d)
        for j in range(len(neighborhood)):
            neighbor = neighborhood[j]
            if neighbor in freq_map:
                freq_map[neighbor] += 1
            else:
                freq_map[neighbor] = 1
    m = max(freq_map.values())
    for seq,count in freq_map.items():
        if count == m:
            frequent_kmers.append(seq)
    return frequent_kmers



def frequent_words_mismatch(text, k, d):
    frequent_patterns = []
    freq_map = {}
    n = len(text)
    for ix in range(n-k+1):
        pattern = text[ix:ix+k]
        neighborhood = neighbors(pattern, d)
        for j in range(len(neighborhood)):
            neighbor = neighborhood[j]
            if neighbor in freq_map:
                freq_map[neighbor] += 1
            else:
                freq_map[neighbor] = 1
    m = max(freq_map.values())
    for seq,count in freq_map.items():
        if count == m:
            frequent_patterns.append(seq)
    return frequent_patterns



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



def hamming_distance(seq1, seq2):
    distance = 0
    for n1,n2 in zip(seq1,seq2):
        if n1 != n2:
            distance += 1
    return distance



def immediate_neighbors(pattern):
    neighborhood = set()
    neighborhood.add(pattern)
    print(neighborhood)
    for ix,_ in enumerate(pattern[1:], 1):
        for nt in 'ACGT':
            neighbor = ''.join([pattern[:ix], nt, pattern[ix+1:]])
            neighborhood.add(neighbor)
    return neighborhood



def minskew(genome):
    skew = 0
    minskew = 0
    positions = []
    for ix,nt in enumerate(genome):
        if nt == 'G':
            skew += 1
        elif nt == 'C':
            skew -= 1
        if skew == minskew:
            positions.append(ix+1)
        elif skew < minskew:
            minskew = skew
            positions = []
            positions.append(ix+1)
    return positions



def neighbors(pattern, d):
    if d == 0:
        return pattern

    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']

    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for sfx_nbr in suffix_neighbors:
        if hamming_distance(pattern[1:], sfx_nbr) < d:
            for nt in 'ACGT':
                neighborhood.add(nt+sfx_nbr)
        else:
            neighborhood.add(pattern[0]+sfx_nbr)
            
    return list(neighborhood)



def pattern_count(text, pattern):
    count = 0
    k = len(pattern)
    for i, nt in enumerate(text[:-k+1]):
        if text[i:i+k] == pattern:
            count += 1
    return count



def pattern_matching(pattern, genome):
    positions = []
    k = len(pattern)
    rc = reverse_complement(pattern)
    for ix,_ in enumerate(genome[:-k+1]):
        if genome[ix:ix+k] == (pattern or rc):
            positions.append(ix)
    return positions



def reverse_complement(pattern):
    translation = pattern.maketrans('ACGT', 'TGCA')
    return pattern.translate(translation)[::-1]