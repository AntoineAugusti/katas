# http://rosalind.info/problems/sset/
n, _ = open("rosalind_sset.txt", "r").read().split('\n')

print 2 ** int(n) % 10**6
