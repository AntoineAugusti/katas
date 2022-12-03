# http://prologin.org/training/challenge/demi2015/course_baveuse
from sys import stdin


nbFloors = int(stdin.readline())
data = [[int(stdin.readline())]]
for i in range(1, nbFloors):
    data.append([int(x) for x in stdin.readline().split()])
