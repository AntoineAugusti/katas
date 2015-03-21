from math import radians, cos, sqrt

def degreesToRadians(degree):
	return radians(float(degree.replace(",", ".")))

def parseDefribrillator(defibrillator):
	lst = [str(x) for x in defibrillator.split(";")]
	# To float and then degrees to radians
	lst[-1] = radians(float(lst[-1].replace(",", ".")))
	lst[-2] = radians(float(lst[-2].replace(",", ".")))

	return lst

def distance(lonA, latA, lonB, latB):
	x = (lonB - lonA) * cos((latA + latB) / 2)
	y = (latB - latA)
	return sqrt(x*x + y*y) * 6371

def closestDefibrillator(defibrillators, lon, lat):
	minDist = 99999
	name = ""
	for defibrillator in defibrillators:
		dist = distance(defibrillator[-2], defibrillator[-1], lon, lat)
		if dist < minDist:
			minDist = dist
			name = defibrillator[1]

	return name

# User's longitude (in degrees)
lon = degreesToRadians(raw_input())
# User's latitude (in degrees)
lat = degreesToRadians(raw_input())
# The number N of defibrillators located in the streets of Montpellier
N = int(raw_input())

# Read data for each defibrillators
defibrillators = []
for i in xrange(N):
	defibrillators.append(parseDefribrillator(raw_input()))

# Find the closest one
print closestDefibrillator(defibrillators, lon, lat)