from sys import argv

RNA_CODON_TABLE = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T',
                   'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 'AGA': 'R', 'AGC': 'S',
                   'AGG': 'R', 'AGU': 'S', 'AUA': 'I', 'AUC': 'I', 'AUG': 'M',
                   'AUU': 'I', 'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H',
                   'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 'CGA': 'R',
                   'CGC': 'R', 'CGG': 'R', 'CGU': 'R', 'CUA': 'L', 'CUC': 'L',
                   'CUG': 'L', 'CUU': 'L', 'GAA': 'E', 'GAC': 'D', 'GAG': 'E',
                   'GAU': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
                   'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'GUA': 'V',
                   'GUC': 'V', 'GUG': 'V', 'GUU': 'V', 'UAA': '', 'UAC': 'Y',
                   'UAG': '', 'UAU': 'Y', 'UCA': 'S', 'UCC': 'S', 'UCG': 'S',
                   'UCU': 'S', 'UGA': '', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C',
                   'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F'}

def translate_mrna(mrna):
    protein = ''
    for ix in range(0, len(mrna), 3):
        codon = mrna[ix:ix+3]
        protein += RNA_CODON_TABLE[codon]
    return protein

def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            mrna = inputs[0]
    except:
        mrna = argv[1]
    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]
        with open(output, 'wt') as out:
            protein = translate_mrna(mrna)
            out.write(protein)

    else:
        print(translate_mrna(mrna))

if __name__ == "__main__":
    main()