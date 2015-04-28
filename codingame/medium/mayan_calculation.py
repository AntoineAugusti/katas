def mayanToNumber(mayanSymbols, mayan):
    """Find a mayan numeral in a list of mayan numerals."""
    for val, nb in mayanSymbols.iteritems():
        if ''.join(nb) == ''.join(mayan):
            return val


def numberToMayan(mayanSymbols, number, height):
    """Write a decimal number in a mayan numeral."""
    # Top to bottom, left to write
    result = ""
    for i in xrange(height):
        result += mayanSymbols[number][i]
        # Add a linebreak at the end of every row
        result += "\n"
    return result[:-1]


def readMayanNumber(height):
    """Read a mayan numeral from the command line."""
    nbLines = int(raw_input())
    nbNumbers = nbLines / height
    currentPower = nbNumbers - 1
    data = []
    for _ in xrange(nbNumbers):
        currentMayanSymbol = []
        for _ in xrange(height):
            currentMayanSymbol.append(raw_input())
        data.append((currentPower, mayanToNumber(mayanDict, currentMayanSymbol)))
        currentPower = currentPower - 1
    return data


def readMayanDict(width, height, base):
    """Populate a mayan dictionary, having a representation for
    each number in the given base. Each mayan numeral has got the same
    width and height"""
    mayanDict = {}
    # Numbers that we can display in Mayan
    numbers = range(0, base)
    for i in xrange(height):
        row = raw_input()
        start = 0
        end = width

        for number in numbers:
            # Initialize the list for a new number
            if number not in mayanDict:
                mayanDict[number] = []
            mayanDict[number].append(row[start:end])
            start += width
            end += width
    return mayanDict


def powerTuplesToNumber(data, base):
    """Convert a power list to a decimal result."""
    res = 0
    for power, factor in data:
        res = res + factor * (base**power)
    return res


def computeNumberRes(dataS1, dataS2, op, base):
    """Get the decimal resultat of an operation between
    two mayan numerals"""
    a = powerTuplesToNumber(dataS1, base)
    b = powerTuplesToNumber(dataS2, base)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    return a / b


def numberToPowerList(number, base):
    """Get the power list for a decimal number.
    Example: 12 in base 10 gives [(1, 1), (0, 2)]"""
    if (number == 0):
        return [(0, 0)]

    lst = []
    power = 0
    while (number > 0):
        lst.append((power, number % base))
        number = number / base
        power = power + 1
    # Put the highest power first
    return lst[::-1]

base = 20
# The width and the height of a mayan numeral
width, height = [int(i) for i in raw_input().split()]
# Read the mayan numerals, from 0 to 19
mayanDict = readMayanDict(width, height, base)
# Read the first number
dataS1 = readMayanNumber(height)
# Read the second number
dataS2 = readMayanNumber(height)
# Read the operator to apply between the two numbers
op = raw_input()
# Compute the decimal resultat of the calculation
res = computeNumberRes(dataS1, dataS2, op, base)
# Convert the decimal result in a "power list"
powerList = numberToPowerList(res, base)

# Display each element of the "power list"
# in mayan numeral
for tup in powerList:
    _, nb = tup
    print numberToMayan(mayanDict, nb, height)
