import time

name = input('What\'s your name?')

print(name , 'Start hangman game!')

word = 'secret'
guesses = ''
turns = 10
while turns>0:
    fail = 0
    for char in word:
        
        if char in guesses:
            print(char, end=' ')

        else:
            
            print('_',end=' ')
            fail += 1
    if fail == 0 :
        print()
        print('Correct!')
    
        break
    print()

    guess = input("guess!")
    guesses += guess
    if guess not in word:
        turns -= 1
        print('Wrong..')
        print('More guess!')
        if turns == 0:
           print('You\'r fail...')  