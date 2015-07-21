# http://rosalind.info/problems/iev/

f = open("rosalind_iev.txt", "r")
for content in f:
    values = [int(x) for x in content.split()]

# The probabilities of having an offspring showing the dominant
# factor are the following ones:
#
# AA-AA = 1
# AA-Aa = 1
# AA-aa = 1
# Aa-Aa = 0.75
# Aa-aa = 0.5
# aa-aa = 0
multipliers = [1] * 3 + [.75, .5, 0]
res = 0
for i, val in enumerate(values):
    res += val * multipliers[i]

# And as they will have two descendants, the values are multiplied by two
print int(res * 2)
