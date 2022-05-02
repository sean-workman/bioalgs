from chapter3 import string_reconstruction
from itertools import product
from sys import argv

def k_universal(k):
    kmers = [''.join(kmer) for kmer in list(product('01', repeat=k))]
    path = string_reconstruction(kmers)
    return path[:-k+1]

def main():
    k = int(argv[1])
    print(k_universal(k))

if __name__ == "__main__":
    main()