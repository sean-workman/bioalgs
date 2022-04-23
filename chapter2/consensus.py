from statistics import mode
from sys import argv

def consensus(motifs):
    return  [mode(position) for position in zip(*motifs)]