# http://rosalind.info/problems/seto/


def strToSet(a):
    return set(map(int, a.replace('{', '').replace('}', '').split(', ')))


def printSet(s):
    res = '{'
    res += ', '.join(map(str, s))
    print res + '}'

n, A, B, _ = open("rosalind_seto.txt", "r").read().split('\n')

oneToN = set(range(1, int(n)+1))
A, B = strToSet(A), strToSet(B)

printSet(A.union(B))
printSet(A.intersection(B))
printSet(A - B)
printSet(B - A)
printSet(oneToN - A)
printSet(oneToN - B)
