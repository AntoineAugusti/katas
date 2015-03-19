R = int(raw_input()) # the length of the road before the gap.
G = int(raw_input()) # the length of the gap.
L = int(raw_input()) # the length of the landing platform.

# game loop
while 1:
	S = int(raw_input()) # the motorbike's speed.
	X = int(raw_input()) # the position on the road of the motorbike.

	result = "WAIT"

	# Speed up before jumping
	if (X < R and S <= G):
		result = "SPEED"

	# Do not go too fast before the jump
	if (X < R and S > (G + 1)):
		result = "SLOW"

	# Jump just before the gap
	if (X == (R - 1)):
		result = "JUMP"

	# Stop after the gap
	if (X >= (R + G) and S > 0):
		result = "SLOW"

	# A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
	print result