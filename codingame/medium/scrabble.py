def pointForLetter(letter):
	if letter in ['e', 'a', 'i', 'o', 'n', 'r', 't', 'l', 's', 'u']:
		return 1
	elif letter in ['d', 'g']:
		return 2
	elif letter in ['b', 'c', 'm', 'p']:
		return 3
	elif letter in ['f', 'h', 'v', 'w', 'y']:
		return 4
	elif letter == 'k':
		return 5
	elif letter in ['j', 'x']:
		return 8
	else:
		return 10

def stringToList(string):
	lst = []
	for c in string:
		lst.append(c)
	return lst

def rankForWord(word):
	res = 0
	for c in word:
		res += pointForLetter(c)
	return res

def canWriteWordWithLetters(word, letters):
	letters = stringToList(letters)
	for c in word:
		if c in letters:
			letters.remove(c)
		else:
			return False
	return True

def optimizeScore(dictionary, availableLetters):
	maxScore = 0
	bestWord = ""
	keyForBestWord = 0
	for word, data in dictionary.iteritems():
		score, key = data
		# If we have found a better score and we can write this word
		if (score >= maxScore and canWriteWordWithLetters(word, availableLetters)):
			# Update the best word only if the score is better
			# of if the score is the same, keep the 1st word in
			# the dictionary
			if (score > maxScore or (score == maxScore and key < keyForBestWord)):
				maxScore = score
				bestWord = word
				keyForBestWord = key
	return bestWord

N = int(raw_input())

# Read available words in the dictionary
dictionary = dict()
for i in xrange(N):
	word = str(raw_input())
	# Remember the word, its score and its position
	dictionary[word] = [rankForWord(word), i]

# Read letters we have to write the best word
availableLetters = raw_input()

print optimizeScore(dictionary, availableLetters)