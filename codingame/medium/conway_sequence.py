def describe(original, line):
	# Special cases
	if line == 1:
		return [original]
	elif line == 2:
		return [1, original]
	# General case
	else:
		oldLine = describe(original, line-1)
		res = []
		currentNumber = oldLine[0]
		times = 1
		for nb in oldLine[1:]:
			if nb != currentNumber:
				# Write the current sequence
				res.append(times)
				res.append(currentNumber)
				# Start a new sequence
				currentNumber = nb
				times = 1
			else:
				times += 1

		# Write one last time
		res.append(times)
		res.append(currentNumber)

		return res

def solve(original, line):
	# Transform to a list of strings and join everything
	return ' '.join(str(v) for v in describe(original, line))

original = int(raw_input())
line = int(raw_input())

print solve(original, line)