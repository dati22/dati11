#!/usr/bin/env python
# coding: utf-8

# In[3]:


board = [1,2,3,4,5,6,7,8,9]
def drawBoard(board):
    print ("-------------")
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-------------")
drawBoard(board)


# In[ ]:


def takeInput(playerToken):
    valid = False
    while not valid:
        playerAnswer = input("куда поставим" + playerToken+"? ")
        if not IsvalidInput(playerAnswer):
            continue
        playerAnswer = Int(playerAnswer)
        if(playerAnswer >= 1 and  playerAnswer<= 9):
            if(str(board[playerAnswer-1]) not in "X0"):
                board[playerAnswer-1] = playerToken
                valid = True
            else:
                print("эта клетка уже занята!")
        else:
            print("некорректный ввод. Введите число от 1 до 9.")
def IsvalidInput(playerAnswer):
    try:
        playerAnswer = Int(playerAnswer)
        return True
    except:
        print("некорректный ввод. вы уверены, что ввели число?")
        return False
takeInput("X")
drawBoard(board)
takeInput("O")
drawBoard(board)


# In[ ]:


def checkwin(board):
    winCoords = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for coord in winCoords:
        if board[coord[0]] == board[coord[1]] == board[coord[2]]:
            return board[coord[0]]
        return False
    tmpBoard = ["X","X","X",4,5,6,7,8,9]
    checkWin(tmpBoard)
    tmpBoard = ["X","O","X",4,5,6,7,8,9]
    checkWin(tmpBoard)

