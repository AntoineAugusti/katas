# http://rosalind.info/problems/sseq/


def findIndicesSequence(source, sequence):
    i = j = 0
    indices = []

    while i < len(source) and j < len(sequence):
        if source[i] == sequence[j]:
            j += 1
            indices.append(i + 1)

        i += 1
    return indices


f = open("rosalind_sseq.txt", "r")

dnas = {}
currentKey = ''
keys = []
for content in f:
    # Beginning of a new sample
    if '>' in content:
        key = content.rstrip().replace('>', '')
        currentKey = key
        keys.append(key)
        dnas[currentKey] = ''
    else:
        dnas[currentKey] += content.rstrip()

indices = findIndicesSequence(dnas[keys[0]], dnas[keys[1]])
print ' '.join(map(str, indices))
