# Sudoku Solver

This is a Python program to solve Sudoku puzzles using a backtracking algorithm.

## Usage

The `SudokuSolver` class takes a 9x9 list representing the Sudoku puzzle as input. Empty cells are represented with 0.

To use it:

1. Instantiate a `SudokuSolver` object with a puzzle grid

2. Call the `solve()` method to find and return the solution

For example:

```python
puzzle = [
  [5,3,0,0,7,0,0,0,0],
  [6,0,0,1,9,5,0,0,0],
  [0,9,8,0,0,0,0,6,0],
  [8,0,0,0,6,0,0,0,3],
  [4,0,0,8,0,3,0,0,1],
  [7,0,0,0,2,0,0,0,6],
  [0,6,0,0,0,0,2,8,0],
  [0,0,0,4,1,9,0,0,5],
  [0,0,0,0,8,0,0,7,9]
]

solver = SudokuSolver(puzzle)  
solution = solver.solve()
print(solution)
```

The `print_sudoku()` function can be used to print out the puzzle in a human-readable format.

## Algorithm

This solver uses a backtracking algorithm to recursively try different values in each cell until a valid solution is found. 

It follows these steps:

1. Find the next empty cell
2. Try placing a valid number (1-9) in that cell  
3. Check if the puzzle is valid with that number placed
4. If valid, recursively try to fill the rest of the puzzle
5. If not valid, backtrack and try a new number in that cell
6. Repeat until the puzzle is filled or determined to be unsolvable

The `_valid()` method checks each placement against row, column and 3x3 box constraints.

Backtracking allows efficiently traversing the search space to find the solution.