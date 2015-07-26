# http://rosalind.info/problems/corr/
from itertools import imap


def hamming(str1, str2):
    return sum(imap(str.__ne__, str1, str2))


def findCorrectAndIncorrectReads(reads):
    correct = []

    for read in reads:
        rc = reverseComplement(read)
        count = reads.count(read) + reads.count(rc)
        if count >= 2:
            correct.append(read)

    return (list(set(reads) - set(correct)), list(set(correct)))

# Correct two strings who differ by one base pair
# str1 is the incorrect string
def correctString(str1, str2):
    corrected = list(str2[:])
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            corrected[i] = str2[i]

    return ''.join(corrected)

# Find the corrections for each of the incorect reads
def findCorrections(incorrectReads, correctReads):
    reversedCorrectReads = map(reverseComplement, correctReads)

    corrections = []
    for incorrect in incorrectReads:
        for correct in list(set(correctReads).union(set(reversedCorrectReads))):
            if hamming(incorrect, correct) == 1:
                corrections.append((incorrect, correctString(incorrect, correct)))

    return corrections

def printCorrection(correction):
    print correction[0] + '->' + correction[1]


def reverseComplement(dna):
    lookup = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([lookup[c] for c in reversed(dna)])


f = open("rosalind_corr.txt", "r")

dnas = {}
currentKey = ''
for content in f:
    # Beginning of a new sample
    if '>' in content:
        key = content.rstrip().replace('>', '')
        currentKey = key
        dnas[currentKey] = ''
    else:
        dnas[currentKey] += content.rstrip()

incorrect, correct = findCorrectAndIncorrectReads(dnas.values())
corrections = findCorrections(incorrect, correct)
map(printCorrection, corrections)
