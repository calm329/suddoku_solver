def parse_grid(grid_string):
    """Parses a grid string into a 2D list of integers."""
    return [[int(c) if c != '.' else 0 for c in grid_string[i:i + 9]] for i in range(0, 81, 9)]

def print_sudoku(grid):
    """Prints the Sudoku board in a readable format."""
    for r in range(9):
        if r in (3, 6):  # Print horizontal separator
            print("-" * 21)
        for c in range(9):
            if c in (3, 6):  # Print vertical separator
                print("|", end=" ")
            print(grid[r][c] if grid[r][c] != 0 else ".", end=" ")
        print()
