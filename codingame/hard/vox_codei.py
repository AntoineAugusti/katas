import sys
import math

# width: width of the firewall grid
# height: height of the firewall grid
width, height = [int(i) for i in raw_input().split()]
grid = []
for i in xrange(height):
    grid.append(list(raw_input()))  # one line of the firewall grid


def bomb_positions(grid):
    res = []
    for i, line in enumerate(grid):
        for j, e in enumerate(line):
            if e == '@':
                res.append((i, j))
    return res

bombs_pos = bomb_positions(grid)
print >> sys.stderr, bombs_pos
print >> sys.stderr, grid

while True:
    # rounds: number of rounds left before the end of the game
    # bombs: number of bombs left
    rounds, bombs = [int(i) for i in raw_input().split()]

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    if bombs > 0:
        to_nuke = bombs_pos.pop()
        print "%i %i" % (to_nuke[0], to_nuke[1]+1)
    else:
        print "WAIT"
