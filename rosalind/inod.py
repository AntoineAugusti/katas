# http://rosalind.info/problems/inod/

n, _ = open("rosalind_inod.txt", "r").read().split('\n')

# Let m be the number of internal nodes.
# In an unrooted tree, all n leaves have a degree of 1
# and all m internal nodes have a degree of 3. Therefore, the
# total number of edges should be (n + 3m) / 2.
# Also, the number of edges in a tree with (n+m) nodes should be (n+m-1).
#
# (n + 3m) / 2 = n + m - 1
# <=> n + 3m = 2n + 2m - 2
# <=> m = n - 2
print int(n) - 2
