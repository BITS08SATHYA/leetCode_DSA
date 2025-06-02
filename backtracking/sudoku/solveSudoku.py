def solveSudoku(board):
    def isValid(num, row, col):
        for x in range(9):
            # column check
            if board[x][col] == num:
                return False
            # row check
            if board[row][x] == num:
                return False
            # box check
            r = 3 * (row // 3) + x //3
            c = 3 * (col//3) + x % 3
            if board[r][c] == num:
                return False
        return True

    def fillTHeBoard(board):
        # identify the empty cell
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in '123456789':
                        if isValid(num, row, col):
                            board[row][col] = num
                            if fillTHeBoard(board): return True
                            board[row][col] = '.'
                    return False
        return True
    fillTHeBoard(board)


print()

