import sys

moveNumber = 0
board = []
gameOver = False
currentPlayer = ""
moves = []

# Populate Board list with all empty characters
for i in range (0,9):
    board.append("-")

# Asks and returns user input | int 0 - 8
def getMove(currentPlayer, moves):
    x = moves[moveNumber]
    return x

# If false game over
def boardContainsEmpty():
    for i in range(0, len(board)):
        if board[i] == "-":
            return(True)

    return False

def spaceEmpty(space):
    if board[space] == "-":
        return True
    else:
        return False

def drawBoard():
    x = 0
    while(x <= len(board) - 1):
        print(board[x], board[x + 1], board[x + 2])
        x = x + 3

def endGame():
    print("The game is over.")

def checkWin():
    if board[0] == board[1] == board[2]:
        if spaceEmpty(0) == False and spaceEmpty(1) == False and spaceEmpty(2) == False:
            return True
    if board[3] == board[4] == board[5]:
        if spaceEmpty(3) == False and spaceEmpty(4) == False and spaceEmpty(5) == False:
            return True
    if board[6] == board[7] == board[8]:
        if spaceEmpty(6) == False and spaceEmpty(7) == False and spaceEmpty(8) == False:
            return True
    if board[0] == board[3] == board[6]:
        if spaceEmpty(0) == False and spaceEmpty(3) == False and spaceEmpty(6) == False:
            return True
    if board[1] == board[4] == board[7]:
        if spaceEmpty(1) == False and spaceEmpty(4) == False and spaceEmpty(7) == False:
            return True
    if board[2] == board[5] == board[8]:
        if spaceEmpty(2) == False and spaceEmpty(5) == False and spaceEmpty(8) == False:
            return True
    if board[0] == board[4] == board[8]:
        if spaceEmpty(0) == False and spaceEmpty(4) == False and spaceEmpty(8) == False:
            return True
    if board[2] == board[4] == board[6]:
        if spaceEmpty(2) == False and spaceEmpty(4) == False and spaceEmpty(6) == False:
            return True
    else:
        return False
    
def writeOutput(result):
    out = open("output.txt","w")
    out.write(str(result))
    out.close()

def main(board, gameOver, moveNumber, currentPlayer, moves):
    # Open Log
    moves = open('log.txt').read().splitlines()

    drawBoard()

    # Populate the existing board
    for i in range(0, len(moves) - 1):
        # Check whose move it is
        if moveNumber % 2 == 0:
            currentPlayer = "x"
        else:
            currentPlayer = "o"
        
        print("")
        board[int(moves[i])] = currentPlayer
        moveNumber += 1
        drawBoard()

    # Check whose move it is
    if moveNumber % 2 == 0:
        currentPlayer = "x"
    else:
        currentPlayer = "o"

    # Start of current move checking

    thisMove = moves[len(moves) - 1]

    # Check if valid move
    if spaceEmpty(int(thisMove)) == False:
        writeOutput(0)

        lines = open('log.txt', 'r').readlines() 
        del lines[-1] 
        open('log.txt', 'w').writelines(lines)

        sys.exit()
    
    else: 
        board[int(thisMove)] = currentPlayer
        
        if boardContainsEmpty() == False:
            writeOutput(3)
            endGame()

        # Check if someone won
        if checkWin() == True:
            drawBoard()

            writeOutput(2)
            
            gameOver = True
            endGame()

        else:
            writeOutput(1)
            sys.exit()


main(board, gameOver, moveNumber, currentPlayer, moves)