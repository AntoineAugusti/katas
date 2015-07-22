# http://rosalind.info/problems/mprt/
from re import finditer
from urllib2 import urlopen


def getFasta(ID):
    url = 'http://www.uniprot.org/uniprot/' + ID + '.fasta'
    f = urlopen(url)

    return ''.join(f.read().split('\n')[1:-1])


def findMotif(string):
    indices = []
    for motif in finditer('(?=(N[^P][ST][^P]))', string):
        indices.append(motif.start() + 1)

    return indices

f = open("rosalind_mprt.txt", "r")
for content in f:
    indices = findMotif(getFasta(content.rstrip()))
    if len(indices) > 0:
        print content.rstrip()
        print ' '.join(map(str, indices))
