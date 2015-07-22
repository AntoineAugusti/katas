# http://rosalind.info/problems/sign/
from itertools import permutations

f = open("rosalind_sign.txt", "r")
for content in f:
    n = (int(content))

originalList = permutations([i for i in range(-n, n+1) if (i != 0)], n)
results = [x for x in originalList if set(range(1, n+1)) == set(map(abs, x))]
print len(results)
for r in results:
    print ' '.join(map(str, r))
