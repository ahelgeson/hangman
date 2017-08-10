# helgeson python hangman game
# import necessary modules
import random

#open, read word file and place into list array
with open("hang_words.txt") as w:
    word = w.readlines()

# Strip any whitespace after word
word = [x.strip("\n") for x in word]

# Choose word at random
selected_word = random.choice(word)

# creates a variable with an empty value
guesses = ''

# set number of turns
turns = 9

# set while loop to run game and
# check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in selected_word    
    for char in selected_word:      

    # check for the character in the guess
        if char in guesses:    
    
        # print out the letter
            print char,

        else:
    
        # if not found, print a dash
            print "_ ",     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero
    # print winning statement 
    # otherwise break loop and print
    # losing statement
    if failed == 0:        
        print " \nCongrats, you guessed it correctly!"
        print "The word was in fact, {}".format(selected_word)  

    # exit the script
        break              

    print

    # ask the user go guess a letter
    guess = raw_input("guess a letter:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in selected_word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print incorrect statement
        print "Incorrect, try again."    
 
    # how many turns are left
        print "You have", + turns, 'more guesses' 
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print lose statement and chosen word
            print "You're guessing is terrible."
            print "You Lose, and the word was {}".format(selected_word)  
