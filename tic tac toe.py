def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0) 
    one = 'X' if xState[1] else ('O' if zState[1] else 1) 
    two = 'X' if xState[2] else ('O' if zState[2] else 2) 
    three = 'X' if xState[3] else ('O' if zState[3] else 3) 
    four = 'X' if xState[4] else ('O' if zState[4] else 4) 
    five = 'X' if xState[5] else ('O' if zState[5] else 5) 
    six = 'X' if xState[6] else ('O' if zState[6] else 6) 
    seven = 'X' if xState[7] else ('O' if zState[7] else 7) 
    eight = 'X' if xState[8] else ('O' if zState[8] else 8) 
    print(f" {zero} | {one} | {two} ")
    print("---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

def sum(a, b, c):
    return a + b + c

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("\nX wong")
            return 1
        elif sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("\nO won")
            return 0
        
    return -1

xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1
print("TIC TAC TOE\n")

while True:
    printBoard(xState, zState)
    
    if turn == 1:
        print("\nX to play \n")
    else:
        print("\nO to play \n")
    
    while True:
        value = int(input('Enter value (0-8): '))
        
        if xState[value] == 0 and zState[value] == 0:
            break
        else:
            print("Spot already taken, choose another spot.")
    
    if turn == 1:
        xState[value] = 1
    else:
        zState[value] = 1

    check = checkWin(xState, zState)
    if check != -1:
        printBoard(xState,zState)
        print("\nMatch over!!")
        break
    
    turn = not turn
