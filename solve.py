import numpy as np
import copy

class SudokuSolver():
    "solves the sudoku"
    def __init__(self):
        pass

    def solve(self, field, gui):
        fieldArray = field.getField()
        grid = self.solveStep(field, fieldArray, gui)
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                field.changeGrid(row, column, grid[row][column])

        return grid

          

    def solveStep(self, field, grid, gui):
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 0:
                    for number in range(1, 10):
                        usedNumbers = self.sumNumber(field.getRowNumbers(row, column, grid), field.getColumnNumbers(row, column, grid), field.getSquareNumbers(row, column, grid))
                        if not number in usedNumbers:
                            gui.printNumbers(grid)
                            grid[row][column] = number 

                            if self.solveStep(field, grid, gui) is not False:
                                return grid
                            
                            grid[row][column] = 0
                    return False
        return grid

    def sumNumber(self, rowNumbers, columnNumbers, squareNumbers):
        sumNumber = []
        sumNumber = np.append(sumNumber, rowNumbers)
        sumNumber = np.append(sumNumber, columnNumbers)
        sumNumber = np.append(sumNumber, squareNumbers)
        return sumNumber
