nbPlaces, nbRuns, nbGroups = [int(i) for i in raw_input().split()]
groups = []
for _ in xrange(nbGroups):
    groups.append(int(raw_input()))

earnings = 0
posCounter = 0
for _ in xrange(nbRuns):
    capacity = nbPlaces
    nbGroupsIn = 0
    while capacity >= groups[posCounter]:
        nbGroupsIn += 1
        # Every group is aboard, skip that
        if (nbGroupsIn > nbGroups):
            break
        # Get the money
        earnings += groups[posCounter]
        # Decrease the number of available spots
        capacity -= groups[posCounter]
        # Move on to the next group
        posCounter += 1
        # Reset the pos counter of the list if we went too far
        if (posCounter >= nbGroups):
            posCounter = 0

print earnings
