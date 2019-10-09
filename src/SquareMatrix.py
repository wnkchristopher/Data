from src.Square import Square


class SquareMatrix:
    allSquares = []

    def __init__(self, size):
        self.size = size
        for x in range(1, size + 1):
            for y in range(1, size + 1):
                self.addSquare(x, y, -1)

    def addSquare(self, x, y, value):
        listNotNeighbours = []
        if self.isValidCoordinates(x - 1, y):
            listNotNeighbours.append([x - 1, y])
        if self.isValidCoordinates(x + 1, y):
            listNotNeighbours.append([x + 1, y])
        if self.isValidCoordinates(x, y - 1):
            listNotNeighbours.append([x, y - 1])
        if self.isValidCoordinates(x, y + 1):
            listNotNeighbours.append([x, y + 1])

        square = Square(x, y, value, listNotNeighbours)
        self.allSquares.append(square)

    def getSquare(self, x, y) -> Square:
        for s in self.allSquares:
            if s.x == x and s.y == y:
                return s

    def isValidCoordinates(self, x, y):
        if 0 < x <= self.size and 0 < y <= self.size:
            return True
        return False

    def printIt(self):
        for y in range(1, self.size + 1):
            s = ""
            for x in range(1, self.size + 1):
                square = self.getSquare(x,y)
                s = s + str(square.value) + "(" + str(len(square.neighbours)) + ")    "
            print(s)
            print("--------------------------------------")
