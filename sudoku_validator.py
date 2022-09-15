import numpy as np


def show_board(arr):

    for row in arr:
        print("+---" * len(arr) + "+")

        for c in row:
            print(f"| {c} ", end='')
        print("|")
    
    print("+---" * len(arr) + "+")



def is_possible(arr, row, column, number):
    
    for c in range(9):
        if arr[row][c] == number:
            
            return False

    for r in range(9):
        if arr[r][column] == number:
            
            return False


    x0 = (row // 3) * 3
    y0 = (column // 3) * 3

    for i in range(3):
        for j in range(3):
            if arr[x0 + i][y0 + j] == number:
                
                return False

    return True



def validator():
    tester_arr = [[0 for j in range(9)] for i in range(9)]

    arr = input("Enter the Sudoku Numbers in string: ").strip().split('\\n')
    arr = [list(map(int, list(txt))) for txt in arr]

    for r in range(9):
        for c in range(9):
            if is_possible(tester_arr, r, c, arr[r][c]):
                tester_arr[r][c] = arr[r][c]

            else:
                return False, arr

    return True, arr

output = validator()

if output[0] == True:
    print("|SUDOKU BOARD|\n".rjust(25))
    show_board(output[1])
    print("\n[Valid Sudoku Board]  Congrats..!\n")
    
else:
    print("|SUDOKU BOARD|".rjust(25))
    show_board(output[1])
    print("\nOps! Invalid Sudoku Board\n")
    




# NOTE: Test Data:
# VALID: 295743861\n431865927\n876192543\n387459216\n612387495\n549216738\n763524189\n928671354\n154938672

# INVALID: 195743862\n431865927\n876192543\n387459216\n612387495\n549216738\n763524189\n928671354\n254938671
