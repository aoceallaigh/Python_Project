import numpy as np
import math
import random

def magic():
    newlist = [1,2]
    mag = random.choice(newlist)
    return mag

def goodbye():
    print('Goodbye, I wish you good fortune!')
    exit

def branch(b):
    if(b == 'exit'):
            goodbye()
    else:
        mag = magic()
        if(mag == 1):
            c = input('Hmmm...You will die a terrible, terrible death!')
        elif(mag ==2):
            c = input('You will find great success and fortune!')
        def play_again():
            c = input('would you like to play again? Type yes or exit: ')
            if(c == 'yes'):
                fortune()
            elif(c == 'exit'):
                goodbye()
            else:
                play_again()
        play_again()

def fortune():
    print('Four Roads Lie Before You:')
    mylist = ['red', 'green', 'blue', 'exit']
    for i in range(0,4):
        print(mylist[i])
    b = input('Choose your path!: ')
    if(b == mylist[0] or b ==  mylist[1] or b == mylist[2] or b == mylist[3]):
        branch(b)
    else:
        q = input('Fool! Try again!\n')
        if(q == 'exit'):
            goodbye()
        else:
            fortune()
    
    



a = input("Hello, welcome to my fortune telling repository!")

start = input("Would you like to know your future? Type yes or exit: ")
if(start == 'yes'):
    a = input('Very good, I can see you have a curious mind...')
    fortune()

elif(start == 'exit'):
    goodbye()



