# http://rosalind.info/problems/tree/


def problem(n, edges):
    return n - len(edges) - 1

f = open("rosalind_tree.txt", "r")
edges = []
i = 1
for content in f:
    if i == 1:
        n = int(content)
    else:
        edges.append(map(int, content.split()))
    i += 1

print problem(n, edges)
