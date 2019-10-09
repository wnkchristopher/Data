class Square:
   # neighbours = []
    def __init__(self, xCoord, yCoord, value, notNeighbours):
        self.x = xCoord
        self.y = yCoord
        self.value = value
        self.notNeighbours = notNeighbours
        self.neighbours = []

    def addNeighbour(self, x, y):
        neighbour = [x, y]
        self.neighbours.append(neighbour)
        self.removeNotNeighbour(x, y)

    def setValue(self, value):
        self.value = value

    def removeNotNeighbour(self, x, y):
        i = self.notNeighbours.remove([x,y])


