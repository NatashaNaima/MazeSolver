from graphics import Line, Point

class Cell:
    def __init__(self, win = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.topY = None
        self.bottomY = None
        self.leftX = None
        self.rightX = None
        self.win = win
    
    def draw(self, cornerX, cornerY, size):
        self.topY = cornerY
        self.bottomY = cornerY + size
        self.leftX = cornerX
        self.rightX = cornerX + size

        lWall = Line(Point(self.leftX, self.topY), Point(self.leftX, self.bottomY))
        if self.has_left_wall:
            self.win.draw_line(lWall, "black")
        else:
            self.win.draw_line(lWall, "white")

        rWall = Line(Point(self.rightX, self.topY), Point(self.rightX, self.bottomY))    
        if self.has_right_wall:
            self.win.draw_line(rWall, "black")
        else:
            self.win.draw_line(rWall, "white")

        tWall = Line(Point(self.leftX, self.topY), Point(self.rightX, self.topY))
        if self.has_top_wall:
            self.win.draw_line(tWall, 'black')
        else:
            self.win.draw_line(tWall, 'white')

        bWall = Line(Point(self.leftX, self.bottomY), Point(self.rightX, self.bottomY))
        if self.has_bottom_wall:
            self.win.draw_line(bWall, "black")
        else:
            self.win.draw_line(bWall, "white")
    
    def draw_move(self, to_cell, undo=False):
        start = Point(self.leftX + (self.rightX - self.leftX)//2,self.topY + (self.bottomY - self.topY)//2)
        end = Point(to_cell.leftX + (to_cell.rightX - to_cell.leftX)//2,to_cell.topY + (to_cell.bottomY - to_cell.topY)//2)
        path = Line(start, end)
        if undo:
            self.win.draw_line(path, "grey")
        else:
            self.win.draw_line(path, "red")

    

     