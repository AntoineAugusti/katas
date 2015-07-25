# http://rosalind.info/problems/pdst/
from itertools import imap


def hamming(a, b):
    return sum(imap(str.__ne__, a, b))


def pDistance(a, b):
    return round((hamming(a, b) * 1.0 / len(a)), 5)


f = open("rosalind_pdst.txt", "r")
dnas = {}
keys = []
currentKey = ''
for content in f:
    # Beginning of a new sample
    if '>' in content:
        key = content.rstrip().replace('>', '')
        currentKey = key
        keys.append(key)
        dnas[currentKey] = ''
    else:
        dnas[currentKey] += content.rstrip()

for i in keys:
    for j in keys:
        print pDistance(dnas[i], dnas[j]),
    print ""
