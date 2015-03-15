# http://www.prologin.org/training/challenge/demi2014/neologisme
from sys import stdin

dummy = int(stdin.readline())
word = str(stdin.readline())
dictLength = int(stdin.readline())

# Build the list of words
words = [];
for i in range(1, dictLength + 1):
	dummy = int(stdin.readline())
	words.append(str(stdin.readline()))

# Is the word in our list?
if word in words:
	print 0
else:
	print 1