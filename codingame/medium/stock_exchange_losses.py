def maxLoss(lst):
	up = lst[0]
	down = lst[0]
	mini = down - up

	for i, val in enumerate(lst[:-1]):
		# We are decreasing
		if (lst[i+1] < val):
			if val > up:
				up = val
			down = val
			if lst[i+1] < down:
				down = lst[i+1]
		if (down - up) < mini:
			mini = down - up

	return mini

# Number of values
n = int(raw_input())
values = [int(x) for x in raw_input().split()]

print maxLoss(values)