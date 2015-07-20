# http://rosalind.info/problems/gc/
from collections import Counter


def computeGCContentPercentage(string):
    counter = Counter(string)

    return 100 * float(counter['C'] + counter['G']) / len(string)


def updateDnas(lines, dnas):
    key = lines[0].replace('>', '')
    dnas[key] = ''.join(lines[1:])
    lines = []

    return dnas


f = open("rosalind_gc.txt", "r")

lines = []
dnas = {}
for content in f:
    # We have a new sample, remember the one we are capturing
    if len(lines) > 1 and '>' in content:
        dnas = updateDnas(lines, dnas)
        lines = []
    lines.append(content.rstrip())

# We "manually" need to add the last DNA sample
dnas = updateDnas(lines, dnas)

# Find the best sample
bestKey, value = max(dnas.iteritems(), key=lambda x: computeGCContentPercentage(x[1]))

print bestKey
print computeGCContentPercentage(value)
