from copy import deepcopy


def strToLst(str):
    lst = []
    for c in str:
        lst.append(c)
    return lst


def normalizeDirection(direction):
    if direction == 'N':
        return 'NORTH'
    elif direction == 'S':
        return 'SOUTH'
    elif direction == 'E':
        return 'EAST'
    elif direction == 'W':
        return 'WEST'

    return direction


class Pos(object):
    def __init__(self, x, y):
        super(Pos, self).__init__()
        self.xVal = x
        self.yVal = y

    def x(self):
        return self.xVal

    def y(self):
        return self.yVal

    def toDirection(self, direction):
        direction = normalizeDirection(direction)
        if direction == 'SOUTH':
            return Pos(self.xVal, self.yVal + 1)
        elif direction == 'NORTH':
            return Pos(self.xVal, self.yVal - 1)
        elif direction == 'EAST':
            return Pos(self.xVal + 1, self.yVal)
        elif direction == 'WEST':
            return Pos(self.xVal - 1, self.yVal)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.xVal == other.x()
                and self.yVal == other.y())

    def __ne__(self, other):
        return not self.__eq__(other)


class Map(object):
    def __init__(self):
        super(Map, self).__init__()
        self.map = None
        self.currentPos = None
        self.breaker = False
        self.directions = ['SOUTH', 'EAST', 'NORTH', 'WEST']
        self.currentDirectionIndex = -1

        # Read and create the map
        self.createMap()

    def nextDirection(self):
        self.currentDirectionIndex += 1
        return self.directions[self.currentDirectionIndex]

    def nextPosition(self):
        direction = self.nextDirection()
        pos = self.getCurrentPos().toDirection(direction)
        return [direction, pos]

    def getCurrentPos(self):
        return self.currentPos

    def cleanPointInMap(self, pos):
        self.map[pos.y()][pos.x()] = ' '

    def moveTo(self, pos):
        self.currentDirectionIndex = -1
        self.currentPos = pos

        # We stepped on a beer, enable or disable
        # the breaker mode
        if self.isBeer(self.getCurrentPos()):
            self.breaker = not self.breaker

        # We stepped on an inverter, reverse direction priorities
        if self.isInverter(self.getCurrentPos()):
            self.directions.reverse()

        # If we were on breaker mode and on an obstacle,
        # destroy it
        if self.breaker and self.canBeDestroyed(self.getCurrentPos()):
            self.cleanPointInMap(self.getCurrentPos())

        # We stepped on a teleporter, go to the other teleporter
        if self.isTeleporter(self.getCurrentPos()):
            self.currentPos = self.findOtherTeleporter(self.getCurrentPos())

    def pointAtPos(self, pos):
        return self.map[pos.y()][pos.x()]

    def pointAtPosIsInValues(self, pos, values):
        for val in values:
            if self.pointAtPosIs(pos, val):
                return True
        return False

    def pointAtPosIs(self, pos, expected):
        return self.pointAtPos(pos) == expected

    def canBeDestroyed(self, pos):
        return self.pointAtPosIs(pos, 'X')

    def isBorder(self, pos):
        return self.pointAtPosIs(pos, '#')

    def isObstacle(self, pos):
        return self.pointAtPosIs(pos, 'X')

    def isBeer(self, pos):
        return self.pointAtPosIs(pos, 'B')

    def isInverter(self, pos):
        return self.pointAtPosIs(pos, 'I')

    def isTeleporter(self, pos):
        return self.pointAtPosIs(pos, 'T')

    def isDirectionChanger(self, pos):
        return self.pointAtPosIsInValues(pos, strToLst('NESW'))

    def createMap(self):
        self.map = []
        nbRows, _ = [int(x) for x in raw_input().split()]
        for _ in xrange(nbRows):
            self.map.append(strToLst(raw_input()))

        self.moveTo(self.findStartPoint())

    def findSymbol(self, symbol, mapToSearch=None):
        if mapToSearch is None:
            mapToSearch = self.map

        for y, line in enumerate(mapToSearch):
            for x, point in enumerate(line):
                if point == symbol:
                    return Pos(x, y)

    def findOtherTeleporter(self, posFirstTeleporter):
        # Remove the first teleporter from the map
        virtualMap = deepcopy(self.map)
        virtualMap[posFirstTeleporter.y()][posFirstTeleporter.x()] = ' '
        # Search for the other teleporter in the map
        return self.findSymbol('T', virtualMap)

    def findStartPoint(self):
        return self.findSymbol('@')

    def findFinalPoint(self):
        return self.findSymbol('$')


class Solution(object):
    def __init__(self, myMap):
        super(Solution, self).__init__()
        self.map = myMap
        self.moves = []

    def makeNextMove(self, nextPos, direction):
        self.map.moveTo(nextPos)
        self.moves.append(normalizeDirection(direction))

    def printMoves(self):
        return '\n'.join(self.moves)

    def solve(self):
        nbMoves = 1
        maxMoves = 200
        while self.map.getCurrentPos() != self.map.findFinalPoint() and nbMoves <= maxMoves:
            # Initialization for the first move
            if nbMoves == 1:
                direction, nextPos = self.map.nextPosition()
            # Keep the old direction when moving
            else:
                nextPos = self.map.getCurrentPos().toDirection(direction)

            # We stepped on a path modifier
            if self.map.isDirectionChanger(self.map.getCurrentPos()):
                direction = self.map.pointAtPos(self.map.getCurrentPos())
                nextPos = self.map.getCurrentPos().toDirection(direction)

            # We hit an unbreakable obstacle, get the next direction
            while (self.map.isObstacle(nextPos) and not self.map.breaker) or (self.map.isBorder(nextPos)):
                direction, nextPos = self.map.nextPosition()

            self.makeNextMove(nextPos, direction)
            nbMoves += 1

        # Check if we've reached the target
        if self.map.getCurrentPos() == self.map.findFinalPoint():
            print self.printMoves()
        # Otherwise, we are trapped in a loop
        else:
            print 'LOOP'


sol = Solution(Map())
sol.solve()
