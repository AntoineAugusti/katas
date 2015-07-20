# http://rosalind.info/problems/subs/
from re import finditer

f = open("rosalind_subs.txt", "r")
lines = []
for content in f:
    lines.append(content.rstrip())

string, search = lines
# Find occurrences, with overlapping matches
positions = [str(m.start() + 1) for m in finditer('(?=' + search + ')', string)]

print ' '.join(positions)
