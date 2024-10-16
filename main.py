from sudoku.solver import solve_sudoku
from sudoku.utils import parse_grid, print_sudoku

def read_puzzles_from_file(filename):
    """Reads Sudoku puzzles from the specified file and returns them as a list."""
    puzzles = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):  # Skip empty lines and comments
                puzzles.append(line)
    return puzzles

if __name__ == "__main__":
    # Read puzzles from sample_puzzles.txt file
    puzzles = read_puzzles_from_file("examples/sample_puzzles.txt")

    # Solve each puzzle
    for i, puzzle in enumerate(puzzles):
        print(f"Sudoku Puzzle {i + 1}:")
        grid = parse_grid(puzzle)
        print("Original Sudoku Puzzle:")
        print_sudoku(grid)

        # Solve the puzzle
        solution = solve_sudoku(grid)
        if solution:
            print("\nSolved Sudoku Puzzle:")
            print_sudoku(solution)
        else:
            print("No solution exists.")
        print("\n" + "=" * 30 + "\n")
