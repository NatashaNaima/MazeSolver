from graphics import Line, Point

class Cell:
    def __init__(self, win) -> None:
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
        if self.has_left_wall:
            wall = Line(Point(self.leftX, self.topY), Point(self.leftX, self.bottomY))
            self.win.draw_line(wall, "black")
        if self.has_right_wall:
            wall = Line(Point(self.rightX, self.topY), Point(self.rightX, self.bottomY))
            self.win.draw_line(wall, "black")
        if self.has_top_wall:
            wall = Line(Point(self.leftX, self.topY), Point(self.rightX, self.topY))
            self.win.draw_line(wall, 'black')
        if self.has_top_wall:
            wall = Line(Point(self.leftX, self.bottomY), Point(self.rightX, self.bottomY))
            self.win.draw_line(wall, "black")
        
     