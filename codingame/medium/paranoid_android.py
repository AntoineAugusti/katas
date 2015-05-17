class Elevator(object):
    def __init__(self, floor, pos):
        super(Elevator, self).__init__()
        self.floor = floor
        self.pos = pos
        self.direction = None

    def __str__(self):
        return 'Elevator on floor %i (pos %i) with dir %s' % (self.floor, self.pos, self.direction)


class Game(object):
    def __init__(self, nbFloors, width, exitFloor, exitPos, nbElevators):
        super(Game, self).__init__()
        self.nbFloors = nbFloors
        self.width = width
        self.exitFloor = exitFloor
        self.exitPos = exitPos
        self.nbElevators = nbElevators
        self.elevators = [0] * nbFloors

    def addElevators(self):
        for _ in xrange(self.nbElevators):
            # elevatorFloor: floor on which this elevator is found
            # elevatorPos: position of the elevator on its floor
            elevatorFloor, elevatorPos = [int(j) for j in raw_input().split()]
            self.elevators[elevatorFloor] = Elevator(elevatorFloor, elevatorPos)
        # Don't forget to add the elevator leading to the exit
        self.elevators[self.exitFloor] = Elevator(self.exitFloor, self.exitPos)

    def setElevatorsDirections(self):
        for i in range(self.nbFloors - 1):
            if (self.elevators[i].pos > self.elevators[i+1].pos):
                self.elevators[i+1].direction = 'LEFT'
            else:
                self.elevators[i+1].direction = 'RIGHT'


# nbFloors: number of floors
# width: width of the area
# nbRounds: maximum number of rounds
# exitFloor: floor on which the exit is found
# exitPos: position of the exit on its floor
# nbTotalClones: number of generated clones
# nbAdditionalElevators: ignore (always zero)
# nbElevators: number of elevators
nbFloors, width, nbRounds, exitFloor, exitPos, nbTotalClones, nbAdditionalElevators, nbElevators = [int(i) for i in raw_input().split()]

game = Game(nbFloors, width, exitFloor, exitPos, nbElevators)
game.addElevators()
game.setElevatorsDirections()

firstRound = True
# Game loop
while True:
    # cloneFloor: floor of the leading clone
    # clonePos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    cloneFloor, clonePos, direction = raw_input().split()
    cloneFloor = int(cloneFloor)
    clonePos = int(clonePos)

    if firstRound:
        firstRound = False
        if (clonePos < game.elevators[0].pos):
            game.elevators[0].direction = 'RIGHT'
        else:
            game.elevators[0].direction = 'LEFT'

    if cloneFloor == -1:
        print 'WAIT'
    else:
        if direction == game.elevators[cloneFloor].direction:
            print 'WAIT'
        else:
            print 'BLOCK'
