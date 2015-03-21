# http://www.prologin.org/training/challenge/demi2014/newton
from sys import stdin

nbElements = int(stdin.readline())
m = [[0 for x in range(nbElements)] for x in range(nbElements)]

# Construct the matrix
for i in range(nbElements):
	line = str(stdin.readline())
	for j in range(nbElements):
		m[i][j] = line[j]

tot = 0
for i in range(nbElements):
	firstLine = (i == 0)
	lastLine = (i == nbElements - 1)

	for j in range(nbElements):
		firstCol = (j == 0)
		lastCol = (j == nbElements - 1)
		# Reset the counter
		count = 0
		# Check neighbours
		if (m[i][j] == 'o'):
			# Check previous line
			if (not(firstLine) and m[i-1][j] == 'x'):
				count += 1

			# Check current line
			if (not(firstCol) and m[i][j-1] == 'x'):
				count +=1
			if (not(lastCol) and m[i][j+1] == 'x'):
				count +=1

			# Check next line
			if (not(lastLine) and m[i+1][j] == 'x'):
				count += 1

		# We have a match, remember it
		if count >= 3:
			tot += 1

print tot