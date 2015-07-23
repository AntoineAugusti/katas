# http://rosalind.info/problems/grph/


def overlapGraph(dnas, size):
    results = []

    for k1 in dnas:
        for k2 in dnas:
            if k1 != k2 and dnas[k1].endswith(dnas[k2][:size]):
                results.append([k1, k2])
    return results

f = open("rosalind_grph.txt", "r")

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

for possibility in overlapGraph(dnas, 3):
    print ' '.join(possibility)
