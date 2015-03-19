from sys import exit

# The number of temperatures to analyse
N = int(raw_input())
# Return 0 and exit if we have no temperatures
if (N <= 0):
	print 0
	exit()

# The N temperatures expressed as integers ranging from -273 to 5526
temperatures = map(int, raw_input().split(' '))

minValue = min(temperatures, key=lambda x:abs(x))

# If two numbers are equally close to 0,
# positive integer has te considered closest to 0
if minValue < 0 and abs(minValue) in temperatures:
	print abs(minValue)
else:
	print minValue