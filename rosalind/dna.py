# http://rosalind.info/problems/dna/
f = open("rosalind_dna.txt", "r")
for content in f:
    a = content.count('A')
    c = content.count('C')
    g = content.count('G')
    t = content.count('T')
    print '%s %s %s %s' % (a, c, g, t)
