# http://rosalind.info/problems/cons/

f = open("rosalind_cons.txt", "r")

occurences = {}
nucleotides = ['A', 'C', 'G', 'T']
for nucleotide in nucleotides:
    occurences[nucleotide] = []

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
