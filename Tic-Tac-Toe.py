#!/usr/bin/env python
# coding: utf-8

# # Tic Tac Toe
# ### For two human players

# In[ ]:


from IPython.display import clear_output


# In[ ]:


player1 = {'name':'','symbol':'X'}
player2 = {'name':'','symbol':'O'}
endGame = False
grid = [" "," "," "," "," "," "," "," "," "]


# In[ ]:


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


# In[ ]:


def gridGuide():
    print("   |   |   ")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print("   |   |   ")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print("   |   |   ")
    print(" 1 | 2 | 3 ")


# In[ ]:


def displayGrid(grid):
    print("   |   |   ")
    print(" "+grid[6]+" | "+grid[7]+" | "+grid[8]+" ")
    print("-----------")
    print("   |   |   ")
    print(" "+grid[3]+" | "+grid[4]+" | "+grid[5]+" ")
    print("-----------")
    print("   |   |   ")
    print(" "+grid[0]+" | "+grid[1]+" | "+grid[2]+" ")
    


# In[ ]:


def play(player, grid):
    print(".......................")
    position = input(player['name']+", choose a position between 1-9:")
    position = int(position)
    
    if(grid[position-1]==" "):    
        grid[position-1] = player['symbol']
    else:
        print("Position unavailable. Try again!")
        play(player, grid)
    


# In[ ]:


def verifyPlayer(symbol, player1,player2):
    if(symbol==player1['symbol']):
        return 1
    elif(symbol==player2['symbol']):
        return 2

# In[ ]:


def verifyGrid(grid, player1, player2):
    if(grid[0]==grid[1] and grid[0]==grid[2] and grid[0]!=' '):
        verifyPlayer(grid[0], player1, player2)
    elif(grid[3]==grid[4] and grid[3]==grid[5] and grid[3]!=' '):
        verifyPlayer(grid[3], player1, player2)
    elif(grid[6]==grid[7] and grid[6]==grid[8] and grid[6]!=' '): 
        verifyPlayer(grid[6], player1, player2)
    elif(grid[0]==grid[3] and grid[0]==grid[6] and grid[0]!=' '):
        verifyPlayer(grid[0], player1, player2)
    elif(grid[1]==grid[4] and grid[1]==grid[7] and grid[1]!=' '):
        verifyPlayer(grid[1], player1, player2)
    elif(grid[2]==grid[5] and grid[2]==grid[8] and grid[2]!=' '):
        verifyPlayer(grid[2], player1, player2)
    elif(grid[0]==grid[4] and grid[0]==grid[8] and grid[0]!=' '):
        verifyPlayer(grid[0], player1, player2)
    elif(grid[2]==grid[4] and grid[2]==grid[6] and grid[2]!=' '):
        verifyPlayer(grid[2], player1, player2)
    
    else: 
        return 0
        


# ### Main starts here

# In[ ]:


start(player1, player2)
gridGuide()
while(endGame == False):
    #gridGuide()
    print()
    print()

    displayGrid(grid)
    play(player1, grid)
    winner = verifyGrid(grid, player1, player2)
    if(winner == 1):
        print(player1['name']+" won! Congratulations")
        endGame = True
    elif(winner == 2):
        print(player2['name']+" won! Congratulations")
        endGame = True
    elif(winner == 0):
        print('No winner so far')

    displayGrid(grid)
    play(player2, grid)
    displayGrid(grid)
    winner = verifyGrid(grid, player1, player2)
    if(winner == 1):
        print(player1['name']+" won! Congratulations")
        endGame = True
    elif(winner == 2):
        print(player2['name']+" won! Congratulations")
        endGame = True
    elif(winner == 0):
        print('No winner so far')

    print()
    clear_output()
    


# In[ ]:




