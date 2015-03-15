# http://www.prologin.org/training/challenge/demi2014/correction
from sys import stdin, exit
from itertools import combinations

nbRegions = int(stdin.readline())
nbSheets = [int(x) for x in stdin.readline().split()]

# Quick check to save us some time
if sum(nbSheets) % 2 == 1:
	print 0
	exit()
target = sum(nbSheets) / 2

# Since we are going to try combinations,
# just try up to the "middle length" of the list
for i in range(1, nbRegions / 2 + 1):
	# Get every combination having a length "i"
	for attempt in combinations(nbSheets, i):
		# Transform tuples to a list
		attempt = list(attempt)
		# Copy the original list
		others = list(nbSheets)
		# Delete values from the current attempt
		for val in attempt:
			others.remove(val)

		# We have found a solution!
		if (sum(attempt) == target and sum(others) == target):
			print 1
			exit()
print 0