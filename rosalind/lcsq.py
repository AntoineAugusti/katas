# http://rosalind.info/problems/lcsq/


# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
def lcs(str1, str2):
    current = [''] * (len(str2) + 1)
    for c in str1:
        last, current = current, ['']
        for i, t in enumerate(str2):
            current.append(last[i] + c if c == t else max(last[i+1], current[-1], key=len))
    return current[-1]

f = open("rosalind_lcsq.txt", "r")

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

a, b = dnas[keys[0]], dnas[keys[1]]
print lcs(a, b)
