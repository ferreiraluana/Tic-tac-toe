#!/usr/bin/env python
# coding: utf-8

# # Tic Tac Toe
# ### For two human players

from IPython.display import clear_output

player1 = {'name':'','symbol':'X'}
player2 = {'name':'','symbol':'O'}
endGame = False
grid = [" "," "," "," "," "," "," "," "," "]
winner = 0


def start(player1, player2):
    print(".......................")
    print("Welcome to Tic Tac Toe")
    print(".......................")
    player1['name'] = input("Enter player 1 name: ")
    player2['name'] = input("Enter player 2 name: ")
    print(".......................")
    print("X: "+player1['name'])
    print("O: "+player2['name'])
    print(".......................")


def gridGuide():
    print("   |   |   ")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print("   |   |   ")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print("   |   |   ")
    print(" 1 | 2 | 3 ")


def displayGrid(grid):
    print("   |   |   ")
    print(" "+grid[6]+" | "+grid[7]+" | "+grid[8]+" ")
    print("-----------")
    print("   |   |   ")
    print(" "+grid[3]+" | "+grid[4]+" | "+grid[5]+" ")
    print("-----------")
    print("   |   |   ")
    print(" "+grid[0]+" | "+grid[1]+" | "+grid[2]+" ")
    

def YouTied(grid):
    tied = 0
    for index in range(0,9):
        if(grid[index]!=' '):
            tied += 1
    if tied != 9:
        return 0
    else:
        return 3

def play(player, grid):
    print(".......................")
    position = input(player['name']+", choose a position between 1-9:")
    if(len(position) != 1):
        print("Choose a number between 1 and 9. Try again!")
        play(player, grid)

    position = int(position)

    if(position>9 or position<1):
        print("Choose a number between 1 and 9. Try again!")
        play(player, grid)
    
    if(grid[position-1]==" "):    
        grid[position-1] = player['symbol']
    else:
        print("Position unavailable. Try again!")
        play(player, grid)   

def verifyPlayer(symbol, player1,player2):
    if(symbol==player1['symbol']):
        return 1
    elif(symbol==player2['symbol']):
        return 2
    elif(symbol==' '):
        return 0

def verifyGrid(grid, player1, player2):
    if(grid[0]==grid[1] and grid[0]==grid[2]):
        return verifyPlayer(grid[0], player1, player2)
    elif(grid[3]==grid[4] and grid[3]==grid[5]):
        return verifyPlayer(grid[3], player1, player2)
    elif(grid[6]==grid[7] and grid[6]==grid[8]): 
        return verifyPlayer(grid[6], player1, player2)
    elif(grid[0]==grid[3] and grid[0]==grid[6]):
        return verifyPlayer(grid[0], player1, player2)
    elif(grid[1]==grid[4] and grid[1]==grid[7]):
        return verifyPlayer(grid[1], player1, player2)
    elif(grid[2]==grid[5] and grid[2]==grid[8]):
        return verifyPlayer(grid[2], player1, player2)
    elif(grid[0]==grid[4] and grid[0]==grid[8]):
        return verifyPlayer(grid[0], player1, player2)
    elif(grid[2]==grid[4] and grid[2]==grid[6]):
        return verifyPlayer(grid[2], player1, player2)
    
    else: 
        return 0    


# ### Main starts here

start(player1, player2)
gridGuide()
while(endGame == False):
    print()
    print()

    displayGrid(grid)
    print()

    tie = YouTied(grid)
    if(tie == 3):
        displayGrid(grid)
        print("You Tied. Nobody won!")
        endGame = True
        break

    play(player1, grid)
    winner = verifyGrid(grid, player1, player2)
    if(winner == 1):
        displayGrid(grid)
        print(player1['name']+" won! Congratulations")
        endGame = True
        break
    elif(winner == 2):
        displayGrid(grid)
        print(player2['name']+" won! Congratulations")
        endGame = True
        break
    elif(winner == 0):
        print('No winner so far')

    displayGrid(grid)
    print()

    tie = YouTied(grid)
    if(tie == 3):
        displayGrid(grid)
        print("You Tied. Nobody won!")
        endGame = True
        break

    play(player2, grid)
    displayGrid(grid)
    winner = verifyGrid(grid, player1, player2)
    if(winner == 1):
        displayGrid(grid)
        print(player1['name']+" won! Congratulations")
        endGame = True
        break
    elif(winner == 2):
        displayGrid(grid)
        print(player2['name']+" won! Congratulations")
        endGame = True
        break
    elif(winner == 0):
        print('No winner so far')

    print()
    clear_output()