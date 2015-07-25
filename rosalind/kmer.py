# http://rosalind.info/problems/kmer/
from itertools import product
from collections import Counter


def possibleKmers(k):
    return [''.join(x) for x in product('ATGC', repeat=k)]


def kmerComposition(dna, k):
    return Counter([dna[i:i+k] for i in range(len(dna)-k+1)])


def result(kCompositions):
    result = []

    for kmer in sorted(kCompositions.iterkeys()):
        result.append(kCompositions[kmer])

    return result

f = open("rosalind_kmer.txt", "r")

dnas = {}
currentKey = ''
for content in f:
    # Beginning of a new sample
    if '>' in content:
        key = content.rstrip().replace('>', '')
        currentKey = key
        dnas[currentKey] = ''
    else:
        dnas[currentKey] += content.rstrip()

kmerCompos = kmerComposition(dnas[currentKey], 4)
print ' '.join(map(str, result(kmerCompos)))
