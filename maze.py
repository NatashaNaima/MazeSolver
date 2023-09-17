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
        for row in range(self.num_rows):
            row_cells = []
            for col in range(self.num_cols):
                row_cells.append(Cell(self.win))
            self.cells.append(row_cells)
        
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.draw_cell(row,col)
        

    def draw_cell(self, row, col):
        if self.win is None:
            return
        
        x1 = self.topLeftCorner.x + col * self.cell_size
        y1 = self.topLeftCorner.y + row * self.cell_size

        self.cells[row][col].draw(x1, y1, self.cell_size)
        self.animate()

    def animate(self):
        if self.win is None: 
            return
        self.win.redraw()
        time.sleep(0.05)
    
    def break_entrance_and_exit(self):
        pass

    def break_wall(self, row, col, wall):
        cell = self.cells[row][col]

        if wall == 'left':
            cell.has_left_wall = False
            if col not in range(1,self.num_cols):
                self.cells[row][col-1].has_right_wall = False

        if wall == 'top':
            cell.has_top_wall = False
            if row not in range(1, self.num_rows):
                self.cells[row-1][col].has_bottom_wall = False

        if wall == 'right':
            cell.has_right_wall = False
            if col not in range(1,self.num_cols):
                self.cells[row][col+1].has_left_wall = False

        if wall == 'bottom':
            cell.has_bottom_wall = False
            if row not in range(0, self.num_rows-1):
                self.cells[row+1][col].has_top_wall = False 

