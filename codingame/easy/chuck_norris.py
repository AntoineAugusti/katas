def writeSegment(type, length):
	out = ""
	if (type == 1):
		out += "0 "
	else:
		out += "00 "

	out += '0' * length

	return out

def inputToBits(text):
	out = ""
	for ch in text:
		chBin = bin(ord(ch))[2:]
		while len(chBin) < 7:
			chBin = '0' + chBin
		out += chBin

	return out

bits = inputToBits(raw_input())

answer = ""
currentBit = int(bits[0])
lengthSequence = 1

# Skip the first and the last bits
for bit in bits[1:-1]:
	bit = int(bit)
	if bit == currentBit:
		lengthSequence += 1
	else:
		answer += writeSegment(currentBit, lengthSequence) + " "
		currentBit = bit
		lengthSequence = 1

lastBit = int(bits[-1])
if lastBit == currentBit:
	answer += writeSegment(currentBit, lengthSequence + 1)
else:
	# Write the old sequence
	answer += writeSegment(currentBit, lengthSequence) + " "
	# Do not omit the last bit
	answer += writeSegment(lastBit, 1)

print answer