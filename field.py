import numpy as np
import copy
from generate import SudokuGenerate

class SudokuField():
    "stores sudoku field and has methods for getting parts of the field"
    def __init__(self, zeros):
        sg = SudokuGenerate()
        self.generate(sg, zeros)

    def generate(self, generator, zeros):
        self._grid = generator.generate(zeros)
    
    def changeGrid(self, row, column, value):
        self._grid[row][column] = value

    def printField(self):
        for row in range(len(self._grid)):
            prettyRow = ""
            for number in range(len(self._grid[row])):
                if (number+1) % 3 == 0:
                    prettyRow = prettyRow + str(int(self._grid[row][number]))
                    prettyRow = prettyRow + " | "
                else:
                    prettyRow = prettyRow + str(int(self._grid[row][number])) + " "
            if (row) % 3 == 0:
                print("-------------------------")
            prettyRow = prettyRow[:-2]+"| "
            print("| "+prettyRow)
        print("-------------------------")
        
    def getField(self):
        newGrid = copy.deepcopy(self._grid)
        return newGrid

    def getRowNumbers(self, row, column, grid=None):
        if grid is None:
            grid = self._grid
        rowNumbers = grid[row]
        newRowNumbers = []
        for number in range(len(rowNumbers)):
            if grid[row][number] > 0:
                newRowNumbers = np.append(newRowNumbers, grid[row][number])
        return newRowNumbers

    def getColumnNumbers(self, row, column, grid=None):
        if grid is None:
            grid = self._grid
        columnNumbers = []
        for rowArray in grid:
            if rowArray[column] > 0:
                columnNumbers = np.append(columnNumbers, rowArray[column])
        return columnNumbers

    def getSquareNumbers(self, row, column, grid=None):
        if grid is None:
            grid = self._grid
        squareNumbers = []
        column = column // 3 * 3
        row = row // 3 * 3
        for rowNumber in range(3):
            for columnNumber in range(3):
                if grid[rowNumber+row][columnNumber+column] > 0:
                    squareNumbers = np.append(squareNumbers, grid[rowNumber+row][columnNumber+column])

        return squareNumbers
