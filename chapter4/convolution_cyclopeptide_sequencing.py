from sys import argv

from sys import argv

def spectral_convolution(spectrum, m):
    convolution_map = {}
    for s_mass in spectrum:
        for q_mass in spectrum:
            diff = s_mass - q_mass
            if diff > 0:
                if diff in convolution_map:
                    convolution_map[diff] += 1
                else:
                    convolution_map[diff] = 1
    convolution = {k:v for k,v in sorted(convolution_map.items(), key = lambda item: item[1], reverse=True) if 57 <= k <= 200}
    counts = sorted(list(convolution.values()), reverse=True)
    out = []
    for mass,count in convolution.items():
        if count >= counts[m]:
            out.append(mass)
    return out

def calculate_mass(peptide):
    return sum([int(p) for p in peptide.split('-')])

def expand(peptide_set, masses):
    expanded = set()
    if peptide_set != {''}:
        for peptide in peptide_set:
            for mass in masses:
                expanded.add('-'.join([peptide, mass]))
    else:
        for peptide in peptide_set:
            for mass in masses:
                expanded.add(''.join([peptide, mass]))
    return expanded

def consistency(subject_spectrum, query_spectrum):
    consistent = True
    for mass in query_spectrum:
        if subject_spectrum.count(mass) < query_spectrum.count(mass):
            consistent = False
            break
    return consistent

def get_mass_frequency(spectrum):
    frequency = {}
    for mass in spectrum:
        if (mass in frequency):
            frequency[mass] += 1
        else:
            frequency[mass] = 1
    return frequency

def cyclospectrum(peptide):
    if peptide != '':
        peptide = [int(p) for p in peptide.split('-')]
    prefix_mass = [0]
    for ix,mass in enumerate(peptide, 1):
        prefix_mass.append(prefix_mass[ix-1] + mass)
    peptide_mass = sum(peptide)
    spectrum = [0]
    for i,_ in enumerate(peptide):
        for j,_ in enumerate(peptide[i:], i+1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < len(peptide):
                spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
    return sorted(spectrum)

def cyclic_scoring(peptide, experimental_spectrum):
    theoretical_spectrum = cyclospectrum(peptide)
    scoring_dict = {mass:0 for mass in experimental_spectrum}
    for mass in experimental_spectrum:
        if scoring_dict[mass] < theoretical_spectrum.count(mass):
            scoring_dict[mass] += 1
    score = sum(scoring_dict.values())
    return score

def linear_spectrum(peptide):
    if peptide != '':
        peptide = [int(p) for p in peptide.split('-')]
    prefix_mass = [0]
    for ix,mass in enumerate(peptide, 1):
        prefix_mass.append(prefix_mass[ix-1] + mass)
    spectrum = [0]
    for i,_ in enumerate(peptide):
        for j,_ in enumerate(peptide[i:], i+1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
    return sorted(spectrum)

def linear_scoring(peptide, experimental_spectrum):
    theoretical_spectrum = linear_spectrum(peptide)
    scoring_dict = {mass:0 for mass in experimental_spectrum}
    theoretical_dict = get_mass_frequency(theoretical_spectrum)
    for mass in experimental_spectrum:
        if mass in theoretical_dict:
            if scoring_dict[mass] < theoretical_dict[mass]:
                scoring_dict[mass] += 1
    score = sum(scoring_dict.values())
    return score

def trim(leaderboard, spectrum, n):
    leader_dict = {peptide:0 for peptide in leaderboard}
    new_leaders = set()
    for peptide in leaderboard:
        leader_dict[peptide] = linear_scoring(peptide, spectrum)
    scores = sorted(list(leader_dict.values()), reverse=True)
    scores = scores + [0]*(n-(len(leaderboard)))
    for peptide,score in leader_dict.items():
        if score >= scores[n-1]:
            new_leaders.add(peptide)
    return new_leaders

def convolution_cyclopep_sequencing(spectrum, n, m):
    masses = [str(m) for m in spectral_convolution(spectrum, m)]
    leaderboard = {''}
    leader_peptide = ''
    while leaderboard:
        leaderboard = expand(leaderboard, masses)
        to_filter = set()
        for peptide in leaderboard:
            if calculate_mass(peptide) == spectrum[-1]:
                if cyclic_scoring(peptide, spectrum) > cyclic_scoring(leader_peptide, spectrum):
                    leader_peptide = peptide
            elif calculate_mass(peptide) > spectrum[-1]:
                to_filter.add(peptide)
        leaderboard = {peptide for peptide in leaderboard if peptide not in to_filter}
        leaderboard = trim(leaderboard, spectrum, n)
    return leader_peptide


def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            m  = int(inputs[0])
            n = int(inputs[1])
            spectrum = [int(i) for i in inputs[2:]]
    except:
        m = int(argv[1])
        n = int(argv[2])
        spectrum = [int(i) for i in argv[3].split(',')]

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]
        with open(output, 'wt') as out:
            leader_peptide = convolution_cyclopep_sequencing(spectrum, n, m)
            out.write(leader_peptide)

    else:
        print(convolution_cyclopep_sequencing(spectrum, n, m))


if __name__ == "__main__":
    # main()
    import cProfile, pstats
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats.print_stats()