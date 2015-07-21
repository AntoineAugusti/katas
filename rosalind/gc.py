# http://rosalind.info/problems/gc/
from collections import Counter


def computeGCContentPercentage(string):
    counter = Counter(string)

    return 100 * float(counter['C'] + counter['G']) / len(string)

f = open("rosalind_gc.txt", "r")

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

# Find the best sample
bestKey, value = max(dnas.iteritems(), key=lambda x: computeGCContentPercentage(x[1]))

print bestKey
print computeGCContentPercentage(value)
