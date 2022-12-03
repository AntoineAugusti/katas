# http://prologin.org/training/challenge/demi2015/course_baveuse
from sys import stdin

nbSnailsPerPlayer, mapSize = [int(x) for x in stdin.readline().split()]
gameMap = [[0] * mapSize] * mapSize
snails = [[], []]

for i in range(nbSnailsPerPlayer):
    pos, speed = [int(x) for x in stdin.readline().split()]
    snails[0].append([pos, speed])

for i in range(nbSnailsPerPlayer):
    pos, speed = [int(x) for x in stdin.readline().split()]
    snails[1].append([pos, speed])

print snails
