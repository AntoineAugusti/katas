# http://rosalind.info/problems/fibd/

f = open("rosalind_fibd.txt", "r")
for content in f:
    n, k = [int(x) for x in content.split()]

f = [0] * (n + 1)
f[0] = 1
for i in range(2, n + 1):
    f[i] = f[i-2] + f[i-1] - f[i - (k + 1)]

print f[n] + f[n-1]
