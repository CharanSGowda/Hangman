import random
from words import words  # var words described in the other document named main
import string


def valid_words(words):
    word = random.choice(words)  # for choosing the words randomly from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hang():
    word = valid_words(words)  # defining word
    word_letters = set(word)  # keeps a track on the words used previously
    alphabet = set(string.ascii_uppercase)  # to import the already determined alphabets in english dictionary
    used_letters = set()  # keeps a track of words already used in the process

    lives = 6

    while len(word_letters) > 0 and lives > 0:  # if word length is greater than 0 then iterate happens
        # letters used
        # ' ' .join(['a', 'b', 'cd']) == 'a b cd'
        print('you have', lives, 'left and You have used these letters Dickhead: ', ' '.join(used_letters) )

        # what current letters are being used presently
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a word: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:


                word_letters.remove(user_letter)


            else:
                lives = lives - 1
                print("Letter Not in the Word")

        elif user_letter in used_letters:
            print("You have already used, dickhead. try again.")

        else:
            print("Invalid Entry")


      # gets here when len(word_letters) == 0
    if lives == 0 :
        print('You Died DIckhead. The Word was', word)
    else :
        print('You Guessed It Gaandu, the word', word, '!!')


hang()
