from src.SquareMatrix import SquareMatrix
from src.Square import Square


class Read:

    def __init__(self, filename):
        self.readFile(filename)
        self.matrix.printIt()

    def readFile(self, filename):
        f = open("../" + filename, "r")
        content = f.read()
        lines = content.splitlines()
        size = int(lines[1].split("x")[1])
        self.matrix = SquareMatrix(size)
        i = 0
        y = 0
        for s in lines:
            if(i<2):
                i += 1
                continue

            if i % 2 == 0:
                y += 1
                self.addNumberLine(s, y)
            else:
                self.addNeighbourLine(s, y)
            i += 1


    def addNumberLine(self, line, y):
        splitLine = line.split(" ")
        x = 1
        for char in splitLine:
            if char == "_":
                x += 1
            elif char.isnumeric():
                self.matrix.getSquare(x, y).setValue(int(char))
                x += 1
            elif char == "x":
                self.matrix.getSquare(x-1, y).addNeighbour(x, y)
                self.matrix.getSquare(x, y).addNeighbour(x-1, y)


    def addNeighbourLine(self, line, y):
        chars = line[::4]
        x = 1
        for c in chars:
            if(c == "x"):
                self.matrix.getSquare(x, y).addNeighbour(x, y+1)
                self.matrix.getSquare(x, y+1).addNeighbour(x, y)
            x += 1