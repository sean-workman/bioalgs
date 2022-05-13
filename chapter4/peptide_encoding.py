from sys import argv

DNA_CODON_TABLE = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAT': 'N', 'ACA': 'T',
                   'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AGA': 'R', 'AGC': 'S',
                   'AGG': 'R', 'AGT': 'S', 'ATA': 'I', 'ATC': 'I', 'ATG': 'M',
                   'ATT': 'I', 'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAT': 'H',
                   'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CGA': 'R',
                   'CGC': 'R', 'CGG': 'R', 'CGT': 'R', 'CTA': 'L', 'CTC': 'L',
                   'CTG': 'L', 'CTT': 'L', 'GAA': 'E', 'GAC': 'D', 'GAG': 'E',
                   'GAT': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
                   'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'GTA': 'V',
                   'GTC': 'V', 'GTG': 'V', 'GTT': 'V', 'TAA': '', 'TAC': 'Y',
                   'TAG': '', 'TAT': 'Y', 'TCA': 'S', 'TCC': 'S', 'TCG': 'S',
                   'TCT': 'S', 'TGA': '', 'TGC': 'C', 'TGG': 'W', 'TGT': 'C',
                   'TTA': 'L', 'TTC': 'F', 'TTG': 'L', 'TTT': 'F'}

def reverse_complement(pattern):
    translation = pattern.maketrans('ACGT', 'TGCA')
    return pattern.translate(translation)[::-1]

def peptide_encoding(text, peptide, codon_table):
    substrings = []
    start_codons = [k for k,v in codon_table.items() if v == peptide[0]]
    for n in range(3):
        rc = False
        for seq in [text, reverse_complement(text)]:
            reading_frame = seq[n:]
            for ix in range(n, len(reading_frame)-1, 3):
                start = seq[ix:ix+3]
                if start in start_codons:
                    substring = start
                    for ix_e, pep_ix in zip(range(ix+3, len(reading_frame), 3), range(1, len(peptide))):
                        codon = seq[ix_e:ix_e+3]
                        if codon_table[codon] == peptide[pep_ix]:
                            substring += codon
                        else:
                            break
                    if len(substring) == 3*len(peptide):
                        if rc:
                            substrings.append(reverse_complement(substring))
                        else:
                            substrings.append(substring)
            rc = True
    return substrings


def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            text = ''.join(inputs[:-1])
            peptide = inputs[-1]
            codon_table = DNA_CODON_TABLE
    except:
        text = argv[1]
        peptide = argv[2]
        codon_table = DNA_CODON_TABLE
    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]
        with open(output, 'wt') as out:
            substrings = peptide_encoding(text, peptide, codon_table)
            out.write('\n'.join(substrings))

    else:
        print(*peptide_encoding(text, peptide, codon_table))

if __name__ == "__main__":
    main()