moveNumber = 0
board = []
gameOver = False
currentPlayer = ""

# Populate Board list with all empty characters
for i in range (0,9):
    board.append("-")

# Asks and returns user input | int 0 - 8
def getMove(currentPlayer):
    x = input("Move: ")
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
    
def main(board, gameOver, moveNumber, currentPlayer):
    # Make sure game is still going on
    while gameOver != True:
        drawBoard()
        validMove = False
        move = int(getMove(currentPlayer))

        # Check whose move it is
        if moveNumber % 2 == 0:
            currentPlayer = "x"
        else:
            currentPlayer = "o"

        if boardContainsEmpty() == False:
            endGame()
            break

        while spaceEmpty(move) == False:
            validMove = spaceEmpty(move)

            if validMove == False:
                print("Illegal Move")
                move = int(getMove(currentPlayer))

        board[move] = currentPlayer
    
        moveNumber += 1

        if checkWin() == True:
            drawBoard()

            if currentPlayer == "x":
                print("X Won")
            else:
                print("O Won")
            
            gameOver = True
            endGame()

    if boardContainsEmpty() == False:
        gameOver = True

main(board, gameOver, moveNumber, currentPlayer)
