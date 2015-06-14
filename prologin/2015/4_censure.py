# http://prologin.org/training/challenge/demi2015/censure
from sys import stdin

_ = int(stdin.readline())
words = stdin.readline().split()
_ = int(stdin.readline())
positions = [int(x) for x in stdin.readline().split()]

for pos in positions:
    words[pos-1] = '*' * len(words[pos-1])

print ' '.join(str(word) for word in words)
