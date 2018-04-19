moveNumber = 0
board = [["-" for _ in range(3)] for _ in range(3)]
gameOver = False
currentPlayer = ""

# Asks and returns user input | int 0 - 8
def getMove(currentPlayer):
    move = int(input("Move: "))
    return (move - 1) // 3, (move - 1) % 3

def spaceEmpty(row, column):
    return True if board[row][column] == "-" else False

def drawBoard():
    for x in range(3):
        print(board[x][0], board[x][1], board[x][2])

def checkWin(row, column):
    #Check the horizontal wins
    if board[row][0] == board[row][1] == board[row][2] and not spaceEmpty(row, column):
        return True
    
    #Check the vertical wins
    if board[0][column] == board[1][column] == board[2][column] and not spaceEmpty(row, column):
        return True
    
    #Check the diagonal wins
    if board[0][0] == board[1][1] == board[2][2] and not spaceEmpty(0, 0):
        return True
		
    if board[0][2] == board[1][1] == board[2][0] and not spaceEmpty(0, 2):
        return True

    return False
    
    
def main(board, gameOver, moveNumber, currentPlayer):
    # Make sure game is still going on
    while gameOver != True:
        drawBoard()
        validMove = False
        row, column = getMove(currentPlayer)

        # Check whose move it is
        currentPlayer = "x" if moveNumber % 2 == 0 else "o"
        
        while spaceEmpty(row, column) == False:
            print("Illegal Move")
            row, column = getMove(currentPlayer)
        
        board[row][column] = currentPlayer
    
        moveNumber += 1

        if checkWin(row, column) == True:
            drawBoard()

            print("X won") if currentPlayer == "x" else "o won"
            
            gameOver = True
            print("The game is over")
            break

        if moveNumber == 9:
            print("The game is over.")

main(board, gameOver, moveNumber, currentPlayer)
