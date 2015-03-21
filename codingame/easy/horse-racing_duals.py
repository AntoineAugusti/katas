N = int(raw_input())
lst = []
# Read the list
for i in xrange(N):
    lst.append(int(raw_input()))

# Sort the list, ascending order
a = sorted(lst)
# Find the min difference
print min(y-x for x,y in zip(a, a[1:]))