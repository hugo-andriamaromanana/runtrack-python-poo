import random

def my_len(board):
    if board == []:
        return 0
    else:
        return 1 + my_len(board[1:])
    
def create_board(n,counter=0):
    board=[]
    if n == counter:
        return board
    else:
        board = board + [["0"]*n]
        return board + create_board(n,counter+1)

def my_join(sep,arrays):
    if my_len(arrays) == 0:
        return ""
    else:
        return arrays[0] + sep + my_join(sep,arrays[1:])

def print_board(board):
    if my_len(board) == 0:
        pass
    else:
        print(my_join(' ',board[0]))
        print_board(board[1:])

def place_queen(board,row,col):
    if my_len(board) == 0:
        return board
    else:
        if row == 0:
            board[0][col] = "X"
            return board
        else:
            return [board[0]] + place_queen(board[1:],row-1,col)

def queen_attack_XY(board,row,col):
    for i in range(my_len(board)):
        if board[row][i] == "X":
            return True
    for i in range(my_len(board)):
        if board[i][col] == "X":
            return True
    return False

#queen_attack_xy but recursive
def queen_attack_XY_rec(board,row,col):
    if my_len(board) == 0:
        return False
    else:
        if board[row][0] == "X":
            return True
        else:
            return queen_attack_XY_rec(board,row,col-1)

def queen_attack_diagonal(board,row,col):
    for i in range(my_len(board)):
        if row-i >= 0 and col-i >= 0:
            if board[row-i][col-i] == "X":
                return True
        if row+i < my_len(board) and col+i < my_len(board):
            if board[row+i][col+i] == "X":
                return True
        if row-i >= 0 and col+i < my_len(board):
            if board[row-i][col+i] == "X":
                return True
        if row+i < my_len(board) and col-i >= 0:
            if board[row+i][col-i] == "X":
                return True
    return False

def queen_attack_diagonal_rec(board,row,col):
    if my_len(board) == 0:
        return False
    else:
        if row-1 >= 0 and col-1 >= 0:
            if board[row-1][col-1] == "X":
                return True
        if row+1 < my_len(board) and col+1 < my_len(board):
            if board[row+1][col+1] == "X":
                return True
        if row-1 >= 0 and col+1 < my_len(board):
            if board[row-1][col+1] == "X":
                return True
        if row+1 < my_len(board) and col-1 >= 0:
            if board[row+1][col-1] == "X":
                return True
        return queen_attack_diagonal_rec(board,row-1,col-1)

def queen_attack(board,row,col):
    if queen_attack_XY(board,row,col) == True or queen_attack_diagonal(board,row,col) == True:
        return True
    else:
        return False

def backtracking(board,row,col):
    if queen_attack(board,row,col) == False:
        return True
    else:
        return False

def place_queens(board,n):
        
def main():
    board = create_board(8)
    board = place_queens(board,8)
    print_board(board)

main()