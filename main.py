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

def drawBoard(board):
    x = 0
    while(x <= len(board) - 1):
        print(board[x], board[x + 1], board[x + 2])
        x = x + 3

def endGame():
    print("The game is over.")

def main(board, gameOver, moveNumber, currentPlayer):
    # Make sure game is still going on
    while gameOver != True:
        drawBoard(board)
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

    if boardContainsEmpty() == False:
        gameOver = True

main(board, gameOver, moveNumber, currentPlayer)
