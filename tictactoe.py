# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 19:19:38 2019

@author: Kriti Gupta
"""
import random
choices=[1,2,3,4,5,6,7,8,9]
def printmatrix():
    "Function to print the tictactoe matrix"
    print(choices[0],'|',choices[1],'|',choices[2])
    print('----------')
    print(choices[3],'|',choices[4],'|',choices[5])
    print('----------')
    print(choices[6],'|',choices[7],'|',choices[8])
    return
print("Lets's start the game!-->")
print("You = X\nComputer = O")
printmatrix()
for i in range(20):
    #while choices[0]!=choices[1] and choices[1]!=choices[2] or choices[3]!=choices[4] and choices[4]!=choices[5] or choices[6]!=choices[7] and choices[7]!=choices[8] or choices[0]!=choices[3] and choices[3]!=choices[6] or choices[1]!=choices[4] and choices[4]!=choices[7] or choices[2]!=choices[5] and choices[5]!=choices[8] or choices[0]!=choices[4] and choices[4]!=choices[8] or choices[2]!=choices[4] and choices[4]!=choices[6]:
    user=int(input('Enter a choice (1-9): '))
#    while choices[user-1]=='X' or choices[user-1]=='O' and user!=1 or user!=2 or user!=3 or user!=4 or user!=5 or user!=6 or user!=7 or user!=8 or user!=9:
#        print("Try Again!")
#        user=int(input('Enter a choice (1-9): '))
    choices[user-1]='X'
    printmatrix()
    if choices[0]==choices[1]==choices[2] or choices[3]==choices[4]==choices[5] or choices[6]==choices[7]==choices[8] or choices[0]==choices[3]==choices[6] or choices[1]==choices[4]==choices[7] or choices[2]==choices[5]==choices[8] or choices[0]==choices[4]==choices[8] or choices[2]==choices[4]==choices[6]:
        break
    
    print("Computer's turn")
    comp=user
    while choices[comp-1]=='X' or choices[comp-1]=='O':
        comp=random.randint(1,9)
    choices[comp-1]='O'
    printmatrix()
    
    if choices[0]==choices[1]==choices[2] or choices[3]==choices[4]==choices[5] or choices[6]==choices[7]==choices[8] or choices[0]==choices[3]==choices[6] or choices[1]==choices[4]==choices[7] or choices[2]==choices[5]==choices[8] or choices[0]==choices[4]==choices[8] or choices[2]==choices[4]==choices[6]:
        break
'''-----HOW TO SHOW OUTPUT FOR TIE????????------'''
if choices[0]==choices[1]==choices[2]=='X' or choices[3]==choices[4]==choices[5]=='X' or choices[6]==choices[7]==choices[8]=='X' or choices[0]==choices[3]==choices[6]=='X' or choices[1]==choices[4]==choices[7]=='X' or choices[2]==choices[5]==choices[8]=='X' or choices[0]==choices[4]==choices[8]=='X' or choices[2]==choices[4]==choices[6]=='X':
    print('You Win!')
else:
    print('Computer Wins!')
