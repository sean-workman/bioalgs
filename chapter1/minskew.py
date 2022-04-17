from sys import argv

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


if __name__ == "__main__":

    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            genome = inputs[0]

    except:
        genome = argv[1]

    if len(argv) == 3:
        output = argv[2]

        with open(output, 'wt') as out:
            positions = minskew(genome)
            out.write(' '.join(positions))

    else:
        print(*minskew(genome))
        
        


