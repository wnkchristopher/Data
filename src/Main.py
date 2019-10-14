from src.Read import Read
from src.MatrixTransmitter import MatrixTransmitter
from src.SquareMatrix import SquareMatrix

reader = Read("puzzle_unsolved.txt")
matrix = reader.getMatrix()

transmitter = MatrixTransmitter(matrix)