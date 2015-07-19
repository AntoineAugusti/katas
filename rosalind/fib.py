# http://rosalind.info/problems/fib/

# F(n) = F(n - 1) + k * F(n - 2)
def fibo(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1, k) + k * fibo(n-2, k)

f = open("rosalind_fib.txt", "r")
for content in f:
    n, k = [int(x) for x in content.split()]

print fibo(n, k)
