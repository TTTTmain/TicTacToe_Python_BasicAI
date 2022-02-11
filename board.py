from colorama import Fore

board = ["   ","   ","   ","   ","   ","   ","   ","   ","   "]
board2 = ["   ","   ","   ","   ","   ","   ","   ","   ","   "]


retry = 0

def board_layout(bo):
    print(bo[0] + "|" + bo[1] + "|" + bo[2])
    print("-----------")
    print(bo[3] + "|" + bo[4] + "|" + bo[5])
    print("-----------")
    print(bo[6] + "|" + bo[7] + "|" + board[8])

def isWinner(bo):
    return ((bo[6] == " x " and bo[7] == " x " and bo[8] == " x ") or
    (bo[3] == " x " and bo[4] == " x " and bo[5] == " x ") or
    (bo[0] == " x " and bo[1] == " x " and bo[2] == " x ") or
    (bo[0] == " x " and bo[3] == " x " and bo[6] == " x ") or
    (bo[1] == " x " and bo[4] == " x " and bo[7] == " x ") or
    (bo[2] == " x " and bo[5] == " x " and bo[8] == " x ") or
    (bo[0] == " x " and bo[4] == " x " and bo[8] == " x ") or
    (bo[6] == " x " and bo[4] == " x " and bo[2] == " x "))

def isLoser(bo):
    return ((bo[6] == " o " and bo[7] == " o " and bo[8] == " o ") or
    (bo[3] == " o " and bo[4] == " o " and bo[5] == " o ") or
    (bo[0] == " o " and bo[1] == " o " and bo[2] == " o ") or
    (bo[0] == " o " and bo[3] == " o " and bo[6] == " o ") or
    (bo[1] == " o " and bo[4] == " o " and bo[7] == " o ") or
    (bo[2] == " o " and bo[5] == " o " and bo[8] == " o ") or
    (bo[0] == " o " and bo[4] == " o " and bo[8] == " o ") or
    (bo[6] == " o " and bo[4] == " o " and bo[2] == " o "))

def isTie():
    return board.count(" x ") == 5

def playerMove():
    playerPos = input("Choose your Location: ")

    if playerPos == "1" and board[0] == "   ":
        board[0] = " x "
        board2[0] = " x "
        playerPos = 0
    elif playerPos == "1" and board[0] != "   ":
        print(Fore.RED + "Space Taken")
        print(Fore.WHITE)
        playerPos = 0
        retry = 1

    if playerPos == "2" and board[1] == "   ":
        board[1] = " x "
        board[1] = " x "
        playerPos = 0
    elif playerPos == "2" and board[1] != "   ":
        print(Fore.RED + "Space Taken")
        print(Fore.WHITE)
        playerPos = 0
        retry = 1

    if playerPos == "3" and board[2] == "   ":
        board[2] = " x "
        board2[2] = " x "
        playerPos = 0
    elif playerPos == "3" and board[2] != "   ":
        print(Fore.RED + "Space Taken")
        print(Fore.WHITE)
        playerPos = 0
        retry = 1

    if playerPos == "4" and board[3] == "   ":
        board[3] = " x "
        board2[3] = " x "
        playerPos = 0
    elif playerPos == "4" and board[3] != "   ":
        print(Fore.RED + "Space Taken")
        print(Fore.WHITE)
        playerPos = 0
        retry = 1

    if playerPos == "5" and board[4] == "   ":
        board[4] = " x "
        board2[4] = " x "
        playerPos = 0
    elif playerPos == "5" and board[4] != "   ":
        print(Fore.RED + "Space Taken")
        print(Fore.WHITE)
        playerPos = 0
        retry = 1

    if playerPos == "6" and board[5] == "   ":
        board[5] = " x "
        board2[5] = " x "
        playerPos = 0
    elif playerPos == "6" and board[5] != "   ":
        print(Fore.RED + "Space Taken")
        print(Fore.WHITE)
        playerPos = 0
        retry = 1

    if playerPos == "7" and board[6] == "   ":
        board[6] = " x "
        board2[6] = " x "
        playerPos = 0
    elif playerPos == "7" and board[6] != "   ":
        print(Fore.RED + "Space Taken")
        print(Fore.WHITE)
        playerPos = 0
        retry = 1

    if playerPos == "8" and board[7] == "   ":
        board[7] = " x "
        board2[7] = " x "
        playerPos = 0
    elif playerPos == "8" and board[7] != "   ":
        print(Fore.RED + "Space Taken")
        print(Fore.WHITE)
        playerPos = 0
        retry = 1

    if playerPos == "9" and board[8] == "   ":
        board[8] = " x "
        board2[8] = " x "
        playerPos = 0
    elif playerPos == "9" and board[8] != "   ":
        print(Fore.RED + "Space Taken")
        print(Fore.WHITE)
        playerPos = 0
        retry = 1



if retry == "1":
        pass
        #does not do a turn
elif retry == "0":
        pass
        #take a turn
