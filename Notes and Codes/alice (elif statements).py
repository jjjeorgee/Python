print('hi')
print('what is your name')
name = input()

if name == 'Alice':
    print('Hi, Alice.') 
    print('how old are you?')
age = input()
if int(age) < 12:
    print('You are not Alice, kiddo.')
elif int(age) > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif int(age) > 100:
    print('You are not Alice, grannie.') 
