# http://www.prologin.org/training/challenge/demi2014/rearrangement
from sys import stdin

nbElements = int(stdin.readline())
firstList = [int(x) for x in stdin.readline().split()]
secondList = [int(x) for x in stdin.readline().split()]

firstList.sort()
secondList.sort()

if firstList == secondList:
	print 1
else:
	print 0