import random
answerNumber = ['It is certain', 
'It is decidedly so',
'Yes', 
'Reply hazy try again', 
'It is certain', 
'My reply is no',
'Outlook not so good', 
'Very doubtful', 
'Ask again later',
'Concentrate and ask again']
r = random.randint(0, 8)
print(answerNumber[r])