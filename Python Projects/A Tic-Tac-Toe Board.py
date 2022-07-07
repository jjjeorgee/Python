theBoard = {'TL': ' ', 'TM': ' ', 'TR': ' ',
            'ML': ' ', 'MM': ' ', 'MR': ' ',
            'LL': ' ', 'LM': ' ', 'LR': ' '}
# T = Top M = Middle L = Low
def printBoard(board):    
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])    
    print('-+-+-')    
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])    
    print('-+-+-')    
    print(board['LL'] + '|' + board['LM'] + '|' + board['LR']) 
    
turn = 'X' 
for i in range(9):
        printBoard(theBoard)    
        print('Turn for ' + turn + '. Move on which space?') 
        move = input()
        theBoard[move] = turn 
        if turn == 'X':        
            turn = 'O'    
        else:        
            turn = 'X'
printBoard(theBoard)
