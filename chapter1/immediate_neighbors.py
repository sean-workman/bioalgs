from sys import argv

def immediate_neighbors(pattern):
    neighborhood = set()
    neighborhood.add(pattern)
    print(neighborhood)
    for ix,_ in enumerate(pattern[1:], 1):
        for nt in 'ACGT':
            neighbor = ''.join([pattern[:ix], nt, pattern[ix+1:]])
            neighborhood.add(neighbor)
    return neighborhood


pattern = argv[1]

print(immediate_neighbors(pattern))