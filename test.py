import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )
    
    def test_maze_not_created_with_no_col(self):
        num_cols = 0
        num_rows = 10
        m2 = Maze(0, 0, num_rows, num_cols, 10)

        self.assertEqual(
            len(m2.cells),
            num_cols,
        )
        with self.assertRaises(IndexError):
            m2.cells[0]

    def test_maze_not_created_with_no_row(self):
        num_cols = 10
        num_rows = 0
        m3 = Maze(0, 0, num_rows, num_cols, 10)

        self.assertEqual(
            len(m3.cells),
            num_cols,
        )
        self.assertEqual(
            len(m3.cells[0]),
            num_rows,
        )
        for i in range(num_cols):
            with self.assertRaises(IndexError):
                m3.cells[i][0]
        

if __name__ == "__main__":
    unittest.main()