from src.Read import Read
from src.PythonEncoder import MatrixTransmitter
from src.SquareMatrix import SquareMatrix

reader = Read("puzzle_unsolved.txt")
matrices = reader.getMatrices()

transmitter = MatrixTransmitter(matrices)