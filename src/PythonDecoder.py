import solvedPuzzle_pb2
import sys

from src.Square import Square
from src.SquareMatrix import SquareMatrix


class WriteSolvedPuzzle:
    def __init__(self):
        protoPuzzles = solvedPuzzle_pb2.Solutions()

        f = open("puzzle_solved.bin", "rb")
        protoPuzzles.ParseFromString(f.read())
        f.close()

        self.createTextFile(protoPuzzles)

    def createTextFile(self, protoPuzzles):
        f = open("../puzzle_solved.txt", "w+")
        output = ""
        quantity = protoPuzzles.numberOfPuzzles
        output = "puzzles " + str(quantity) + "\n"

        for puzzle in protoPuzzles.puzzles:
            strPuzzle = "size " + str(puzzle.size) + "x" + str(puzzle.size) + "\n"
            squareMatrix = SquareMatrix(puzzle.size)
            squareMatrix.allSquares = []
            for square in puzzle.squares:
                squareMatrix.addSquare(square.x, square.y, square.value)
            for y in range(1, puzzle.size+1):
                for x in range(1, puzzle.size+1):
                    strPuzzle += str(squareMatrix.getSquare(x, y).getValue()) + " "
                strPuzzle+="\n"
            output += strPuzzle



        f.write(output)
        f.close()

solvedMatrix = WriteSolvedPuzzle()