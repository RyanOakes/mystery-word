import re
#
# def mystery_word():

# def main():



def create_list(word):
    return word.split()
    cleansed_word = word.split()
    return cleansed_word




master_words_list = []
with open('/usr/share/dict/words', 'r') as master_list:

    for word in master_list:

            cleansed_word = create_list(word.lower())
            master_words_list.append(cleansed_word)

    print(master_words_list)

    if word in master_words_list:
        print(word)



# word = word.split()
# word = word.lower()
# return word
# ​
# def clean_characters(sentence):
#     return re.sub(r'[^A-Za-z]', '', sentence).lower()
#         #word.split()



# all_lines = {}
# with open('sample.txt', 'r') as read:
#     read.seek(0)
#     for line in read:
#         for word in line.split():
#             word = re.sub('[^A-Za-z]', '', word).lower()
#             if word not in all_lines:
#                 all_lines[word] = 1
#             else:
#                 all_lines[word] += 1



        # for word in line.split():
        #     word = re.sub('[^A-Za-z]', '', word).lower()
        #     if word not in all_lines:
        #         all_lines[word] = 1
        #     else:
        #         all_lines[word] += 1
        #
        #             for line in f:
        # for word in f.split():
        #     #words - line.split()
        #     scrubbed_word = re.sub('[a-Zaz]', " ", word).lower()
        #     if scrubbed_word != '':
        #         print(scrubbed_word)

#BEGIN GAME
    #User must choose between EASY -- NORMAL -- HARD difficulty
#     easy_dict = ()
#
#     normal_dict = ()
#
#     hard = ()
#
#
# adding to dic
#                 if word in word_count:
#
#                 if word not in word_count
#                     word_count[word] = 1
#
#                 else:
#                     word_count[word] += 1

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
