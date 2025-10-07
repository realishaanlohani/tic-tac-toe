import numpy as n
print("How it works> \n You choose whether to go first or second \n Then you pick a number based on the diagram shown and then yay you play tictactoe, how nice")
gameboard = n.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])

pfield = n.array([['', '', ''], ['', '', ''], ['','','']])
print(pfield)
print(gameboard)
def win():
    # if []
    pass
def first():
    pass
def second():
    pass
def choice():
    a = input("Wheather you want to go first or second (f/s): ")
    if a == 'f':
        first()

    elif a == 's':
        second()