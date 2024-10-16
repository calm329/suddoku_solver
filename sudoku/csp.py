class CSP:
    def __init__(self, initBoard):
        self.board = {}
        self.domain = {}
        self.constraints = []
        self.rows = "ABCDEFGHI"
        self.columns = "123456789"
        
        # Initialize the board
        for r_idx, r in enumerate(self.rows):
            for c_idx, c in enumerate(self.columns):
                cell = r + c
                value = initBoard[r_idx][c_idx]
                self.board[cell] = value
                
                # Domain is all possible values [1-9] if the cell is not filled
                if value == 0:
                    self.domain[cell] = list(range(1, 10))
                else:
                    self.domain[cell] = [value]

        # Constraints: all cells in the same row, column, or 3x3 grid must be different
        self.create_constraints()
        
    def create_constraints(self):
        # Add row constraints
        for r in self.rows:
            for c1 in self.columns:
                for c2 in self.columns:
                    if c1 != c2:
                        self.constraints.append((r + c1, r + c2))

        # Add column constraints
        for c in self.columns:
            for r1 in self.rows:
                for r2 in self.rows:
                    if r1 != r2:
                        self.constraints.append((r1 + c, r2 + c))

        # Add 3x3 grid constraints
        for box_row in ('ABC', 'DEF', 'GHI'):
            for box_col in ('123', '456', '789'):
                for r1 in box_row:
                    for c1 in box_col:
                        for r2 in box_row:
                            for c2 in box_col:
                                if r1 + c1 != r2 + c2:
                                    self.constraints.append((r1 + c1, r2 + c2))
