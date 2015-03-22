def packBounds(xMin, xMax, yMin, yMax):
	return [[xMin, xMax], [yMin, yMax]]

def unpackBounds(bounds):
	xMin, xMax = bounds[0]
	yMin, yMax = bounds[1]
	return [xMin, xMax, yMin, yMax]

def nextMove(width, height, x, y, direction, bounds):
	xMin, xMax, yMin, yMax = unpackBounds(bounds)

	if direction == "U":
		yMax = y
	elif direction == "UR":
		xMin = x
		yMax = y
	elif direction == "R":
		xMin = x
	elif direction == "DR":
		xMin = x
		yMin = y
	elif direction == "D":
		yMin = y
	elif direction == "DL":
		xMax = x
		yMin = y
	elif direction == "L":
		xMax = x
	elif direction == "UL":
		yMax = y
		xMax = x

	if "U" in direction or "D" in direction:
		y = (yMax - yMin) / 2 + yMin
	if "L" in direction or "R" in direction:
		x = (xMax - xMin) / 2 + xMin

	return [x, y, packBounds(xMin, xMax, yMin, yMax)]

# width: width of the building.
# height: height of the building.
width, height = [int(i) for i in raw_input().split()]
N = int(raw_input()) # maximum number of turns before game over.
x, y = [int(i) for i in raw_input().split()]

xMin = 0
yMin = 0
xMax = width
yMax = height

bounds = packBounds(xMin, xMax, yMin, yMax)

# Game loop
while True:
	# The direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
	direction = raw_input()
	x, y, bounds = nextMove(width, height, x, y, direction, bounds)
	print str(x) + " " + str(y)