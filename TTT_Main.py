from board import board_layout, playerMove, isWinner, board, board2, isLoser,isTie
from Ai_outcome import moveRandom, moveNext, moveWin1, isBlank, open, posEdge, posCorner
import random

#fixes:
#problem when it take both middle and edge
#random overlap at start

playerTurn = 0

board_layout(board)
playerMove()
moveRandom()

while True:
    board_layout(board)
    if isWinner(board) == True:
        print("You Win")
        break
    elif isLoser(board) == True:
        print("You Lose")
        break
    elif isTie() == True:
        print("Tie")
        break

    else:
        if playerTurn == 0:
            playerMove()
            playerTurn = 1
        else:
            isBlank()
            moveWin1()
            moveNext()
            open.clear()
            playerTurn = 0
