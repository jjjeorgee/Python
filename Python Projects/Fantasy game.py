Inventory = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6,
             'dagger': 1}

def displayInventory(stuff):
    print('Inventory:')
    total_items = 0
    for keys, values in stuff.items():
        total_items = total_items + stuff.get(stuff, 0)
        
    print("Total number of items: " + str(total_items))

displayInventory(Inventory)