import random as r
import numpy as n
print("How it works> \n You choose whether to go first or second \n Then you pick a number based on the diagram shown and then yay you play tictactoe, how nice")
gameboard = n.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
pfield = n.array([['', '', ''], ['', '', ''], ['','','']])
l = [1,2,3,4,5,6,7,8,9]
print(gameboard)
print(pfield)
def change_num_X(loc:int):
        global pfield
        if loc == 1:
            pfield[0,0] = 'X'
        elif loc == 2:
            pfield[0,1] = 'X'
        elif loc == 3:
            pfield[0,2] = 'X'
        elif loc == 4:
            pfield[1,0] = 'X'
        elif loc == 5:
            pfield[1,1] = 'X'
        elif loc == 6:
            pfield[1,2] = 'X'
        elif loc == 7:
            pfield[2,0] = 'X'
        elif loc == 8:
            pfield[2,1] = 'X'
        elif loc == 9:
            pfield[2,2] = 'X'
        else:
            print("Invalid!")
def change_num_O(loc:int):
        global pfield
        if loc == 1:
            pfield[0,0] = 'O'
        elif loc == 2:
            pfield[0,1] = 'O'
        elif loc == 3:
            pfield[0,2] = 'O'
        elif loc == 4:
            pfield[1,0] = 'O'
        elif loc == 5:
            pfield[1,1] = 'O'
        elif loc == 6:
            pfield[1,2] = 'O'
        elif loc == 7:
            pfield[2,0] = 'O'
        elif loc == 8:
            pfield[2,1] = 'O'
        elif loc == 9:
            pfield[2,2] = 'O'
        else:
            print("Invalid!")
def declare_win():
    pass
def bot_plays(pick):
    
    integer = r.choice(l)
    l.pop(integer)
    if pick == 'X':
        change_num_O(integer)
    elif pick == 'O':
        change_num_X(integer)

def win():
    # if []
    global pfield
    for i in range(0,3):
        if (pfield[i]==['X', 'X', "X"]).tolist()==[True, True, True] or (pfield[i]==['O', 'O', "O"]).tolist()==[True, True, True]:
            break
    for i in range(0,3):
        if (pfield[:, i]==['X', 'X', "X"]).tolist()==[True, True, True] or (pfield[:, i]==['O', 'O', "O"]).tolist()==[True, True, True]:
            break
    if (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='X') or (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='O') or (str(pfield[0,3])==str(pfield[1,1])==str(pfield[3,0])=='X') or (str(pfield[0,3])==str(pfield[1,1])==str(pfield[3,0])=='O'):
        pass

def first():
    p ='X'
    i = int(input("Enter the location: "))
    change_num_X(i)
    bot_plays(p)
    pass


def second():
    p = 'O'
    i = int(input("Enter the location: "))
    bot_plays(p)
    change_num_O(i)
    pass

def choice():
    a = input("Wheather you want to go first or second (f/s): ")
    if a == 'f':
        first()
    elif a == 's':
        second()


