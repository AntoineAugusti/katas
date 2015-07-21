# http://rosalind.info/problems/perm/
from itertools import permutations

f = open("rosalind_perm.txt", "r")
for content in f:
    upperBound = int(content)

possibilities = list(permutations(range(1, upperBound + 1)))
print len(possibilities)

for possibility in possibilities:
    print ' '.join(map(str, possibility))
