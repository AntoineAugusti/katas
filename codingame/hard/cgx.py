import sys
import math

newLine = True
spaces = 0
finalStr = ''


def printSpaces(nb):
    global finalStr
    finalStr += ' ' * nb


def printNewline():
    global newLine, finalStr
    finalStr += '\n'
    newLine = True


def myPrint(c):
    global newLine, finalStr
    if newLine:
        printSpaces(spaces)
        newLine = False
    finalStr += c

nbLines = int(raw_input())
data = []
for i in xrange(nbLines):
    data.append(raw_input())
data = [item for sublist in data for item in sublist]
data = ''.join(data)

readingString = False
for c in data:
    if readingString:
        myPrint(c)
        if c == '\'':
            readingString = False
    else:
        if c in [' ', '\t']:
            continue
        elif c == '(':
            if not newLine:
                printNewline()
            myPrint('(')
            printNewline()
            spaces += 4
        elif c == ')':
            spaces -= 4
            if not newLine:
                printNewline()
            myPrint(')')
        elif c == '\'':
            readingString = not readingString
            myPrint('\'')
        elif c == ';':
            myPrint(';')
            printNewline()
        else:
            myPrint(c)

print finalStr
