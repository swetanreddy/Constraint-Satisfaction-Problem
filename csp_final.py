class SudokuSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def solve(self):
        if self._solve_sudoku():
            return self.puzzle
        else:
            return None

    def _find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    return i, j
        return None

    def _valid(self, num, pos):
        # Check row
        for i in range(9):
            if self.puzzle[pos[0]][i] == num:
                return False

        # Check column    
        for i in range(9):
            if self.puzzle[i][pos[1]] == num:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.puzzle[i][j] == num:
                    return False

        return True

    def _solve_sudoku(self):
        pos = self._find_empty()

        if not pos:
            return True

        row, col = pos

        for num in range(1, 10):
            if self._valid(num, (row, col)):
                self.puzzle[row][col] = num

                if self._solve_sudoku():
                    return True

                self.puzzle[row][col] = 0

        return False
    
def print_sudoku(grid):
    for row in grid:
        for elem in row:
            print(elem, end=" ")
        print()
    print("\n")


# Example Usage:
if __name__ == "__main__":
    easy_puzzle = [
        [6, 0, 8, 7, 0, 2, 1, 0, 0],
        [4, 0, 0, 0, 1, 0, 0, 0, 2],
        [0, 2, 5, 4, 0, 0, 0, 0, 0],
        [7, 0, 1, 0, 8, 0, 4, 0, 5],
        [0, 8, 0, 0, 0, 0, 0, 7, 0],
        [5, 0, 9, 0, 6, 0, 3, 0, 1],
        [0, 0, 0, 0, 0, 6, 7, 5, 0],
        [2, 0, 0, 0, 9, 0, 0, 0, 8],
        [0, 0, 6, 8, 0, 5, 2, 0, 3],    
    ]

    hard_puzzle = [
        [0, 7, 0, 0, 4, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 6, 1, 0],
        [3, 9, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 4, 0, 0, 9],
        [0, 0, 3, 0, 0, 0, 7, 0, 0],
        [5, 0, 0, 1, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 7, 6],
        [0, 5, 4, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 1, 0, 0, 5, 0],   
    ]

    solver1 = SudokuSolver(easy_puzzle)
    solution1 = solver1.solve()

    solver2 = SudokuSolver(hard_puzzle)
    solution2 = solver2.solve()

    if solution1:
        print("Solution for Easy Sudoku:\n")
        print_sudoku(solution1)
    else:
        print("No solution exists for Easy Sudoku")

    print("="*30 + "\n")

    if solution2:
        print("Solution for Hard Sudoku:\n")
        print_sudoku(solution2)
    else:
        print("No solution exists for Hard Sudoku")