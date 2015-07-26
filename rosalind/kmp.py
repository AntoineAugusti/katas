# http://rosalind.info/problems/kmp/


def kmp(string):
    P = [0] * len(string)
    j = 0

    for q in range(2, len(string)):
        while j > 0 and string[j] != string[q-1]:
            j = P[j-1]
        if string[j] == string[q-1]:
            j += 1
        P[q-1] = j
    return P

f = open("rosalind_kmp.txt", "r")

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

print ' '.join(map(str, kmp(dnas[currentKey])))
