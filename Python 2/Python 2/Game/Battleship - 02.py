from random import randint

board = []
boardTwo = []

for x in range(5):
    board.append(["O"] * 5)
    boardTwo.append(["O"] * 5)
     
    
def print_board(board):
    for row in board:
        print " ".join(row)
    
        
def random_row(board):
    return randint(0, len(board) - 1)
    
def random_col(board):
    return randint(0, len(board[0]) - 1)
    
ship_row = random_row(board)
ship_col = random_col(board)

playerRow = int(raw_input("Pick a row for your battleship "))
playerCol = int(raw_input("Pick a column for your battleship "))
boardTwo[playerRow - 1][playerCol - 1] = "B"
print_board(boardTwo)

ship_row = random_row(board)
ship_col = random_col(board)

win = False

#for turn in range(4):
while win == False:
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    enemyRow = randint(0, len(board) - 1)
    enemyCol = randint(0, len(board) - 1)

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        win = True
        break
    elif enemyRow == playerRow and enemyCol == playerCol:
        win = False
        print "Oh no! They've sunk your battleship!"
        break
        
    else:
        if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row - 1][guess_col - 1] == "X"):
            print "You guessed that one already."
        else:
            print "You missed their battleship!"
            board[guess_row - 1][guess_col - 1] = "X"
    print_board(board)
    print ""
    if enemyRow == playerRow and enemyCol == playerCol:
        print "Oh no! They've sunk your battleship!"
        win = True
        break
    elif boardTwo[enemyRow - 1][enemyCol - 1] == "X":
        enemyRow = randint(0, len(board) - 1)
        enemyCol = randint(0, len(board) - 1)
        continue
    else:
        print "The enemy missed your battleship!"
        boardTwo[enemyRow - 1][enemyCol - 1] = "X"
        print_board(boardTwo)
        print ""
        

