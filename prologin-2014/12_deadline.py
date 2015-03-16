# http://www.prologin.org/training/challenge/demi2014/deadline
from sys import stdin
from itertools import combinations

remainingTime = int(stdin.readline())
remainingExercises = int(stdin.readline())

# Grab exercises
data = []
for i in range(remainingExercises):
	data.append([int(x) for x in stdin.readline().split()])

hasSolution = True
combinationLength = 2
maxPoints = 0

while hasSolution:
	attemptsInRange = []

	# Get every combination having a length "combinationLength"
	for attempt in combinations(data, combinationLength):
		timer = 0
		points = 0
		# Transform tuples to a list
		attempt = list(attempt)

		for exercise in attempt:
			timer += exercise[0]
			points += exercise[1]

		# Remember if the attemp was in our allowed time range
		inTimeAllowed = (timer <= remainingTime)
		attemptsInRange.append(inTimeAllowed)

		# We have found a solution! Remember it
		if (inTimeAllowed and points > maxPoints):
			maxPoints = points

	# If we had only failed attemps, we can't do better
	if (attemptsInRange.count(False) == len(attemptsInRange)):
		hasSolution = False
	# Otherwise, try to do more exercises
	else:
		combinationLength += 1

print maxPoints