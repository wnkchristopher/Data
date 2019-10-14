from Matrix_pb2 import ProtoMatrix
from Matrix_pb2 import ProtoSquare
import Matrix_pb2

class MatrixTransmitter:
    def __init__(self, squareMatrix):
        # create empty matrix
        self.protoMatrix = Matrix_pb2.ProtoMatrix()
        self.convertData(squareMatrix)

        quotesFile = open("puzzle_unsolved.bin", "wb")
        quotesFile.write(self.protoMatrix.SerializeToString())
        quotesFile.close()

    def convertData(self, squareMatrix):
        self.protoMatrix.size = squareMatrix.size

        for square in squareMatrix.getAllSquares():
            self.addSquare(square)

    def addSquare(self, square):
        protoSquare = self.protoMatrix.squares.add()
        protoSquare.value = square.getValue()
        protoSquare.position.x = square.getX()
        protoSquare.position.y = square.getY()
        self.addNeighbours(square.getNeighbours(), protoSquare)
        self.addNotNeighbours(square.getNotNeighbours(), protoSquare)

    def addNeighbours(self, neighbours, protoSquare):
        for neighbour in neighbours:
            protoNeighbour = protoSquare.neighbours.add()
            protoNeighbour.x = neighbour[0]
            protoNeighbour.y = neighbour[1]

    def addNotNeighbours(self, notNeighbours, protoSquare):
        for notNeighbour in notNeighbours:
            protoNotNeighbour = protoSquare.notNeighbours.add()
            protoNotNeighbour = notNeighbour[0]
            protoNotNeighbour = notNeighbour[1]
