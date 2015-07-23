# http://rosalind.info/problems/rna/

f = open("rosalind_rna.txt", "r")
for content in f:
    print content.rstrip().replace('T', 'U')
