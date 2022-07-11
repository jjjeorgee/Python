catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    catNames = catNames + [name]
    if name == '': 
         break
print('The cat names are:')
for name in catNames:    
    print(name)
