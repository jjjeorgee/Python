#if everyone on earth fought, how many people would the winner have to fight ?

#Answer using a function
def pop(number):
    if number==1:
        print('done')
    else:
        print (number//2)
        pop(number//2)

print(pop(8000000000))

#Answer using while loop
number = int(input('Type ur number boss: '))
while True:
    print(number//2)
    number = number//2
    if number == 1:
        break