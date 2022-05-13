from sys import argv

STRING_MASSES = ['57', '71', '87', '97', '99', '101', '103', '113', '114',
                 '115', '128', '129', '131', '137','147', '156', '163', '186']

def calculate_mass(peptide):
    return sum([int(p) for p in peptide.split('-')])

def expand(peptide_list):
    expanded = []
    if peptide_list != ['']:
        for peptide in peptide_list:
            for mass in STRING_MASSES:
                expanded.append('-'.join([peptide, mass]))
    else:
        for peptide in peptide_list:
            for mass in STRING_MASSES:
                expanded.append(''.join([peptide, mass]))
    return expanded

def consistency(subject_spectrum, query_spectrum):
    consistent = True
    for mass in query_spectrum:
        if subject_spectrum.count(mass) < query_spectrum.count(mass):
            consistent = False
            break
    return consistent

def cyclospectrum(peptide):
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

def linear_spectrum(peptide):
    peptide = [int(p) for p in peptide.split('-')]
    prefix_mass = [0]
    for ix,mass in enumerate(peptide, 1):
        prefix_mass.append(prefix_mass[ix-1] + mass)
    spectrum = [0]
    for i,_ in enumerate(peptide):
        for j,_ in enumerate(peptide[i:], i+1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
    return sorted(spectrum)

def bb_cyclopep_sequencing(spectrum):
    '''
    Starting with an empty string as a "candidate peptide" we enter a while loop that will continue until no candidates exist.
    In each iteration of the while loop, our candidate peptides are all "branched" 20x into peptides that contain all possible
    amino acids at the next residue.

    Then, for each candidate peptide we generate its cyclic spectrum - if the total mass of the candidate is equal to
    the mass of the parent peptide in our input spectrum we check to see if the candidates spectrum is equivalent
    to our input spectrum. If the spectra are equivalent and the peptide that generated the spectrum is not yet in
    our list of final peptides, we add it to the list and then remove it from the pool of candidates.

    If the mass of the peptide is not equal to the input peptide, we check to see if its spectrum is "consistent"
    with that of the input spectrum (i.e. the number of times we see a particular mass in our query spectrum must be
    less than or equal to the number of occurrences of that mass in our input spectrum). If it isn't consistent it
    is added to a list that indicates it should be removed.
    
    '''
    candidate_peptides = ['']
    final_peptides = []
    while candidate_peptides:
        candidate_peptides = expand(candidate_peptides)
        filtered_candidates = []
        for peptide in candidate_peptides:
            if calculate_mass(peptide) == spectrum[-1]:
                if (cyclospectrum(peptide) == spectrum) and peptide not in final_peptides:
                    final_peptides.append(peptide)
                candidate_peptides.remove(peptide)
            elif consistency(spectrum, linear_spectrum(peptide)):
                filtered_candidates.append(peptide)
        candidate_peptides = filtered_candidates
    return final_peptides

def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            spectrum = [int(i) for i in inputs]
    except:
        spectrum = argv[1].split(',')

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]
        with open(output, 'wt') as out:
            final_peptides = bb_cyclopep_sequencing(spectrum)
            out.write(' '.join(map(str, final_peptides)))

    else:
        print(*bb_cyclopep_sequencing(spectrum))

if __name__ == "__main__":
    main()