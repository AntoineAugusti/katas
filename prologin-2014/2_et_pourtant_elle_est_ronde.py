# http://www.prologin.org/training/challenge/demi2014/et_pourtant_elle_est_ronde
from sys import stdin

nbLines = int(stdin.readline())
nbCharactersPerLine = int(stdin.readline())

pattern = []
for i in range(1, nbLines + 1):
	pattern.append(stdin.readline())

pattern.reverse()

print "".join(pattern)