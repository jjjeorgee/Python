print('Defining functions')
def hello():  
    print('Howdy!')    
    print('Howdy!!!')    
    print('Hello there.')
hello() 

def name():
    print(3+2)
name()

#Local and Global variables

print('Local and Global variables ')
eggs = 21       #Global variable

def hi(name):
    print('Hi' + ' ' +name + ', you are welcome')
hi('Bob') 
hi('Peace') 

print('Hello',  end=', ') 
print('World')
print('cats', 'dogs', 'mice',  sep='/') 

def spam():     #Local variable
    eggs = 31337
spam()
print(eggs)

def spem():    
    egg = 99   
    bacon()    
    print(egg)

def bacon():
    ham = 101
    egg = 0
    print(egg)
spem()
bacon()

def spom():
    print(eggs)
spom()
print(eggs)