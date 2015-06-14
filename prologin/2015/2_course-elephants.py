# http://prologin.org/training/challenge/demi2015/course_elephants
from sys import stdin
from operator import itemgetter

nbElephants = int(stdin.readline())
target = int(stdin.readline())

speeds = [int(x) for x in stdin.readline().split()]
positions = [int(x) for x in stdin.readline().split()]

bestElephant = 0
lowestValue = target
for i in range(nbElephants):
    # Compute the number of turns required to reach the target
    nbTurnsRequired = (target - positions[i]) / speeds[i]
    if nbTurnsRequired < lowestValue:
        bestElephant = i
        lowestValue = nbTurnsRequired

print bestElephant
