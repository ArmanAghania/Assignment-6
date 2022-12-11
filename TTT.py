import pyfiglet
import random
import datetime
import colorama

game_board = [["-","-","-"],
              ["-","-","-"],
              ["-","-","-"]]

def menu():  
    title = pyfiglet.figlet_format("Tic Tac Toe", font = "slant")
    print(title)     
    print('Select Game Mode: ')
    print('1. Single Player')
    print('2. Multiplayer')


def show():
    for row in game_board:
        for cell in row:
            if cell == 'X':
                print(colorama.Fore.RED + 'X', end=" ")
            elif cell == 'O':
                print(colorama.Fore.RED + 'O', end=" ")
            else:
                print(colorama.Fore.RESET + cell, end=" ")
        print(colorama.Fore.RESET)

def computer_input(role: str, sign: str):
    while True:

        if role == 'Computer':
            row = random.randint(0,2)
            col = random.randint(0,2)

            if game_board[row][col] == '-':
                game_board[row][col] = sign
                break
        else:
            row = int(input('row: '))
            col = int(input('col: '))
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game_board[row][col] == '-':
                    game_board[row][col] = sign
                    break
                else:
                    print('This cell is not empty, Try Again!')
            else:
                print('Your input should be between 0 and 2')

def checkGame(role: str, sign: str, startTime: int):
    if checkWin(sign) == True:
        print(f"\n{role} wins!")
        endTime = datetime.datetime.now().replace(microsecond =0 )
        print("Game Duration:", endTime - startTime)
        exit()
    else:
        if checkDraw() == True:
            print("\nDraw!")
            endTime = datetime.datetime.now().replace(microsecond = 0)
            print("Game Duration:", endTime - startTime)
            exit()

def checkWin(sign: str):
    win = False

    for i in range(3):
        if (game_board[i][0] == game_board[i][1] == game_board[i][2] == sign) or (game_board[0][i] == game_board[1][i] == game_board[2][i] == sign):
            win = True
            break
    if (game_board[0][0] == game_board[1][1] == game_board[2][2] == sign) or (game_board[0][2] == game_board[1][1] == game_board[2][0] == sign):
        win = True
    
    return win    

def checkDraw():
    if not any("-" in i for i in game_board):
        return True
    else:
        return False

def gamePlay(choice: int):
    
    show()
    startTime = datetime.datetime.now().replace(microsecond = 0)

    if choice == 1:
        while True:
            computer_input("Player", "X")
            show()
            checkGame("Player", "X", startTime)
            
            computer_input("Computer", "O")
            show()
            checkGame("Computer", "O", startTime)

    elif choice == 2:
        while True:
            computer_input("Player 1", "X")
            show()
            checkGame("Player 1", "X", startTime)

            computer_input("Player 2", "O")
            show()
            checkGame("Player 2", "O", startTime)

    else:
        while True:
            print("The input is not valid!")
            choice = int(input('--?!'))

            if choice == 1:
                break
            elif choice == 2:
                break
            
        gamePlay(choice)



menu()
choice = int(input('--?!'))
gamePlay(choice)

