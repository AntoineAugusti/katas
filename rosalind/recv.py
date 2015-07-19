# http://rosalind.info/problems/revc/
from string import maketrans

f = open("rosalind_revc.txt", "r")
for content in f:
    print (content.rstrip()[::-1]).translate(maketrans("ATCG", "TAGC"))
