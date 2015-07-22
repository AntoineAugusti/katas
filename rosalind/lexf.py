# http://rosalind.info/problems/lexf/
from itertools import product

f = open("rosalind_lexf.txt", "r")
i = 1
for content in f:
    if i == 1:
        letters = content.strip().split()
        i += 1
    else:
        nb = int(content)

possibilities = list(product(letters, repeat=nb))

for possibility in possibilities:
    print ''.join(map(str, possibility))
