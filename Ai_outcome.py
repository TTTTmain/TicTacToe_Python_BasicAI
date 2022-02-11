import random
from board import board, isWinner, board2

def moveRandom():
    aiPos = random.randint(1,9)

    if aiPos == 1:
        board[0] = " o "
        board2[0] = " o "
    elif aiPos == 2:
        board[1] = " o "
        board2[1] = " o "
    elif aiPos == 3:
        board[2] = " o "
        board2[2] = " o "
    elif aiPos == 4:
        board[3] = " o "
        board2[3] = " o "
    elif aiPos == 5:
        board[4] = " o "
        board2[4] = " o "
    elif aiPos == 6:
        board[5] = " o "
        board2[5] = " o "
    elif aiPos == 7:
        board[6] = " o "
        board2[6] = " o "
    elif aiPos == 8:
        board[7] = " o "
        board2[7] = " o "
    elif aiPos == 9:
        board[8] = " o "
        board2[8] = " o "
    aiPos = 0

posCorner = []
posEdge = []
open = []

def isBlank():
    spaces = list(enumerate(board))
    for i in spaces:
        if i == (0, "   "):
            open.append(i)
        elif i == (1, "   "):
            open.append(i)
        elif i == (2, "   "):
            open.append(i)
        elif i == (3, "   "):
            open.append(i)
        elif i == (4, "   "):
            open.append(i)
        elif i == (5, "   "):
            open.append(i)
        elif i == (6, "   "):
            open.append(i)
        elif i == (7, "   "):
            open.append(i)
        elif i == (8, "   "):
            open.append(i)


def moveWin1():
    #find open spots
    pos = [x[0] for x in open]
    for num in pos:
        board2[num] = " o "
        if isWinner(board) == True:
            board[num] = " o "
            break
        else:
            board2[num] = "   "

    for num in pos:
        if num == 0:
            posCorner.append(num)
        if num == 2:
            posCorner.append(num)
        if num == 6:
            posCorner.append(num)
        if num == 8:
            posCorner.append(num)

    if len(posCorner) == 0:
        for num in pos:
            if num == 4:
                board[4] = " o "
                board2[4] = " o "

            else:
                for num in pos:
                    if num == 1:
                        posEdge.append(num)
                    if num == 3:
                        posEdge.append(num)
                    if num == 5:
                        posEdge.append(num)
                    if num == 7:
                        posEdge.append(num)

def moveNext():
    if len(posCorner) >= 1:
        corner = random.choice(posCorner)
        board[corner] = " o "
        board2[corner] = " o "
        try:
            posCorner.clear()
        except AttributeError:
            pass


    elif len(posEdge) >= 1 :
        edge = random.choice(posEdge)
        board[edge] = " o "
        board2[edge] = " o "
        try:
            edge.clear()
        except AttributeError:
            pass

def checkIfPlayerWin():
    if
















def moveWin2():
    pass
    #take priority in winning, use tacic, unless middle taken



def moveBlock2():
    pass
    #block if necessary
