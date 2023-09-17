from Cell import Cell
from graphics import Point

import time

class Maze:
    def __init__(
            self,
            x,
            y,
            num_rows,
            num_cols,
            cell_size,
            win = None
    ):
        self.topLeftCorner = Point(x,y)
        self.cells = []
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self.win = win

        self.create_cells()

    def create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self.cells.append(col_cells)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cell(i,j)
        

    def draw_cell(self, i, j):
        if self.win is None:
            return
        
        x1 = self.topLeftCorner.x + i * self.cell_size
        y1 = self.topLeftCorner.y + j * self.cell_size

        self.cells[i][j].draw(x1, y1, self.cell_size)
        self.animate()

    def animate(self):
        if self.win is None: 
            return
        self.win.redraw()
        time.sleep(0.05)
    

