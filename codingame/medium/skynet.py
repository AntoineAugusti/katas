from sys import stderr
from collections import defaultdict


def readLinks(nbLinks):
    # Read relationships between nodes
    links = defaultdict(list)

    for i in xrange(nbLinks):
        # N1 and N2 defines a link between these nodes
        # The graph is not oriented
        N1, N2 = [int(i) for i in raw_input().split()]
        links[N1].append(N2)
        links[N2].append(N1)

    return links


def readExits(nbExits):
    # Read the position of the exits
    exits = []

    for i in xrange(nbExits):
        # The index of a gateway node
        EI = int(raw_input())
        exits.append(EI)

    return exits

# N: the total number of nodes in the level, including the gateways
# L: the number of links
# E: the number of exit gateways
N, L, E = [int(i) for i in raw_input().split()]

links = readLinks(L)
exits = readExits(E)

print >> stderr, "links: ", links
print >> stderr, "exits: ", exits

# Game loop
while True:
    # The index of the node on which the Skynet agent is positioned this turn
    SI = int(raw_input())

    # Try to destroy a link connecting the current position
    # of the Skynet agent to an exit
    command = None
    for exit in exits:
        if exit in links[SI]:
            command = "%d %d" % (SI, exit)

    # If we haven't found a direct link, nuke another link
    if command is None:
        for exit in exits:
            # Best guess: a link leading to an exit
            if len(links[exit]) > 0:
                command = "%d %d" % (exit, links[exit].pop())
                break
            # Just remove a link where the starting point
            # is the Skynet's position
            elif len(links[SI]) > 0:
                command = "%d %d" % (SI, links[SI].pop())
                break

    print command
