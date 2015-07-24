# http://rosalind.info/problems/pmch/
from math import factorial


def nbPerfectMatchings(rna):
    return factorial(rna.count("A")) * factorial(rna.count("C"))

f = open("rosalind_pmch.txt", "r")
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

print nbPerfectMatchings(dnas[currentKey])
