"""
NAME 
    solver

DESCRIPTION
    a simple sudoku solver written with the backtracking algorithm
    all credit goes to techwithtim @ https://www.techwithtim.net/
    written for personal, educational purposes

FUNCTIONS 
    solve(bo)

    valid(bo, num, pos)

    print_board(bo)

    find_empty(bo)
"""

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
] # the starting board that needs to be solved

def solve(bo):
    """
    DESCRIPTION
    uses a backtracking algorithm to solve the board
    uses find_empty and valid
    recursively backtracks

    PARAMETERS
    bo: board to be solved

    RETURN
    returns true if board is solved
    """
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False
    
def valid(bo, num, pos):
    """
    DESCRIPTION
    checks if a number in a spot is valid
    validity is determined according to sudoku rules 

    PARAMETERS
    bo: board to be solved
    num: number being checked (1-9)
    pos: position being checked

    RETURN
    returns true if valid 
    """
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True
    
def print_board(bo):
    """
    DESCRIPTION
    prints a 9x9 sudoku board  
    visually seperates each 3x3 box 

    PARAMETERS 
    bo: 9x9 board to be printed 
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("---------------------")  

        for j in range(len(bo[i])): 
            if j % 3 == 0 and j != 0:
                print(" | ", end="") 

            if j == 8:
                print(bo[i][j]) 
            elif j == 2 or j == 5: 
                print(bo[i][j], end="")
            else: 
                print(str(bo[i][j]) + " ", end="") 

def find_empty(bo):
    """
    DESCRIPTION
    finds the first empty spot in a 9x9 sudoku board 
    empty spots contain 0
    searches top to bottom, left to right

    PARAMETERS
    bo: 9x9 board to be searched 

    RETURN 
    returns a tuple containing the location of the empty spot
    """
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return (i, j) # row, col 

    return None


# prints board before and after solution
print_board(board)
solve(board)
print("                             ")
print_board(board)