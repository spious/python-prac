import random
from words import words
import string


def get_valid_words(word_list):
    word = random.choice(word_list)

    # if a word has a - or space in it, then it will again choose a random word from the list
    # it will keep generating a random item till we find a word without - or space
    while ('-' in word or ' ' in word):
        word = random.choice(word_list)

    return word.upper()


def board(used_letters, word, lives):
    word_list = [letter if letter in used_letters else '_' for letter in word]
    print('\n⭐ The word so far looks like: ', ' '.join(word_list))
    print('You have', lives, 'lives left.')


def hangman():
    word = get_valid_words(words)
    word_letters = set(word)

    alphabets = set(string.ascii_uppercase)

    used_letters = set()

    lives = 6
    while (len(word_letters) > 0 and lives > 0):

        if len(used_letters) > 0:
            print('\nYou have used these letters till now: ',
                  ','.join(used_letters))

        user_input = input('🚩 Guess a letter: ').upper()

        # check if user_input is not yet used
        if user_input in alphabets - used_letters:
            # since the letter is not used already, add it in used letters
            used_letters.add(user_input)

            # then check if the letter is in the correct answer set, if yes then remove it from the answer set
            if user_input in word_letters:
                word_letters.remove(user_input)
                print(user_input.upper(), 'is in the word!')
                board(used_letters, word, lives)
            else:
                lives -= 1
                print(user_input, 'is not in the word.')
                board(used_letters, word, lives)

        elif user_input in used_letters:
            print('You have already guessed this letter.Try again!\n')
        else:
            print('Invalid character. Try again!🚫\n')

    if lives == 0:
        # print(lives_visual_dict[lives])
        print('\nNo lives left, sorry😔. The word was', word, end="\n\n")
    else:
        print('\nYAY! You guessed the word:', word, '!!😀', end="\n\n")


hangman()

# def play_again():
#     play_again = input("\nPlay Again?? \nY for Yes \nN for No \n\n")

#     if play_again.lower() not in ['y','n']:
#         play_again = input(f'\nInvalid response.Please enter either \nY for Yes \nN for No \n\n')
#     elif play_again.lower() == 'y':
#         return hangman()
#     else:
#         print(f'\nThank You for Playing!👋')
