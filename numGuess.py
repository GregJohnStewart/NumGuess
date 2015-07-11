# numGuess
# V1.1
# Number Guessing game!
# Generates a number, and then the user tries to guess it. Keeps track of high scores and allows the deletion of those scores.
# Greg Stewart
# Copyright Greg Stewart 2014
# Using python 2.7.6
# you can edit to your liking, just please give me credit
#

# import needed things
import random
import time
import math
import os.path

#global variables
playing = 'y' # are they playing or not?
choice = "null" # difficulty choice
guesses_left = 0 # how many guesses are left
guesses_made = 0 # how many guesses are made
number = 0 #the number the user tries to guess
score = 0 #the player's score
PlayThisRound = 'false' # are they playing the game this time around the loop?
exiting = 'false' # are we exiting?
goBack = 'false' # to skip ending stuff

# //////////////
# worker classes
# //////////////
def showHS():# shows the highscores
    hs = open(".highScores.hs", "r")
    easy_s = hs.readline()
    easy_s = easy_s.rstrip('\n')
    easy_p = hs.readline()
    med_s = hs.readline()
    med_s = med_s.rstrip('\n')
    med_p = hs.readline()
    hard_s = hs.readline()
    hard_s = hard_s.rstrip('\n')
    hard_p = hs.readline()
    imp_s = hs.readline()
    imp_s = imp_s.rstrip('\n')
    imp_p = hs.readline()
    hs.close()
    print "\nHere are the High Scores!\n \
Difficulty:            Score:     Player:\n \
Easy:                  {0}         {1} \
Medium:                {2}         {3} \
Hard:                  {4}         {5} \
Impossible:            {6}         {7}".format(easy_s,easy_p,med_s,med_p,hard_s,hard_p,imp_s,imp_p)

#to see if the highScores file is present, if not, make it           
def testHSPresent():
    if os.path.exists('.highScores.hs'):
    	print "Highscores Present!"
    else:
        hs = open(".highScores.hs", "w")
        hs.write(str("0000"))
        hs.write('\n')
        hs.write("n/a")
        hs.write('\n')
        hs.write(str("0000"))
        hs.write('\n')
        hs.write("n/a")
        hs.write('\n')
        hs.write(str("0000"))
        hs.write('\n')
        hs.write("n/a")
        hs.write('\n')
        hs.write(str("0000"))
        hs.write('\n')
        hs.write("n/a")
        hs.close()
        print "Highscore file created."

    


# /////////////
# start program
# /////////////

#intro stuff
print "NumGuess\n\
Py Guessing Game\n\
Author: Greg Stewart\n\
Copyright 2014 Greg Stewart\n\
Version: 1.1\n\
Classic number guessing game!"
testHSPresent();
	
#start of game loop	
while playing == 'y' or playing == 'Y':  #while plying
    #reset variables
    guesses_made = 0      
    score = 0
    goBack = 'false'
    playThisRound = 'true'
    exiting = 'false'
    upperNum = 0
    lowerNum = 1
    #ask for what difficulty to play
    print "\nWhat difficulty would you like to play, or what would you like to do?\n\
    Difficulty:       Num Range:           # chances:\n \
   Easy:             1-100                10\n \
   Medium:           1-10,000             15\n \
   Hard:             1-500,000            20\n \
   Impossible:       1-1,000,000          15"
    try:
        choice = str(raw_input("Choices: (E/M/H/I;HighScores/Exit): "))
    except:
        print "A typo was made. Please try again."
        choice = 'f'    
        
    # set guesses_left and get appropriate random int, or display high scores or set to exit
    if choice == 'E' or choice == 'e':
        guesses_left = 10
        number = random.randint(1,100)
        upperNum = 100
    elif choice == "M" or choice == "m":
        guesses_left = 15
        number = random.randint(1,10000)
        upperNum = 10000
    elif choice == "H" or choice == "h":
        guesses_left = 20
        number = random.randint(1,500000)
        upperNum = 500000
    elif choice == "I" or choice == "i":
        guesses_left = 15
        number = random.randint(1,1000000)
        upperNum = 1000000
    elif choice == "HighScores" or choice == "highscores" or  choice == "Highscores" or  choice == "highScores" or choice == "h" or choice == "H":
        playThisRound = 'false'
        showHS()
        goBack = 'true'
        try:
            clearHS = str(raw_input('Do you want to clear the high Scores? (YES/n): '))
        except:
            clearHS = "f"

        if clearHS != "YES":
            print "Returning to main prompt."
        elif clearHS == "YES":
            hs = open(".highScores.hs", "w")
            hs.write(str("0000"))
            hs.write('\n')
            hs.write("n/a")
            hs.write('\n')
            hs.write(str("0000"))
            hs.write('\n')
            hs.write("n/a")
            hs.write('\n')
            hs.write(str("0000"))
            hs.write('\n')
            hs.write("n/a")
            hs.write('\n')
            hs.write(str("0000"))
            hs.write('\n')
            hs.write("n/a")
            hs.close()
            print "Highscores Cleared"
        else:
            print "Sorry invalid input. going back to main prompt"
        
    elif choice == "exit" or choice == "Exit":
        playThisRound = 'false'
        exiting = 'true'
    else:
        print "oops! invalid input. Please try again."
        playThisRound = 'false'
        
    #play the actual game and take start time
    #number = 1    # to set a number, for debugging
    start = time.time()
    while guesses_left != 0 and playThisRound != 'false': # while they havent'guessed the number and they input a correct input
        print "\n"
        
        #print "tip: {0}".format(number) # to show the answer to the user, debugging purposes
        print "Between {0} and {1}".format(lowerNum,upperNum)
        print 'Guesses Left: {0}'.format(guesses_left)
        
        #try/ catch in case they don't enter an int
        try:
            print  'Take a guess: ({0}-{1} - 0 to quit) '.format(lowerNum,upperNum)
            guess = int(raw_input("Guess: "))
        except:
            guess = 'typo'
        
        
        if guess == 0:
            goBack = 'true'
            print "Game exited"
            break
        elif guess >= lowerNum and guess <= upperNum:
            
            guesses_made += 1
            guesses_left -= 1
            if guess < number:
                print 'Your guess is too low.'
                
                lowerNum = guess
            if guess > number:
                print 'Your guess is too high.'
                upperNum = guess
            if guess == number:
                break

        else:
            print "A typo was made. Please try again."
    
    #take ind time, and calculate time elapsed
    end = time.time()
    tScore = end - start
    
    #how to handle postgame things
    if exiting == 'true':#if exiting the program
        choice2 = str(raw_input('Are you sure? (y/n): '))
        if choice2 == 'y' or choice2 == 'Y':
            playing = 'n'
        elif choice2 == 'n' or choice2 == 'N':
            playing = 'y'
    elif goBack == 'true':#to just skip if need be, resets goBack
    	goBack == 'false'
    elif guess == number and playThisRound == 'true':#if you won the game
        #sets guesses left to 1, so your score isn't 0
        if guesses_left == 0:
            guesses_left = 1
        
        #calculate score and round off zeros
        score = ((5*60) - tScore) * guesses_left
        score = int(math.floor(score))
        tScore = round(tScore, 2)
        
        #output stats and retrieve current highScores
        print 'Good job! You guessed my number ( {0} ) with {1} guesses, in {2}secs!\n Total Score: {3}'.format(number, guesses_made,tScore,score)
        hs = open(".highScores.hs", "r")
        easy_s = hs.readline()
        easy_s = easy_s.rstrip('\n')
        easy_p = hs.readline()
        easy_p = easy_p.rstrip('\n')
        med_s = hs.readline()
        med_s = med_s.rstrip('\n')
        med_p = hs.readline()
        med_p = med_p.rstrip('\n')
        hard_s = hs.readline()
        hard_s = hard_s.rstrip('\n')
        hard_p = hs.readline()
        hard_p = hard_p.rstrip('\n')
        imp_s = hs.readline()
        imp_s = imp_s.rstrip('\n')
        imp_p = hs.readline()
        imp_p = imp_p.rstrip('\n')
        hs.close()
        highScore = 'false'
        
        #decide whether or not you got a high score in the appropriate difficulty. If so, record your name and score
        if (choice == "e" or choice == "E") and score > int(easy_s) :
            print "highscore!!"
            easy_s = score
            enteredName = 'false'
            while enteredName == 'false':
                try:
                    easy_p = str(raw_input('Enter your name: '))
                    enteredName = 'true'
                except:
                    print "oops, typo. try again."
            highScore = 'true'

        elif choice == "m" or choice == "M" and score > int(med_s) :
            print "highscore!!"
            med_s = score
            enteredName = 'false'
            while enteredName == 'false':
                try:
                    med_p = str(raw_input('Enter your name: '))
                    enteredName = 'true'
                except:
                    print "oops, typo. try again."
            highScore = 'true'

        elif choice == "h" or choice == "H" and score > int(hard_s) :
            print "highscore!!"
            hard_s = score
            enteredName = 'false'
            while enteredName == 'false':
                try:
                    hard_p = str(raw_input('Enter your name: '))
                    enteredName = 'true'
                except:
                    print "oops, typo. try again."
            highScore = 'true'

        elif choice == "i" or choice == "I" and score > int(imp_s) :
            print "highscore!!"
            imp_s = score
            enteredName = 'false'
            while enteredName == 'false':
                try:
                    imp_p = str(raw_input('Enter your name: '))
                    enteredName = 'true'
                except:
                    print "oops, typo. try again."
            highScore = 'true'

        # if there was a new highscore, write it to file
        if highScore == "true":
            hs = open(".highScores.hs", "w")
            hs.write(str(easy_s))
            hs.write('\n')
            hs.write(easy_p)
            hs.write('\n')
            hs.write(str(med_s))
            hs.write('\n')
            hs.write(med_p)
            hs.write('\n')
            hs.write(str(hard_s))
            hs.write('\n')
            hs.write(hard_p)
            hs.write('\n')
            hs.write(str(imp_s))
            hs.write('\n')
            hs.write(imp_p)
            hs.close()
        showHS();
        playing = str(raw_input('Want to play again? (y/n): '))
        showHS()
        
    #if you didnt guess it
    elif guess != number and playThisRound == 'true':
        print 'Nope. The number I was thinking of was {0}'.format(number)
        playing = str(raw_input('Want to play again? (y/n): '))
        showHS()
print 'Goodbye'   
#end program
