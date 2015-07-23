# http://rosalind.info/problems/revp/


def reverseComplement(dna):
    lookup = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([lookup[c] for c in reversed(dna)])


def findPalindroms(string):
    length = len(string)
    results = []

    for i in range(length):
        for j in range(i+4, i+13):
            if j > length:
                continue

            a = string[i:j]
            b = reverseComplement(a)

            if a == b:
                results.append([i + 1, j - i])
    return results


f = open("rosalind_revp.txt", "r")

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

for possibility in findPalindroms(dnas[currentKey]):
    print ' '.join(map(str, possibility))
