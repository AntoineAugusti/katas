# The width of a letter
width = int(raw_input())
# The height of a letter
height = int(raw_input())
# The sentence to write
toWrite = raw_input().upper()
# Letters that we can display in ASCII Art
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"

# Read our data
data = {}
for i in xrange(height):
	row = raw_input()
	start = 0
	end = width

	for letter in letters:
		# Initialize the list for a new letter
		if letter not in data:
			data[letter] = []
		data[letter].append(row[start:end])
		start += width
		end += width

# Write the sentence we are expected to write
# Top to bottom, left to write
result = ""
for i in xrange(height):
	for character in toWrite:
		# We don't know how to display that,
		# fallback to the default character
		if character not in letters:
			result += data["?"][i]
		else:
			result += data[character][i]
	# Add a linebreak at the end of every row
	result += "\n"

print result