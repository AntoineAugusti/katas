# http://www.prologin.org/training/challenge/demi2014/jump
from sys import stdin

nbPlanets = int(stdin.readline())
planetsSizes = [int(x) for x in stdin.readline().split()]

count = 0
for i, gravity in enumerate(planetsSizes):
	# Beginning of the list
	if (i == 0 and nbPlanets >= 2):
		if (planetsSizes[i + 1] < gravity):
			count += 1

	# Middle of the list
	if (i >= 1 and (i + 1) <= nbPlanets):
		if (planetsSizes[i - 1] < gravity or planetsSizes[i - 1] < gravity):
			count += 1

	# End of list
	if (i == (nbPlanets - 1) and nbPlanets >= 2):
		if (planetsSizes[i - 1] < gravity):
			count += 1

print count