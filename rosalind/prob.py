# http://rosalind.info/problems/prob/
from math import log10


def commonLogarithm(value):
    return log10(value)


def computeProbabilities(GCContent):
    return {
        'C': GCContent / 2,
        'G': GCContent / 2,
        'A': (1 - GCContent) / 2,
        'T': (1 - GCContent) / 2
    }


def computeMatchProbability(string, GCContent):
    probabilities = computeProbabilities(GCContent)

    res = 1
    for c in string:
        res *= probabilities[c]

    return commonLogarithm(res)

dna, GCContents, _ = open("rosalind_prob.txt", "r").read().split('\n')
GCContents = map(float, GCContents.split())

print ' '.join(map(str, [computeMatchProbability(dna, v) for v in GCContents]))
