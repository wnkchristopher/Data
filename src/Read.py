from src.SquareMatrix import SquareMatrix
from src.Square import Square


class Read:

    def __init__(self, filename):
        self.allMatrices = []
        self.readFile(filename)

    def readFile(self, filename):
        f = open("../" + filename, "r")
        content = f.read()

        puzzles = content.split("size ")
        print("")

        for puzzle in puzzles[1:]:
            lines = puzzle.splitlines()
            size = int(lines[0].split("x")[1])
            matrix = SquareMatrix(size)
            i = 0
            y = 0
            for s in lines:
                if(i<1):
                    i += 1
                    continue

                if i % 2 == 1:
                    y += 1
                    self.addNumberLine(s, y, matrix)
                else:
                    self.addNeighbourLine(s, y, matrix)
                i += 1
            self.allMatrices.append(matrix)


    def addNumberLine(self, line, y, matrix:SquareMatrix):
        splitLine = line.split(" ")
        x = 1
        for char in splitLine:
            if char == "_":
                x += 1
            elif char.isnumeric():
                matrix.getSquare(x, y).setValue(int(char))
                x += 1
            elif char == "x":
                matrix.getSquare(x-1, y).addNeighbour(x, y)
                matrix.getSquare(x, y).addNeighbour(x-1, y)


    def addNeighbourLine(self, line, y, matrix:SquareMatrix):
        chars = line[::4]
        x = 1
        for c in chars:
            if(c == "x"):
                matrix.getSquare(x, y).addNeighbour(x, y+1)
                matrix.getSquare(x, y+1).addNeighbour(x, y)
            x += 1

    def getMatrices(self):
        return self.allMatrices