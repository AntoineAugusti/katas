# http://www.prologin.org/training/challenge/demi2014/piege
from sys import stdin, exit

nbChapters = int(stdin.readline())

# Read data for each chapter
data = []
for i in range(nbChapters):
	data.append([int(x) for x in stdin.readline().split()])

for i, elems in enumerate(data):
	# Deal only with non-final chapters
	if (len(elems) > 1):
		neighbours = elems[1:]
		# We can go before, we can have a loop
		if min(neighbours) < i:
			print 1
			exit()

print 0