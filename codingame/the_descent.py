# Game loop
while True:
	SX, SY = [int(i) for i in raw_input().split()]

	moutains = []
	for i in xrange(8):
		# Represents the height of one mountain, from 9 to 0.
		# Mountain heights are provided from left to right.
		moutains.append(int(raw_input()))

	# Target the highest moutain
	if (SX == moutains.index(max(moutains))):
		print "FIRE"
	else:
		print "HOLD"