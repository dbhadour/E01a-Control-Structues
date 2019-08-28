#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')
colors = ['red','orange','yellow','green','blue','violet','purple']  # this is an array of strings.
play_again = ''
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): #a while loop wit two conditions
    match_color = random.choice(colors) #picks a random color in the array
    count = 0
    color = '' # we reset the value assigned to color to hide the answer 
    while (color != match_color):
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line . here we answer the question
        color = color.lower().strip()
        count += 1 #since we have answered the question once it adds one to count and it will do it again if this while loop gets executed again.
        if (color == match_color):
            print('Correct!') 
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    print('\nYou guessed it in {0} tries!'.format(count))
    if (count < best_count): 
        print('This was your best guess so far!')
        best_count = count #it keeps track of our most number of guesses and if we play again and guess in less tries then that becomes the best count
    play_again = input("\nWould you like to play again? ").lower().strip()
print('Thanks for playing!')