from tkinter import W

#creating a collatz sequence with python 
def collatz(number):
    if number == 1:
        print('Loop completed')
    elif int(number) % 2 == 0:
        print(number//2)
        collatz(number//2)
    else:
        print(3 * int(number) + 1)
        (collatz(number*3+1)) 

#input validation 
try:
    collatz(int(input('Input an integer greater than 1: ')))
except ValueError:
    print('None integer detected', end =', ')
    print('Program will close now.')
