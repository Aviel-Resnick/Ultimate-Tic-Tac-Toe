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

def boardEmpty():
    for i in board:
        if board[i] == "-":
            return False

    return True


def main(board, gameOver, moveNumber, currentPlayer):
    # Make sure game is still going on
    while gameOver != True:
        print(board)

        # Check whose move it is
        if moveNumber % 2 == 0:
            currentPlayer = "x"
        else:
            currentPlayer = "o"

        board[int(getMove(currentPlayer))] = currentPlayer

        moveNumber += 1

    if boardEmpty() == False:
        gameOver = True


main(board, gameOver, moveNumber, currentPlayer)
