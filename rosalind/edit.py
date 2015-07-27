# http://rosalind.info/problems/edit/

# Wagner-Fischer algorithm
def editDistance(seq1, seq2):
    cur = list(range(len(seq1)+1))
    for j, s in enumerate(seq2):
        last, cur = cur, [j + 1]
        for i, t in enumerate(seq1):
            cur.append(last[i] if s == t else min([last[i+1], last[i], cur[-1]]) + 1)
    return cur[-1]


f = open("rosalind_edit.txt", "r")

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

print editDistance(dnas[keys[0]], dnas[keys[1]])
