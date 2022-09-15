
class Sudoku:
    def __init__(self):
        self.board_arr = [[0 for j in range(9)] for i in range(9)]
        self.board_arr[0][1] = 8
        self.board_arr[7][5] = 2

        
    def is_possible(self, row, col, n):
        for i in range(9):
            if self.board_arr[row][i] == n:
                return False
            
        for j in range(9):
            if self.board_arr[j][col] == n:
                return False

        x0 = row // 3 * 3
        y0 = col // 3 * 3

        for i in range(3):
            for j in range(3):
                if self.board_arr[x0 + i][y0 + j] == n:
                    return False

        return True

    def solver(self):
        
        for r in range(9):
            for c in range(9):   
                if self.board_arr[r][c] == 0:

                    for n in range(1, 10):
                        if self.is_possible(r, c, n):

                            self.board_arr[r][c] = n
                            self.solver()
                                
                            self.board_arr[r][c] = 0
                    return 

        self.show_board(self.board_arr)
        print('\n_____________________________________')
        exit()



    def matrix_maker(self, r, c):
        self.board_arr = np.array([[c * i + j + 1 for j in range(c)] for i in range(r)], np.int8)


    def show_board(self, arr):

        for row in arr:
            print("+---" * len(arr) + "+")

            for c in row:
                print(f"| {c} ", end='')
            print("|")
        
        print("+---" * len(arr) + "+")
        


obj = Sudoku()

print("\t   |Initial Board|")
obj.show_board(obj.board_arr)


print("\n\n\t   |Solved Board|")
obj.solver()

