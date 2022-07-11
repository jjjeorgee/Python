def spam():      
    eggs = 'spam local'    
    print(eggs)    # prints 'spam local'

def bacon():      
    eggs = 'bacon local'    
    print(eggs)    # prints 'bacon local'    
    spam()         # prints 'spam local'
    print(eggs)    # prints 'bacon local'

eggs = 'global' 
bacon()            # prints 'bacon local'
print(eggs)        # prints 'global'

def tt():
    global boy
    boy = 12
    boy = boy + 11
    print(boy)
boy  = 11
tt()
print(boy)
print(boy) 

def ss():
    print(boy)
ss()

def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs) 

