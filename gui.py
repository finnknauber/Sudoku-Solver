import numpy as np
import pygame
from solve import SudokuSolver
from field import SudokuField
from generate import SudokuGenerate


class SudokuGUI():
    def __init__(self):
        pass

    def paintGrid(self):
        blockSize = 70 # Set the size of the grid block
        for row in range(9):
            for column in range(9):
                rect = pygame.Rect(row*blockSize, column*blockSize, blockSize, blockSize)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

    def drawNumber(self, number, row, column):
        myFont = pygame.font.SysFont("Arial", 80)
        randNumLabel = myFont.render(str(int(number)), 1, (0, 0, 0))
        self.screen.blit(randNumLabel, (column*70+15, row*70-10))

    def printNumbers(self, grid):
        self.screen.fill((255, 255, 255))
        self.paintGrid()
        for row in range(9):
            for column in range(9):
                number = grid[row][column]
                if not number == 0:
                    self.drawNumber(number, row, column)
        pygame.display.flip()

                
    def display(self, zeros, gui):
        solver = SudokuSolver()
        field = SudokuField(zeros)
        generator = SudokuGenerate()
        grid = field.getField()
        pygame.init()
        self.screen = pygame.display.set_mode((630, 630))
        pygame.display.set_caption("Sudoku Solver")
        pygame.mouse.set_visible(1)
        pygame.key.set_repeat(1, 30)
        clock = pygame.time.Clock()
        pygame.key.set_repeat(100)

        self.screen.fill((255, 255, 255))

        self.paintGrid()
        self.printNumbers(grid)

        # game runs while running is true
        running = True
        while running:
            # game runs at 30 frames 
            clock.tick(30)

            # event handling
            for event in pygame.event.get():
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    self.screen.fill((255, 255, 255))
                    field.generate(generator, zeros)
                    grid = field.getField()
                    self.paintGrid()
                    self.printNumbers(grid)

                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    grid = solver.solve(field, gui)
                    self.printNumbers(grid)

                # if quit stop the game
                if event.type == pygame.QUIT:
                    running = False

            # show display
            pygame.display.flip()