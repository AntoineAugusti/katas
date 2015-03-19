# LX: the X position of the light of power
# LY: the Y position of the light of power
# x: Thor's starting X position
# y: Thor's starting Y position
LX, LY, x, y = [int(i) for i in raw_input().split()]

# Game loop
while True:
	E = int(raw_input()) # The level of Thor's remaining energy, representing the number of moves he can still make.
	result = ""

	if (y < LY):
		result = "S"
		y += 1
	elif (LY < y):
		result = "N"
		y -= 1
	if (x < LX):
		result += "E"
		x += 1
	elif (LX < x):
		result += "W"
		x -= 1

	print result