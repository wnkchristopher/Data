import solvedPuzzle_pb2
import sys

class WriteSolvedPuzzle:
    def __init__(self):
        matrix = solvedPuzzle_pb2.Puzzle()

        f = open("puzzle_solved.bin", "rb")
        matrix.ParseFromString(f.read())
        f.close()

        self.createTextFile(matrix.puzzle)

    def createTextFile(self, puzzle):
        f = open("../puzzle_solved.txt", "w+")
        f.write(puzzle)
        f.close()

solvedMatrix = WriteSolvedPuzzle()