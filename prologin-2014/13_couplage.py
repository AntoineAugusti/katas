# http://www.prologin.org/training/challenge/demi2014/couplage
from sys import stdin

nbBowlsFirst = int(stdin.readline())
nbBowlsSecond = int(stdin.readline())
bowlsFirst = [int(x) for x in stdin.readline().split()]
bowlsSecond = [int(x) for x in stdin.readline().split()]

def maxInTwoLists(first, second):
	"""Find the max value present in two lists"""
	maxFirst = max(first)
	maxSecond = max(second)

	if (maxFirst == maxSecond):
		return maxFirst
	elif (maxFirst < maxSecond):
		second.remove(maxSecond)
		return maxInTwoLists(first, second)
	else:
		first.remove(maxFirst)
		return maxInTwoLists(first, second)

def optimize(acc, first, second):
	# If a list is empty, stop here
	if len(first) == 0 or len(second) == 0:
		return acc

	# Try to reach the max value in these lists
	maxValue = maxInTwoLists(first, second)

	# If we have matching bowls before the maxValue, count them
	for i in range(min(first.index(maxValue), second.index(maxValue))):
		if (first[i] == second[i]):
			return optimize(acc + first[i], first[i+1:], second[i+1:])

	# Determine the index of the maxValue in both lists
	firstIndex = first.index(maxValue)
	secondIndex = second.index(maxValue)

	# Maybe it would be better to not reach this maxValue.
	# Delete it from the first list and try that
	firstWithoutMax = list(first)
	firstWithoutMax.remove(maxValue)

	return max(
		# Go straight to the maxValue in both lists and continue with tails
		optimize(acc + maxValue, first[firstIndex+1:], second[secondIndex+1:]),
		# Maybe it would be better to not reach this maximum
		optimize(acc, firstWithoutMax, second)
	)

print optimize(0, bowlsFirst, bowlsSecond)