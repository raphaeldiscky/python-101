'''
    no queen should share a row, column, or diagonal with another queen
    Time Complexity: O(n^n)

    n = 4
    board = ["----",
            "----",
            "----",
            "----"
            ]

    placeNQueens(n, board) =
       ["-q--",
        "---q",
        "q---",
        "--q-"
        ]
'''


def isSafe(i, j, board):
    # to test whether the position given by i row and j column is safe to place a queen.
    for c in range(len(board)):
        for r in range(len(board)):
            # check if i,j share row with any queen
            if board[c][r] == 'q' and i == c and j != r:
                return False
            # check if i,j share column with any queen
            elif board[c][r] == 'q' and j == r and i != c:
                return False
            # check if i,j share diagonal with any queen
            elif (i+j == c+r or i-j == c-r) and board[c][r] == 'q':
                return False
    return True


def nQueens(r, n, board):
    # base case, when queens have been placed in all rows return
    if r == n:
        return True, board
    # else in r-th row, check for every box whether it is suitable to place queen
    for i in range(n):
        if isSafe(r, i, board):
            # if i-th columns is safe to place queen, place the queen there and check recursively for other rows
            board[r][i] = 'q'
            okay, newboard = nQueens(r+1, n, board)
            # if all next queens were placed correctly, recursive call should return true, and we should return true here too
            if okay:
                return True, newboard
            # else this is not a suitable box to place queen, and we should check for next box
            board[r][i] = '-'
    return False, board


def placeNQueens(n, board):
    return nQueens(0, n, board)[1]


def main():
    n = 4
    board = [["-" for _ in range(n)] for _ in range(n)]
    qBoard = placeNQueens(n, board)
    qBoard = "\n".join(["".join(x) for x in qBoard])
    print(qBoard)


main()
