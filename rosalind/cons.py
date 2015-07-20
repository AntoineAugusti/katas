# http://rosalind.info/problems/cons/


def updateDnas(lines, dnas):
    key = lines[0].replace('>', '')
    dnas[key] = ''.join(lines[1:])
    lines = []

    return dnas

f = open("rosalind_cons.txt", "r")

occurences = {}
nucleotides = ['A', 'C', 'G', 'T']
for nucleotide in nucleotides:
    occurences[nucleotide] = []

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

# Build the occurence matrix
for key in dnas:
    for i, c in enumerate(dnas[key]):
        if len(occurences[c]) == 0:
            occurences[c] = [0] * len(dnas[key])
        occurences[c][i] += 1

# Consensus
toWrite = ''
for pos in xrange(len(occurences['A'])):
    mostCommonNucleotide = ''
    maxValue = 0
    for nucleotide in nucleotides:
        if occurences[nucleotide][pos] > maxValue:
            maxValue = occurences[nucleotide][pos]
            mostCommonNucleotide = nucleotide
    toWrite += mostCommonNucleotide

print toWrite

# Profile
for key in nucleotides:
    print "%s: %s" % (key, ' '.join(map(str, occurences[key])))
