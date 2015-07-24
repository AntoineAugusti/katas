# http://rosalind.info/problems/pper/
from math import factorial


def nbPermutations(n, k):
    return factorial(n)/factorial(n-k) % 1000000

numbers, _ = open("rosalind_pper.txt", "r").read().split('\n')
n, k = map(int, numbers.split())

print nbPermutations(n, k)
