from Matrix_pb2 import ProtoMatrix
from Matrix_pb2 import ProtoSquare
import Matrix_pb2

class MatrixTransmitter:
    def __init__(self, allMatrices):

        self.protoMatrices = Matrix_pb2.ProtoAllMatrices()
        self.convertData(allMatrices)

        quotesFile = open("puzzle_unsolved.bin", "wb")
        quotesFile.write(self.protoMatrices.SerializeToString())
        quotesFile.close()

    def convertData(self, allMatrices):
        self.protoMatrices.quantity = len(allMatrices)

        for matrix in allMatrices:
            self.addMatrix(matrix)


    def addMatrix(self, matrix):
        protoMatrix = self.protoMatrices.matrices.add()
        protoMatrix.size = matrix.getSize()
        for square in matrix.getAllSquares():
            self.addSquare(square, protoMatrix)

    def addSquare(self, square, protoMatrix):
        protoSquare = protoMatrix.squares.add()
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
            protoNotNeighbour.x = notNeighbour[0]
            protoNotNeighbour.y = notNeighbour[1]
