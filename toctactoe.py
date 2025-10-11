import random as r
import numpy as n
print("How it works> \n You choose whether to go first or second \n Then you pick a number based on the diagram shown and then yay you play tictactoe, how nice")
gameboard = n.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
pfield = n.array([['', '', ''], ['', '', ''], ['','','']])
l = [1,2,3,4,5,6,7,8,9]
c0, c1 =0,0
counter = 0
game_on = 1
print(gameboard)
print(pfield)
def change_num_X(loc:int):
        global counter
        counter+=1
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
        print(pfield)
def change_num_O(loc:int):
        global counter
        counter+=1
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
        print(pfield)
def declare_win(playground):
        global pfield
        global game_on
        if (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='X') or (str(pfield[0,2])==str(pfield[1,1])==str(pfield[2,0])=='X'):
            print("Game Ended!\n Bot wins!")
            game_on = 0
            exit()
        if (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='O') or (str(pfield[0,2])==str(pfield[1,1])==str(pfield[2,0])=='O'):
            print("Game Ended!\n User wins!")
            game_on = 0
            exit()
        for i in range(0,3):
            if (pfield[i]==['X', 'X', "X"]).tolist()==[True, True, True]:
                print("Game ended!\n Bot wins!")
                game_on = 0
                exit()
            if (pfield[i]==['O', 'O', "O"]).tolist()==[True, True, True]:
                print("Game ended!\n User wins!")
                game_on = 0
                exit()
        for i in range(0,3):
            if (pfield[:, i]==['X', 'X', "X"]).tolist()==[True, True, True]:
                print("Game Ended\n Bot wins!")
                game_on = 0
                exit()
            if (pfield[:, i]==['O', 'O', "O"]).tolist()==[True, True, True]:
                print("Game Ended\n User wins!")
                game_on = 0
                exit()


def bot_plays(pick):
    global l
    global c1

    integer = r.choice(l)
    l.remove(integer)
    c1+=1
    if pick == 'X':
        change_num_O(integer)
    elif pick == 'O':
        change_num_X(integer)
    

# def win():
#     # if []
#     global pfield
#     for i in range(0,3):
#         if (pfield[i]==['X', 'X', "X"]).tolist()==[True, True, True] or (pfield[i]==['O', 'O', "O"]).tolist()==[True, True, True]:
#             break
#     for i in range(0,3):
#         if (pfield[:, i]==['X', 'X', "X"]).tolist()==[True, True, True] or (pfield[:, i]==['O', 'O', "O"]).tolist()==[True, True, True]:
#             break
#     if (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='X') or (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='O') or (str(pfield[0,3])==str(pfield[1,1])==str(pfield[3,0])=='X') or (str(pfield[0,3])==str(pfield[1,1])==str(pfield[3,0])=='O'):
#         pass
def win():
    # if []
    global pfield
    if (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='X') or (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='O') or (str(pfield[0,3])==str(pfield[1,1])==str(pfield[3,0])=='X') or (str(pfield[0,3])==str(pfield[1,1])==str(pfield[3,0])=='O')==False:
        for i in range(0,3):
            if (pfield[i]==['X', 'X', "X"]).tolist()==[True, True, True] or (pfield[i]==['O', 'O', "O"]).tolist()==[True, True, True]:
                print("Game ended!")
                
        for i in range(0,3):
            if (pfield[:, i]==['X', 'X', "X"]).tolist()==[True, True, True] or (pfield[:, i]==['O', 'O', "O"]).tolist()==[True, True, True]:
                print("Game Ended")

def first():
    global counter
    global l
    global c0, c1
    p ='X'
    game_on = 1
    while True:
        i = int(input("Enter the location: "))
        print("You play: ")
        change_num_X(i)
        l.remove(i)

        global pfield
        if (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='X') or (str(pfield[0,2])==str(pfield[1,1])==str(pfield[2,0])=='X'):
            print("Game Ended!\n User wins!")
            game_on = 0
            break
        if (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='O') or (str(pfield[0,2])==str(pfield[1,1])==str(pfield[2,0])=='O'):
            print("Game Ended!\n Bot wins!")
            game_on = 0
            break
        for i in range(0,3):
            if (pfield[i]==['X', 'X', "X"]).tolist()==[True, True, True]:
                print("Game ended!\n User wins!")
                game_on = 0
                break
            if (pfield[i]==['O', 'O', "O"]).tolist()==[True, True, True]:
                print("Game ended!\n Bot wins!")
                game_on = 0
                break
        for i in range(0,3):
            if (pfield[:, i]==['X', 'X', "X"]).tolist()==[True, True, True]:
                print("Game Ended\n User wins!")
                game_on = 0
                break
            if (pfield[:, i]==['O', 'O', "O"]).tolist()==[True, True, True]:
                print("Game Ended\n Bot wins!")
                game_on = 0
                break
        # if c0>c1 or c0 == c1:
        #     print("user wins!")
        # else:
        #     print("bot wins!")
        if game_on == 0:
            exit()
        else:
            if counter == 9:
                print("It's a draw!")
                exit()
            else:
                print("Bot plays:")
                bot_plays(p)
                if (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='X') or (str(pfield[0,2])==str(pfield[1,1])==str(pfield[2,0])=='X'):
                    print("Game Ended!\n User wins!")
                    game_on = 0
                    exit()
                if (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='O') or (str(pfield[0,2])==str(pfield[1,1])==str(pfield[2,0])=='O'):
                    print("Game Ended!\n Bot wins!")
                    game_on = 0
                    exit()
                for i in range(0,3):
                    if (pfield[i]==['X', 'X', "X"]).tolist()==[True, True, True]:
                        print("Game ended!\n User wins!")
                        game_on = 0
                        exit()
                    if (pfield[i]==['O', 'O', "O"]).tolist()==[True, True, True]:
                        print("Game ended!\n Bot wins!")
                        game_on = 0
                        exit()
                for i in range(0,3):
                    if (pfield[:, i]==['X', 'X', "X"]).tolist()==[True, True, True]:
                        print("Game Ended\n User wins!")
                        game_on = 0
                        exit()
                    if (pfield[:, i]==['O', 'O', "O"]).tolist()==[True, True, True]:
                        print("Game Ended\n Bot wins!")
                        game_on = 0
                        exit()

def second():
    global counter
    global c0, c1
    global l
    p = 'O'
    game_on = 1
    while True:
        print("Bot plays: ")
        bot_plays(p)

        global pfield
        if (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='X') or (str(pfield[0,2])==str(pfield[1,1])==str(pfield[2,0])=='X'):
            print("Game Ended!\n Bot wins!")
            game_on = 0
            break
        if (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='O') or (str(pfield[0,2])==str(pfield[1,1])==str(pfield[2,0])=='O'):
            print("Game Ended!\n User wins!")
            game_on = 0
            break
        for i in range(0,3):
            if (pfield[i]==['X', 'X', "X"]).tolist()==[True, True, True]:
                print("Game ended!\n Bot wins!")
                game_on = 0
                break
            if (pfield[i]==['O', 'O', "O"]).tolist()==[True, True, True]:
                print("Game ended!\n User wins!")
                game_on = 0
                break
        for i in range(0,3):
            if (pfield[:, i]==['X', 'X', "X"]).tolist()==[True, True, True]:
                print("Game Ended\n Bot wins!")
                game_on = 0
                break
            if (pfield[:, i]==['O', 'O', "O"]).tolist()==[True, True, True]:
                print("Game Ended\n User wins!")
                game_on = 0
                break

        if game_on == 0:
            break
            
        else:
            if counter == 9:
                print("It's a draw!")
                exit()
            else:
                i = int(input("Enter the location: "))
                c0+=1
                print("User plays:")
                change_num_O(i)
                l.remove(i)
                if (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='X') or (str(pfield[0,2])==str(pfield[1,1])==str(pfield[2,0])=='X'):
                    print("Game Ended!\n Bot wins!")
                    game_on = 0
                    exit()
                if (str(pfield[0,0])==str(pfield[1,1])==str(pfield[2,2])=='O') or (str(pfield[0,2])==str(pfield[1,1])==str(pfield[2,0])=='O'):
                    print("Game Ended!\n User wins!")
                    game_on = 0
                    exit()
                for i in range(0,3):
                    if (pfield[i]==['X', 'X', "X"]).tolist()==[True, True, True]:
                        print("Game ended!\n Bot wins!")
                        game_on = 0
                        exit()
                    if (pfield[i]==['O', 'O', "O"]).tolist()==[True, True, True]:
                        print("Game ended!\n User wins!")
                        game_on = 0
                        exit()
                for i in range(0,3):
                    if (pfield[:, i]==['X', 'X', "X"]).tolist()==[True, True, True]:
                        print("Game Ended\n Bot wins!")
                        game_on = 0
                        exit()
                    if (pfield[:, i]==['O', 'O', "O"]).tolist()==[True, True, True]:
                        print("Game Ended\n User wins!")
                        game_on = 0
                        exit()

def tttgame():
    choice = input("Wheather you want to go first or second (f/s): ")
    if choice == 'f':
        first()
    elif choice == 's':
        second()
    else:
        exit()
tttgame()
