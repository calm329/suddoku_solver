from sudoku.csp import CSP
from sudoku.ac3 import ac3
from sudoku.backtracking import backtrack

def solve_sudoku(grid):
    csp = CSP(grid)
    if ac3(csp):
        success, assignment = backtrack({}, csp)
        if success:
            # Convert the assignment (which is a dictionary) to a 2D list
            solved_board = [[0] * 9 for _ in range(9)]
            for cell, value in assignment.items():
                r_idx = ord(cell[0]) - ord('A')
                c_idx = int(cell[1]) - 1
                solved_board[r_idx][c_idx] = value
            return solved_board
    return None

