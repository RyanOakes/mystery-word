import re
import random

# def mystery_word():

# def main():

def clean_text(word):
    return word.lower().strip()


def game_initation():
    print("""Welcome to Mystery Word!

You may choose from three difficultly levels.
Type 'e' for easy.
Type 'm' for medium.
Type 'h' for hard.\n""")
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

    try:
        if len(input) > 1:
            print("Not legit! Please try again!")

    except TypeError:
        print("Please enter 'e' for Easy, 'm' for Medium, or 'h' for Hard: ")

    if input == 'e':
        return list(random.choice(easy_list))

    elif input == 'm':
        return list(random.choice(medium_list))

    elif input == 'h':
        return list(random.choice(hard_list))


def inform_user_of_word_length():
        print("\nOK, here's a hint; your secret word is {} characters long. Good luck!\n ".format(len(secret_word)))



def initiate_core_game():

    correct_guesses = []
    print(secret_word)
    while len(correct_guesses) < 8:

        try:
            #print(secret_word)
            display_guesses(secret_word, correct_guesses)
            user_letter_guess = input('\nGimme a letter please: ')

            if user_letter_guess in correct_guesses:
                print("\nHey, you already guessed that letter! Try again!\n")
                continue

            if len(user_letter_guess) > 1:
                print("\nHey, I said one letter! Try again!\n")
                continue

            # if "_" in secret_word:
            #     break

            else:
                correct_guesses += user_letter_guess
                print("\nRemember, you only get eight guesses! You've made {} thus far.\n".format(len(correct_guesses)))
                continue



        except ValueError:
            print("{}  is unacceptable!".format(guess))
            continue

        else:
            print("WE MUST GET THIS FAR!")
            print(correct_guesses)
            display_guesses(secret_word, correct_guesses)



    else:
        play_again = input('Wanna play again? Type "Y" if you desire a rematch! ')

        if play_again.upper() == 'Y':
            initiate_core_game()
        else:
            print("\nUntil next time!\n")


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


inform_user_of_word_length() #Inform user of secret word's length


initiate_core_game() #Initiate main game
