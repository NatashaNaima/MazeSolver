import unittest
from maze import Maze

class Tests(unittest.TestCase):
    # cell creation tests
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10)
        self.assertEqual(
            len(m1.cells),
            num_rows,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols,
        )
    
    def test_maze_not_created_with_no_row(self):
        num_cols = 10
        num_rows = 0
        m2 = Maze(0, 0, num_rows, num_cols, 10)

        self.assertEqual(
            len(m2.cells),
            0
        )

    def test_maze_not_created_with_no_col(self):
        num_cols = 0
        num_rows = 10
        m3 = Maze(0, 0, num_rows, num_cols, 10)

        self.assertEqual(
            len(m3.cells),
            0
        )
    
    # drawing tests
    def test_maze_draws_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10)

        self.assertFalse(
            m1.cells[0][0].has_left_wall
        )

        self.assertFalse(
            m1.cells[9][11].has_right_wall
        )

if __name__ == "__main__":
    unittest.main()