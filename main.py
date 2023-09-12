from graphics import Window, Line, Point
from Cell import Cell

def main():
    win = Window(800, 600)

    win.draw_line(Line(Point(10,20), Point(790, 10)), "black")
    win.draw_line(Line(Point(10,20), Point(10, 590)), "black")

    cell1 = Cell(win,)
    cell2 = Cell(win)
    cell3 = Cell(win)

    cell1.draw(10, 10, 30)
    cell2.draw(100, 100, 30)
    cell3.draw(300, 100, 30)
    
    win.wait_for_close()

main()
