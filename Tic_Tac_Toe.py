#Program for implementing tic tac toe game

print("######TIC TAC TOE GAME######")
print("The rules of the game are:")
print('''1.You,player 'O' can start the game by placing 'O' only at the diagonals
for the first round but you can place 'O' anywhere in the rest of the rounds''')
print("2.Positions of 'O' shall be inserted using 'x' and 'y' coordinates")
print("3.The diagonals will not be evaluated. Only top to bottom and left to right will be counted")
print("4.There are totally 3 rounds")
import random
def display(l):
    for row in l:
        for entry in row:
            print(entry,end=' ')
        print(' ')
        
for rounds in range(1,4):
    print("Welcome to round",i)
    moves=1
    L=[['__','__','__' ],['__','__','__' ],['__','__','__' ]]
    display(L)
    print("Positions are (0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)")
    print("Diagonal positions are (0,0),(1,1),(2,2)")
    for i in range(len(L)):
        for j in range(len(L))
    print("Your turn")
    x=int(input("Enter the x coordinate for 'O' within the diagonals:"))
    y=int(input("Enter the y coordinate for 'O' within the diagonals:"))
    if moves==1:
        if x==y:
            L[x][y]='O'
            display(L)
            moves+=1
        else:
            print("OOPS! You can't start the first round with non-diagonal position")
    else:
        L[x][y]='O'
        moves+=1
        display(L)
    


