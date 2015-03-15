# http://www.prologin.org/training/challenge/demi2014/voleurs
from sys import stdin

nbPeople = int(stdin.readline())
nbBags = int(stdin.readline())
bags = [int(x) for x in stdin.readline().split()]

# Filter the list
matching = [elem for elem in bags if (elem % nbPeople == 0)]

# Get the max value if the list is not empty
if len(matching) >= 1:
	print max(matching)
else:
	print 0