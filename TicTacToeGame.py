from tkinter import *
from tkinter.ttk import *
import random
def nextTurn(row,column):
    global player
    if buttons[row][column]['text']=="" and checkWinner() is False:
        if player==players[0]:
            buttons[row][column]['text']=player
            if checkWinner() is False:
                player=players[1]
                label.config(text=(players[1]+" ->turn"))
            elif checkWinner() is True:
                label.config(text=(players[0]+" ->Wins"))
            elif checkWinner()=="Tie":
                label.config(text=("Tie!!!"))
        else:
            buttons[row][column]['text']=player
            if checkWinner() is False:
                player=players[0]
                label.config(text=(players[0]+" ->turn"))
            elif checkWinner() is True:
                label.config(text=(players[1]+" ->Wins"))
            elif checkWinner()=="Tie":
                label.config(text=("Tie!!!"))

def checkWinner():
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text']==buttons[row][2]['text'] !="" :
            buttons[row][0]
            buttons[row][1]
            buttons[row][2]
            return True
        
    for column in range(3):
        if buttons[0][column]['text']==buttons[1][column]['text']==buttons[2][column]['text'] !="" :
            buttons[0][column]
            buttons[1][column]
            buttons[2][column]
            return True
    
    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text'] != "":
        buttons[0][0]
        buttons[1][1]
        buttons[2][2]
        return True
    
    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text'] != "":
        buttons[0][2]
        buttons[1][1]
        buttons[2][0]
        return True
    
    elif emptySpaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column]
        return "Tie"
    
    else:
        return False
def emptySpaces():
    spaces=9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text']!="":
                spaces -=1
    if spaces == 0:
        return False
    else:
        return True
def newGame():
    global player
    player=random.choice(players)
    label.config(text=player + " ->text")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="")

window=Tk()
window.title("Tic Tac Toe")
players=["X","O"]
player=random.choice(players)
buttons=[[0,0,0],
         [0,0,0],
         [0,0,0]]
label=Label(text=player + " ->turn", font=('consolas',40))
label.pack(side="top")
resetBtn=Button(text="Re-Start Game", command=newGame)
resetBtn.pack(side="top")
frame=Frame(window)
frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column]=Button(frame, text="",width=5,command=lambda row=row, column=column: nextTurn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()


