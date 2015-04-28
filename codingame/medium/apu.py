from compiler.ast import flatten


def findFirstTarget(grid):
    for i, line in enumerate(grid):
        for j, point in enumerate(line):
            if pointIsTarget(point):
                return [j, i]
    return [-1, -1]


def findSecondTarget(grid, offsetX, row):
    for j, point in enumerate(grid[row][offsetX:]):
        if pointIsTarget(point):
            return [offsetX + j, row]
    return [-1, -1]


def findThirdTarget(grid, col, offsetY):
    for i, line in enumerate(grid[offsetY:]):
        if pointIsTarget(line[col]):
            return [col, offsetY + i]
    return [-1, -1]


def pointIsTarget(point):
    return point == '0'


def strToLst(string):
    lst = []
    for c in string:
        lst.append(c)
    return lst


def gridHasNode(grid):
    return '0' in ''.join(flatten(grid))


def solve(grid):
    while gridHasNode(grid):
        x1, y1 = findFirstTarget(grid)
        x2, y2 = findSecondTarget(grid, x1 + 1, y1)
        x3, y3 = findThirdTarget(grid, x1, y1 + 1)
        # Three coordinates: a node, its right neighbor, its bottom neighbor
        print '%i %i %i %i %i %i' % (x1, y1, x2, y2, x3, y3)
        # Remove the first node, and try another time
        grid[y1][x1] = '.'

# The number of cells on the X axis
width = int(raw_input())
# The number of cells on the Y axis
height = int(raw_input())

grid = []
for i in xrange(height):
    # Width characters, each either 0 or .
    grid.append(strToLst(raw_input()))


solve(grid)
