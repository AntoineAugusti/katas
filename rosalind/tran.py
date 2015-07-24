# http://rosalind.info/problems/tran/


def isTransition(a, b):
    lst = sorted([a, b])

    return lst == ['A', 'G'] or lst == ['C', 'T']


def isTransversion(a, b):
    lst = sorted([a, b])

    if lst == ['A', 'C'] or lst == ['A', 'T']:
        return True
    if lst == ['C', 'G'] or lst == ['G', 'T']:
        return True

    return False


def computeTransitionTransversion(str1, str2):
    nbTransitions = nbTransversions = 0

    for i in range(len(str1)):
        if isTransversion(str1[i], str2[i]):
            nbTransversions += 1
        if isTransition(str1[i], str2[i]):
            nbTransitions += 1

    return [nbTransitions, nbTransversions]

f = open("rosalind_tran.txt", "r")
dnas = {}
keys = []
currentKey = ''
for content in f:
    # Beginning of a new sample
    if '>' in content:
        key = content.rstrip().replace('>', '')
        currentKey = key
        keys.append(key)
        dnas[currentKey] = ''
    else:
        dnas[currentKey] += content.rstrip()

str1, str2 = [dnas[keys[0]], dnas[keys[1]]]
transitions, transversions = computeTransitionTransversion(str1, str2)
print transitions / float(transversions)
