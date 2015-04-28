from collections import defaultdict


def traverseRelations(relations, children, length):
    if len(children) == 0:
        return length

    lengths = []
    for child in children:
        lengths.append(traverseRelations(relations, relations[child], length + 1))

    return max(lengths)

# The number of relationships of influence
n = int(raw_input())
relations = defaultdict(list)
for i in xrange(n):
    # A relationship of influence between two people (x influences y)
    x, y = [int(j) for j in raw_input().split()]
    relations[x].append(y)

# Find the longest succession of influences
lengths = []
for childKey in relations.keys():
    lengths.append(traverseRelations(relations, relations[childKey], 1))

print max(lengths)
