# http://prologin.org/training/challenge/demi2015/temperatures
from sys import stdin

nbTemperatures = int(stdin.readline())
temperatures = [int(x) for x in stdin.readline().split()]

deltaEncoding = []
deltaEncoding.append(temperatures[0])
for i in range(1, nbTemperatures):
    deltaEncoding.append(temperatures[i] - temperatures[i-1])

print ' '.join(str(delta) for delta in deltaEncoding)
