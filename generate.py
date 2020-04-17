import numpy as np

class SudokuGenerate():
    """method for generating sudokus"""
    def __init__(self):
        pass

    def generate(self, zeros):
        grid = np.zeros((9,9))
        grid = self.solveRandom(grid)
        grid = self.removeRandomNumbers(zeros, grid)
        return grid

    def removeRandomNumbers(self, zeros, grid):
        if zeros >= 81:
            zeros = 81
        for zero in range(zeros):
            row = np.random.randint(low = 0, high = 9)
            column = np.random.randint(low = 0, high = 9)
            while grid[row][column] == 0:
                row = np.random.randint(low = 0, high = 9)
                column = np.random.randint(low = 0, high = 9)
            grid[row][column] = 0
        return grid

    def solveRandom(self, grid):
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 0:
                    for number in range(1, 10):
                        number = np.random.randint(low=1, high=10)
                        usedNumbers = self.sumNumber(self.getRowNumbers(row, column, grid), self.getColumnNumbers(row, column, grid), self.getSquareNumbers(row, column, grid))
                        if not number in usedNumbers:
                            grid[row][column] = number 
                            
                            if self.solveRandom(grid) is not False:
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