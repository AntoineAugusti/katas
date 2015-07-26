# http://rosalind.info/problems/aspc/
from operator import mul


def nCr(n, r):
    r = min(r, n-r)
    if r == 0:
        return 1
    numer = reduce(mul, xrange(n, n-r, -1))
    denom = reduce(mul, xrange(1, r+1))
    return numer / denom

n, m = map(int, open("rosalind_aspc.txt", "r").read().split())

print(sum([nCr(n, k) for k in range(m, n+1)]) % 1000000)
