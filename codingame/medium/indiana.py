def exitDirection(roomType, enterPos):
    if roomType in [1, 3, 7, 8, 9, 12, 13]:
        return 'BOTTOM'
    if roomType in [2, 6]:
        if enterPos == 'LEFT':
            return 'RIGHT'
        else:
            return 'LEFT'
    if roomType == 4:
        if enterPos == 'TOP':
            return 'LEFT'
        else:
            return 'BOTTOM'
    if roomType == 5:
        if enterPos == 'TOP':
            return 'RIGHT'
        else:
            return 'BOTTOM'
    if roomType == 10:
        return 'LEFT'
    if roomType == 11:
        return 'RIGHT'


def coordExit(startX, startY, direction):
    if direction == 'BOTTOM':
        return (startX, startY + 1)
    elif direction == 'RIGHT':
        return (startX + 1, startY)
    else:
        return (startX - 1, startY)


width, height = [int(i) for i in raw_input().split()]
roomsTypes = []
for _ in xrange(height):
    # Represents a line in the grid and contains "width" integers.
    # Each integer represents one room of a given type.
    roomsTypes.append([int(i) for i in raw_input().split()])
# The coordinate along the X axis of the exit (not useful for this first mission, but must be read).
exitPos = int(raw_input())

while True:
    x, y, pos = raw_input().split()
    x = int(x)
    y = int(y)

    xNext, yNext = coordExit(x, y, exitDirection(roomsTypes[y][x], pos))
    print "%i %i" % (xNext, yNext)
