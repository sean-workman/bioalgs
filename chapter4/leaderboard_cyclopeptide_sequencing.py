from sys import argv

STRING_MASSES = {'57', '71', '87', '97', '99', '101', '103', '113', '114',
                 '115', '128', '129', '131', '137','147', '156', '163', '186'}

def calculate_mass(peptide):
    return sum([int(p) for p in peptide.split('-')])

def expand(peptide_set):
    expanded = set()
    if peptide_set != {''}:
        for peptide in peptide_set:
            for mass in STRING_MASSES:
                expanded.add('-'.join([peptide, mass]))
    else:
        for peptide in peptide_set:
            for mass in STRING_MASSES:
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

def leaderboard_cyclopep_sequencing(spectrum, n):
    leaderboard = {''}
    leader_peptide = ''
    while leaderboard:
        leaderboard = expand(leaderboard)
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
            n = int(inputs[0])
            spectrum = [int(i) for i in inputs[1:]]
    except:
        n = int(argv[1])
        spectrum = [int(i) for i in argv[2].split(',')]

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]
        with open(output, 'wt') as out:
            leader_peptide = leaderboard_cyclopep_sequencing(spectrum, n)
            out.write(leader_peptide)

    else:
        print(leaderboard_cyclopep_sequencing(spectrum, n))


if __name__ == "__main__":
    # main()
    import cProfile, pstats
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats.print_stats()