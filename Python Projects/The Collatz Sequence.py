from tkinter import W


def collatz(number):
    if number == 1:
        print('Loop completed')
    elif int(number) % 2 == 0:
        print(number//2)
        collatz(number//2)
    else:
        print(3 * int(number) + 1)
        (collatz(number*3+1)) 

collatz(9)
