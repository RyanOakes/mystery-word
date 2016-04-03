import re
import random

# def mystery_word():

# def main():

def clean_text(word):
    return word.lower().strip()


def game_initation():
    print("""Welcome to Mystery Word!

You can choose from three difficultly levels.
Type 'e' for easy.
Type 'm' for medium.
Type 'h' for hard.\n""")

    while True:

        try:

            if len(input) > 1:
                print("Not legit! Please try again!")

            if input != 'e':
                print("Hey, that's not acceptable!")

            elif input != 'm':
                print("Hey, that's not acceptable!")

            elif input != 'h':
                print("Hey, that's not acceptable!")



    return input("What will it be? ")


def create_the_list_easy(list):
    for word in master_words_list:
        if  len(word) >= 4 and len(word) <= 6:
            easy_list.append(word)


def create_the_list_medium(list):
    for word in master_words_list:
        if len(word) > 5 and len(word) <= 8:
            medium_list.append(word)


def create_the_list_hard(list):
    for word in master_words_list:
        if len(word) >= 8:
            hard_list.append(word)


def choosing_game_difficulty(input):

    while True:
        try:
            if len(input) > 1:
                print("Not legit! Please try again!")

            if input != 'e':
                print("Hey, that's not acceptable!")

            elif input != 'm':
                print("Hey, that's not acceptable!")

            elif input != 'h':
                print("Hey, that's not acceptable!")

        except ValueError:
            print("Nice try mortal, but blah isn't a number! Please guess again: ")

        if input == 'e':
            return list(random.choice(easy_list))

        elif input == 'm':
            return list(random.choice(medium_list))

        elif input == 'h':
            return list(random.choice(hard_list))


def inform_user_of_word_length():
    print("\nOK, here's a hint; your secret word is {} characters long. Good luck! ".format(len(secret_word)))



def initiate_core_game():

    correct_guesses = []
    while len(correct_guesses) < 8:

        try:
            print(secret_word)
            display_guesses(secret_word, correct_guesses)
            user_letter_guess = input('\nGimme a letter please: ')

            if user_letter_guess in correct_guesses:
                print("Hey, you already guessed that! Try again!")
                continue

            if len(user_letter_guess) > 1:
                print("Hey, I said one letter! Try again!")
                continue

            else:
                correct_guesses += user_letter_guess
                continue



        except ValueError:
            print("{} isn't a number!".format(guess))
            continue

        else:
            print("WE MUST GET THIS FAR!")
            print(correct_guesses)
            display_guesses(secret_word, correct_guesses)



    else:
        print("WANNA PLAY AGAIN!?")

        if play_again.lower() != 'n':
            guessing_game()
        else:
            print("\nUntil next time, human!")




def display_guesses(secret_word, correct_guesses):

    for letter in secret_word:
        if letter in correct_guesses:
            print(letter.upper(), end=" ")

        else:
            print("_", end=" ")






################################################################################

easy_list = []
medium_list = []
hard_list = []
master_words_list = []
total_guesses = []

with open('/usr/share/dict/words', 'r') as text_doc:

    for word in text_doc:

        cleansed_word = clean_text(word)

        master_words_list.append(cleansed_word)

    create_the_list_easy(master_words_list)
    create_the_list_medium(master_words_list)
    create_the_list_hard(master_words_list)



user_game_mode = game_initation() #Starts the game


secret_word = choosing_game_difficulty(user_game_mode) #User selects game difficulty/secret word is chosen


inform_user_of_word_length() #Inform user of secet word's length

initiate_core_game()


# def core_game()):
#
#     try:
#         user_letter_guess = input('\nGimme a letter please: ')
        # correct_guesses += user_letter_guess
        # total_guesses += user_letter_guess
#         if len(user_letter_guess) > 1:
#             print("Hey, I said one letter! Try again!")

#         if user_letter_guess in total_guesses:
#             print("Hey, you already guessed that! Please try again.")
#
#     except ValueError:
#         print("{} isn't a number!".format(guess))
#
#     else:
#         print("What")
#
#     print(correct_guesses)
#
#
#     display_guesses(secret_word, correct_guesses)
#
# print("\nThanks for playing you fuck!")
# # secret_word_with_blanks = len(secret_word) * " _ "
# # print(secret_word_with_blanks)
#
# A user loses a guess only when they guess incorrectly. If they guess a letter
# that is in the computer's word, they do not lose a guess.
#
# If the user guesses the same letter twice, do not take away a guess. Instead,
#  print a message letting them know they've already guessed that letter and ask them to try again.



# def initiate_core_game():
#
#     while len(total_guesses) < 8:
#
#         try:
#             user_letter_guess = input('\nGimme a letter please: ')
#
#                 if len(user_letter_guess) > 1:
#                     print("Hey, I said one letter! Try again!")
#
#
#                 if user_letter_guess in total_guesses:
#                 print("Hey, you already guessed that! Please try again.")
#
#         except ValueError:
#             print("{} isn't a number!".format(guess))
#
#         else:
#             print("What")
#
#         print(correct_guesses)
#
#
#         display_guesses(secret_word, correct_guesses)

#
# try:
#     user_letter_guess = input('\nGimme a letter please: ')
#     correct_guesses += user_letter_guess
#     total_guesses += user_letter_guess
#     if len(user_letter_guess) > 1:
#         print("Hey, I said one letter! Try again!")
#
#     if user_letter_guess in total_guesses:
#         print("Hey, you already guessed that! Please try again.")
#
# except ValueError:
#     print("{} isn't a number!".format(guess))
#
# else:
#     print("What")
#
# print(correct_guesses)
#
#
# display_guesses(secret_word, correct_guesses)
#
#
#
#
#
#
#
#
#
#
# # for letter in secret_word:
# # ​   if letter in correct_guesses:
# #         print(letter.upper(), end=" ")
# #
# #     else:
# #         print("_", end=" ")
#
#
# # def display_visual_guesses(secret_word, correct_guesses):
# #
# #     for letter in secret_word:
# # ​
# #         if letter in correct_guesses:
# #             print(letter.upper(), end=" ")
# #
# #         else:
# #             print("_", end=" ")
# # adding to dic
# #                 if word in word_count:
# #
# #                 if word not in word_count
# #                     word_count[word] = 1
# #
# #                 else:
# #                     word_count[word] += 1
#
#
#

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
