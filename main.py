from graphics import Window
from maze import Maze

def main():

    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size = (screen_x - 2 * margin) / num_cols
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size, win)

    win.wait_for_close()

main()
