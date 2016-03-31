

with open('/usr/share/dict/words', 'r') as list:
    for line in list:
        print(line, end='')


#BEGIN GAME
    #User must choose between EASY -- NORMAL -- HARD difficulty


#SECRET WORD IS CHOSEN
    #INFORM user of character length of said word


#USER GUESS
    #ASK user to input a letter choice
        #Both upper and lower case are acceptable
    #IF user enters invalid entry (e.g. more than one letter), inform them they
    #try again
    #If USER repeats a guess, do NOT take away a guess. INFORM them they've already
    #guessed that letter and ask them to try again.
    #If USER runs out of guesses (eight max), reveal the word to user and end game


#GUESS EVALUATION
    #Let the user know if letter appears in the SECRET WORD


#DISPLAY GUESS
    #Display the partially-guessed word, including letters that have not been guessed.
        #For example, if they've only gotten "a" and "e" in apple, print a _ _ _ e


#DISPLAY REMAINING GUESSES
    #INFORM user of remaining guess.
    #Users are only allowed 8 total guesses.


#GAME CONCLUSION
    #Game ends when user constructs FULL WORD or runs out of guesses


#GAME RE-INITIATION
    #Ask user if they wish to play again; if they reply positively, restart game
