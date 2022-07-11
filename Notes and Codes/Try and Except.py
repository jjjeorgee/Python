try:    
    age = int(input('type age here for a surprise: '))
    print('you will be ' +str(age +1)+' in a year.')
except ValueError:
    print('error. enter integer please or this program will close ')
    age = int(input())
    print('you will be ' +str(age +1)+' in a year.')
except Exception:
    print('syntax error lol') 
finally:
    print('exiting...')