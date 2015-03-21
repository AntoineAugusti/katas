# http://www.prologin.org/training/challenge/demi2014/labyrinthe
from sys import stdin

nbLines = int(stdin.readline())
nbCols = int(stdin.readline())
maze = [[0 for x in range(nbCols)] for x in range(nbLines)]

# Construct the maze
for i in range(nbLines):
	line = [int(x) for x in stdin.readline().split()]
	for j in range(nbCols):
		maze[i][j] = line[j]

# Mark the bottom right cell as the target
maze[nbLines-1][nbCols-1] = 2

nbSteps = 0
def search(x, y):
	global nbSteps

	# Target reached
	if maze[x][y] == 2:
		return True
	# Wall
	elif maze[x][y] == 1:
		return False
	# Already visited
	elif maze[x][y] == 3:
		return False

	# Mark as visited
	maze[x][y] = 3

	# Explore neighbours clockwise
	if ((x < (nbLines - 1) and search(x+1, y))
		or (y > 0 and search(x, y-1))
		or (x > 0 and search(x-1, y))
		or (y < (nbCols - 1) and search(x, y+1))):
		nbSteps += 1
		return True

	return False

# Start to solve the maze
search(0, 0)

# Print the number of steps
if nbSteps > 0:
	print nbSteps
else:
	print -1