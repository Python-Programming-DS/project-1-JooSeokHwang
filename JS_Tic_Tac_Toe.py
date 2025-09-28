# --------------------------------------------------------------------
# Name : Joo Seok Hwang
# Date : 28 Sep 2025
# --------------------------------Note--------------------------------
# This is a program for Game of Tic-Tac-Toe played on 3 by 3 grid by two playrer.
# Whoever makes 3 marks in a row by row, column, or diagonal wins. 
# Please enjoy the game.
# --------------------------------------------------------------------

def printBoard(board):  # print the board status
    print("-----------------")
    print(r"|R\C| 0 | 1 | 2 |")
    print("-----------------")
    print(f"| 0 |{board[0][0]:^3}|{board[0][1]:^3}|{board[0][2]:^3}|")
    print("-----------------")
    print(f"| 1 |{board[1][0]:^3}|{board[1][1]:^3}|{board[1][2]:^3}|")
    print("-----------------")
    print(f"| 2 |{board[2][0]:^3}|{board[2][1]:^3}|{board[2][2]:^3}|")
    print("-----------------")

def resetBoard(board):  # reset the board status
    return [["" for _ in range(3)] for _ in range(3)]

def getGrid(turn):  # get grid and return its row and col numbers
    print(f"\n{turn}'s turn.")
    print(f"Where do you want your {turn} placed?")
    print("Please enter row number and column number separated by a comma.")
    grid = input()
    print(f"{"\033[F"}{"\033[K"}{"\033[31m"}{grid}{"\033[0m"}")  # highlight user input with red color
    grid = grid.split(",")
    print(f"You have entered row #{grid[0]}\n\t  and column #{grid[1]}")
    return int(grid[0]), int(grid[1])

def validateEntry(row, col, board):  # return True if valid, error msg and False if invalid
    # if row or column size is bigger than board size, print error msg and return False
    if row > len(board)-1 or col > len(board[0])-1:
        print("Invalid entry: try again.")
        print("Row & column numbers must be 0, 1, or 2.")
        return False

    # if the input grid position is not empty, print error msg and return False
    elif board[row][col] != "":  
        print("That cell is already taken.")
        return False
    
    # if neither out of the board nor already taken, return True
    else:
        print("Thank you for your selection.")
        return True

def checkFull(board):  # return True if the board is full, False if not full
    for row in board:
        if "" in row:
            return False
    return True

def checkWin(board, turn):  # at one's turn, chenk if he or she wins, and return True if does, or False
    winner = ""
    
    # check win by row by counting marks in each row
    for i in range(len(board)):
        if board[i].count(turn) == 3:
            winner = turn

    # create new lists on each column and check win by counting marks in the lists 
    # I find a simpler way using [row[i] for row in board], but leaving original code for record
    for i in range(len(board[0])):  
        col = []
        for j in range(len(board)):
            col.append(board[j][i])
        if col.count(turn) == 3:
            winner = turn
    
    # create new lists by each diagonal and check win by counting marks in the lists
    diag_to_right = []
    for i in range(len(board)):  # create a diagonal list toward right from [0,0] to [2,2]
        diag_to_right.append(board[i][i])
        if diag_to_right.count(turn) == 3:
            winner = turn
    diag_to_left = []
    for i in range(len(board)):  # create a diagonal list toward left from [0,-1] to [2,-3]
        diag_to_left.append(board[i][-(i+1)])
        if diag_to_left.count(turn) == 3:
            winner = turn

    if winner != "":
        return True
    else:
        return False

def ifEnd(board, turn):  # if the game ends, display the result and return True, or return False
    if checkWin(board, turn) == True:  # when there is a winner
        print(f"{turn} IS THE WINNER!!!")
        printBoard(board)
        return True
    elif checkFull(board) == True:  # draw when the board is full but no winner
        print("DRAW! NOBODY WINS!")
        printBoard(board)
        return True
    else : 
        return False

def main():
    # initialize board, turn, restart indicator
    board = [["" for _ in range(3)] for _ in range(3)]
    turn = "X"
    re = "y"

    print("\nNew Game: X goes first.\n")
    printBoard(board)

    while re.lower() == "y":
        row, col = getGrid(turn)
        while validateEntry(row, col, board) is False:  # Check validation of a input, if not repeat asking for input
            row, col = getGrid(turn)
        board[row][col] = turn  # if valid, put the input in the board
        
        if ifEnd(board, turn) == True:  # if the game ends, reset and get input for new game
            board = resetBoard(board)
            print("\nAnother Game? Enter Y or y for yes.")
            re = input()
            print(f"{"\033[F"}{"\033[K"}{"\033[31m"}{re.upper()}{"\033[0m"}")  # highlight user input with red color
            if re.lower() == "y":
                print("New Game: X goes first.\n")
                printBoard(board)

        # if the game is not end, change turns
        else: 
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            printBoard(board)
    print("\nThank you for playing!")

if __name__ == "__main__":
    main()