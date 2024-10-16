import unittest
from sudoku.solver import solve_sudoku
from sudoku.utils import parse_grid

class TestSudokuSolver(unittest.TestCase):
    def test_easy_puzzle(self):
        puzzle = (
            "53..7...." +
            "6..195..." +
            ".98....6." +
            "8...6...3" +
            "4..8.3..1" +
            "7...2...6" +
            ".6....28." +
            "...419..5" +
            "....8..79"
        )
        grid = parse_grid(puzzle)
        solution = solve_sudoku(grid)
        self.assertIsNotNone(solution)
        # Check if all cells are filled
        for row in solution:
            for cell in row:
                self.assertNotEqual(cell, 0)

    def test_unsolvable_puzzle(self):
        # An invalid puzzle that cannot be solved
        puzzle = (
            "53..7...." +
            "6..195..." +
            ".98....6." +
            "8...6...3" +
            "4..8.3..1" +
            "7...2...6" +
            ".6....28." +
            "...419..5" +
            "....8..78"  # Invalid row with duplicate '8'
        )
        grid = parse_grid(puzzle)
        solution = solve_sudoku(grid)
        self.assertIsNone(solution)

    def test_already_solved_puzzle(self):
        # A puzzle that is already solved
        puzzle = (
            "534678912" +
            "672195348" +
            "198342567" +
            "859761423" +
            "426853791" +
            "713924856" +
            "961537284" +
            "287419635" +
            "345286179"
        )
        grid = parse_grid(puzzle)
        solution = solve_sudoku(grid)
        self.assertEqual(grid, solution)

if __name__ == "__main__":
    unittest.main()
