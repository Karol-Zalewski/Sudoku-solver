import pprint
def find_next_empty(puzzle):
    """
    Finds the next row, col on the puzzle that's not filled yet --> rep with -1
    Return row, col tuple (or(None, None) if there is none)
    Args:
        puzzle (_type_): (list): A list containing inner lists with int inside
    """
    # We are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    # If no spaces in the puzzle are empty (-1)
    return None, None

def is_valid(puzzle, guess, row, col):
    """
    Figures out whether the guess at the row/col of the puzzle is a valid guess
    Returns True if is valid, False otherwise
    Args:
        puzzle (list): A list containing inner lists with int inside
        guess int: The number (1-9) to check
        row (int): Describes position of the guess
        col (int): Describes position of the guess
    """
    
    # Check if the number in guess already exists in the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # Check if the number in guess already exists in the column
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False
    
    # Check if the number already exists in the 3x3 square
    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3
    square = []
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            square.append(puzzle[r][c])
    
    if guess in square:
        return False
    
    return True

def solve_sudoku(puzzle):
    """
    Solve sudoku using backtracking!
    Our puzzle is a list made from lists, where each inner list is a row in our sudoku puzzle
    return whether a solution exists
    mutates puzzle to be the solution (if the solution exists)
    Args:
        puzzle (list): A list containing inner lists with int inside
    """

    # Chose a random place on the board to make a guess
    row, col = find_next_empty(puzzle)

    # If there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True
    
    # If there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1,10):

        # Check if it is a valid guess
        if is_valid(puzzle, guess, row, col):

            # If this is valid, than place that guess on the puzzle
            puzzle[row][col] = guess

            # Now recurse using this puzzle
            if solve_sudoku(puzzle):
                return True
            
        # If it is not valid or if our guess does not solve the puzzle
        # we need to backtrack and try a new number

        # Reset the guess
        puzzle[row][col] = -1

    # If none of the numbers that we try work, then this puzzle is Unsolvable!
    return False

Example_board = [
    [3, 9, -1,  -1, 5, -1,  -1, -1, -1],
    [-1, -1, -1,  2, -1, -1,  -1, -1, 5],
    [-1, -1, -1,  7, 1, 9,  -1, 8, -1],

    [-1, 5, -1,  -1, 6, 8,  -1, -1, -1],
    [2, -1, 6,  -1, -1, 3, -1, -1, -1],
    [-1, -1, -1,  -1, -1, -1,  -1, -1, 4],

    [5, -1, -1,  -1, -1, -1,  -1, -1, -1],
    [6, 7, -1, 1, -1, 5,  -1, 4, -1],
    [1, -1, 9,  -1, -1, -1, 2, -1, -1]
]
if __name__ == '__main__':
    print(solve_sudoku(Example_board))
    pprint.pprint(Example_board)

            