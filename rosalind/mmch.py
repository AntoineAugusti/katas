# http://rosalind.info/problems/mmch/
from math import factorial


def nPr(n, k):
    '''Returns the number of k-permutations of n.'''
    return factorial(n) / factorial(n-k)

f = open("rosalind_mmch.txt", "r")

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

string = dnas[currentKey]
nbAU = [string.count(c) for c in 'AU']
nbGC = [string.count(c) for c in 'GC']

# There are nPr(max, min) edges for each AU, CG.
# Total number of edges is then the product.
maxNbMatchings = nPr(max(nbAU), min(nbAU)) * nPr(max(nbGC), min(nbGC))
print maxNbMatchings
