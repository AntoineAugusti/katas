from math import floor

def getMinAndMaxXAndAvgY(houses):
	minX = houses[0][0]
	maxX = minX
	avgY = 0
	for house in houses:
		x, y = house
		if x < minX:
			minX = x
		if x > maxX:
			maxX = x
		avgY += y
	return [minX, maxX, int(floor(avgY / len(houses)))]

def computeLengthMainCable(end, start):
	return end - start

def optimizeMainCable(houses, avgY):
	# Try to find the best value for the Y of the main cable
	# Compute the minimum length from each building to the
	# vertical average coordinate
	dMin = 9999999
	yCenter = avgY
	for house in houses:
		_, y = house
		dist = abs(y - avgY)
		if dist < dMin:
			yCenter = y
			dMin = dist
	return yCenter

def computeLengthVerticalCables(houses, avgY):
	yMainCable = optimizeMainCable(houses, avgY)
	res = 0
	for house in houses:
		_, y = house
		res += abs(y - yMainCable)
	return res

def solve(houses):
	minX, maxX, avgY = getMinAndMaxXAndAvgY(houses)
	res = computeLengthMainCable(maxX, minX)
	res += computeLengthVerticalCables(houses, avgY)
	return res

N = int(raw_input())
houses = []
for i in xrange(N):
    houses.append([int(i) for i in raw_input().split()])

print solve(houses)