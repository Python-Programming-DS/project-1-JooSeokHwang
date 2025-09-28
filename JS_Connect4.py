# --------------------------------------------------------------------
# Name : Joo Seok Hwang
# Date : 28 Sep 2025
# --------------------------------Note--------------------------------
# This is a program for Game of Connect4 played on 6 by 7 grid by two playrer.
# Whoever makes 4 marks in a row by row, column, or diagonal wins. 
# For convenience in programming, I convert the columns in the board to rows, so board[0], board[1].... represent column a, b, .... in actual board.
# However, overall basic logic is not changed.
# Please enjoy the game.
# --------------------------------------------------------------------

def printBoard(board):  # print the board status
    print(f"| 6 |{board[0][5]:^3}|{board[1][5]:^3}|{board[2][5]:^3}|{board[3][5]:^3}|{board[4][5]:^3}|{board[5][5]:^3}|{board[6][5]:^3}|")
    print("---------------------------------")
    print(f"| 5 |{board[0][4]:^3}|{board[1][4]:^3}|{board[2][4]:^3}|{board[3][4]:^3}|{board[4][4]:^3}|{board[5][4]:^3}|{board[6][4]:^3}|")
    print("---------------------------------")
    print(f"| 4 |{board[0][3]:^3}|{board[1][3]:^3}|{board[2][3]:^3}|{board[3][3]:^3}|{board[4][3]:^3}|{board[5][3]:^3}|{board[6][3]:^3}|")
    print("---------------------------------")
    print(f"| 3 |{board[0][2]:^3}|{board[1][2]:^3}|{board[2][2]:^3}|{board[3][2]:^3}|{board[4][2]:^3}|{board[5][2]:^3}|{board[6][2]:^3}|")
    print("---------------------------------")
    print(f"| 2 |{board[0][1]:^3}|{board[1][1]:^3}|{board[2][1]:^3}|{board[3][1]:^3}|{board[4][1]:^3}|{board[5][1]:^3}|{board[6][1]:^3}|")
    print("---------------------------------")
    print(f"| 1 |{board[0][0]:^3}|{board[1][0]:^3}|{board[2][0]:^3}|{board[3][0]:^3}|{board[4][0]:^3}|{board[5][0]:^3}|{board[6][0]:^3}|")
    print("---------------------------------")    
    print(r"|R\C| a | b | c | d | e | f | g |") 
    print("---------------------------------")

def resetBoard(board):  # reset the board status
    return [["" for _ in range(6)] for _ in range(7)]

def getGrid(turn, availables):  # get grid and if the grid is in available positions, return its row and col by number
    letters = "abcdefg"
    nums = "123456"
    grid = ""
    print(f"\n{turn}'s turn.")
    print(f"Where do you want your {turn} placed?")
    while grid not in availables:  # when the grid is not available, repeat asking for input
        print(f"Available positions are: {availables}\n")
        grid = input(f"Please enter column-letter and row-number (e.g., a1): ")
    print("Thank you for your selection.")
    return int(letters.find(grid[0])), int(nums.find(grid[1]))  # convert a1, b1, ... form to 00, 10, ...

def availablePosition(board):  # return a list of available positions as a form of a1, b1, ...
    avail_pos = []
    letters = "abcdefg"

    # for each row(row a, row b, ....), get the last position
    for i in range(len(board)):
        row = letters[i]
        col = str(len(board[i]) - board[i].count("") + 1)  # get the last position number of a row by subtracting the number of empty positions and convert to string form
        avail_pos.append(row + col)
    return avail_pos

def checkFull(board):  # return True if full, False if not full
    for row in board:
        if "" in row:
            return False
    return True

def checkWin(board, turn):  # at one's turn, chenk if he or she wins, then return True if does, or False
    winner = ""

    # check win by row by counting marks in each row
    for i in range(len(board)):  
        for j in range(len(board[0])-3):  # each iteration starting grid changes from ([0,0] to [0,2]) to ([6,0] to [6,2])
            if board[i][j:j+4].count(turn) == 4:  # if a 4-position contains 4 same makrs, he or she wins
                winner = turn
                return True
            
    # create new lists on each column and check win by counting marks in the lists 
    for i in range(len(board[0])): 
        col = [row[i] for row in board]
        for j in range(len(board)-3):  # each iteration starting grid changes from ([0,0] to [3,0]) to ([0,5], [3,5])
            if col[j:j+4].count(turn) == 4:  # if a 4-position of a new list contains 4 same makrs, he or she wins
                winner = turn
                return True
            
    # create new lists by diagonal and check win by counting marks in the lists 
    # create a diagonal list toward right
    # each iteration starting grid changes, so the diagonal list changes from ['a1', 'b2', 'c3', 'd4'] to ['d3', 'e4', 'f5', 'g6']
    for i in range(len(board)-3):
        for j in range(len(board[0])-3):
            diag_to_right = []
            for k in range(4):
                diag_to_right.append(board[i+k][j+k])
            if diag_to_right.count(turn) == 4:
                winner = turn 
                return True   
            
    # create a diagonal list toward left 
    # each iteration starting grid changes so the diagonal list changes from ['a4', 'b3', 'c2', 'd1'] to ['d6', 'e5', 'f4', 'g3']
    for i in range(len(board)-3): 
        for j in range(len(board[0])-3, len(board[0])):
            diag_to_left = []
            for k in range(4):
                diag_to_left.append(board[i+k][j-k])
            if diag_to_left.count(turn) == 4:
                winner = turn
                return True    
    return False

def ifEnd(board, turn):  # if ends, display the result and return True, or return False
    if checkWin(board, turn) == True:
        print(f"\n{turn} IS THE WINNER!!!")
        printBoard(board)
        return True
    elif checkFull(board) == True:
        print("\nDRAW! NOBODY WINS!")
        printBoard(board)
        return True
    else: 
        return False

def main():
    # initialize board, turn, restart indicator
    board = [["" for _ in range(6)] for _ in range(7)]
    turn = "X"
    re = "y"

    print("\nNew Game: X goes first.\n")
    printBoard(board)
    
    while re.lower() == "y":
        row, col = getGrid(turn, availablePosition(board))  # check input validity and get grid
        board[row][col] = turn  # put the grid into the board

        # if the game ends, reset and get input for new game
        if ifEnd(board, turn) == True:
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