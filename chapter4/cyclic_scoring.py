from sys import argv

AA_MASS = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
           'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
           'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
            'H': 137, 'F': 147, 'R': 156, 'Y': 163,'W': 186}


def cyclic_spectrum(peptide, mass_table):
    prefix_mass = [0]
    for ix,aa in enumerate(peptide, 1):
        for symbol in mass_table.keys():
            if symbol == aa:
                prefix_mass.append(prefix_mass[ix-1] + mass_table[symbol])
    peptide_mass = sum([mass_table[symbol] for symbol in peptide])
    spectrum = [0]
    for i,_ in enumerate(peptide):
        for j,_ in enumerate(peptide[i:], i+1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < len(peptide):
                spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
    return sorted(spectrum)

def cyclic_scoring(peptide, experimental_spectrum):
    theoretical_spectrum = cyclic_spectrum(peptide, AA_MASS)
    scoring_dict = {mass:0 for mass in experimental_spectrum}
    for mass in experimental_spectrum:
        if scoring_dict[mass] < theoretical_spectrum.count(mass):
            scoring_dict[mass] += 1
    score = sum(scoring_dict.values())
    return score

def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            peptide = inputs[0]
            experimental_spectrum = [int(i) for i in inputs[1:]]
            mass_table = AA_MASS
    except:
        peptide = argv[1]
        experimental_spectrum = [int(i) for i in argv[2].split(',')]
        mass_table = AA_MASS
    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]
        with open(output, 'wt') as out:
            theoretical_spectrum = cyclic_spectrum(peptide, mass_table)
            score = cyclic_scoring(experimental_spectrum, theoretical_spectrum)
            out.write(str(score))
    else:
        score = cyclic_scoring(peptide, experimental_spectrum)
        print(score)

if __name__ == "__main__":
    main()
        

