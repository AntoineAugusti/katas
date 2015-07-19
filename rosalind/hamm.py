# http://rosalind.info/problems/hamm/
import itertools


def hamming(str1, str2):
    return sum(itertools.imap(str.__ne__, str1, str2))

f = open("rosalind_hamm.txt", "r")
lines = []
for content in f:
    lines.append(content.rstrip())

print hamming(lines[0], lines[1])
