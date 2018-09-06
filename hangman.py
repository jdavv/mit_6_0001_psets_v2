# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    print("Welcome to the game Hangman!")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word_char_list = []
    valid_guesses = []

    for c in secret_word:
        secret_word_char_list.append(c)

    for c in secret_word:
        if c in letters_guessed:
            valid_guesses.append(c)
        else:
            continue

    if valid_guesses == secret_word_char_list:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: guessed_word: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    valid_guesses = []
    for c in secret_word:
        if c in letters_guessed:
            valid_guesses.append(c)
        else:
            valid_guesses.append("_ ")

    guessed_word = ''.join(valid_guesses)
    return guessed_word


def is_a_vowel(userinput):
    '''

    :param userinput: a single character string
    :return:  Boolean True or false.
    Checks if userinput is in the vowel list
    '''
    vowel = ['a', 'e', 'i', 'o', 'u']

    if userinput in vowel:
        return True
    else:
        return False


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: available_letters: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    available_letters = []
    for c in alphabet:
        if c not in letters_guessed:
            available_letters.append(c)
        else:
            available_letters.append(' ')
    available_letters = ''.join(available_letters)
    available_letters = "Available letters: " + available_letters
    return available_letters


def is_guess_valid(letters_guessed, userinput):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    userinput: a string of 1 char that is only ascii lowercase
    returns a boolean valid.
    Checks if userinput is already in the list letters_guessed.
    '''
    if userinput in letters_guessed:
        valid = False
    else:
        valid = True
    return valid


def is_guess_correct(userinput, secret_word):
    '''

    :param userinput: a character the user type
    :param secret_word: word user is trying to guess
    :return: Boolean True or false
    Checks if userinput is found in the secret_word
    '''

    if userinput in secret_word:
        valid = True
    else:
        valid = False

    return valid

def is_guess_alpha_lower(userinput):
    '''

    :param userinput:
    :return: Boolean True or False
    checks userinput is a lowercase letter
    '''

    if userinput.islower():
        return True
    else:
        return False



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)

# 9/6/2018 Not worried about this function anymore.
# Focusing on hangman_with_hints()

    # Initialize some variables
    letters_guessed = []
    guesses_left = 6
    warnings_left = 3

    while guesses_left + warnings_left > 0:
        print("I am thinking of a word that is ", len(secret_word), "letters long. ")
        print(get_guessed_word(secret_word, letters_guessed))
        print("guesses left : ", guesses_left)
        print("warnings left : ", warnings_left)

        userinput = input("Please guess a letter: ")

        if userinput in letters_guessed:
            if warnings_left > 0:
                warnings_left = warnings_left - 1
            else:
                guesses_left = guesses_left - 1
            print('LETTER HAS ALREADY BEEN GUESSED')

        else:
            letters_guessed.append(userinput)
            if is_guess_correct(userinput, secret_word):
                print("GUESS IS CORRECT")
            else:
                print("GUESS IS NOT CORRECT")
                if is_a_vowel(userinput):
                    print ("IS A VOWEL")
                    guesses_left = guesses_left - 2
                else:
                    print("IS NOT A VOWEL")
                    guesses_left = guesses_left - 1
    else:
        print("YOU LOST!! HAHA")


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # my_word with spaces removed that the get_guessed_word function added
    my_word_cleaned = my_word.replace(' ', '')

    # A list of letters in my_word_cleaned
    letters_in_my_word_cleaned = list(my_word_cleaned)

    # A list of letters in other_word
    letters_in_other_word = list(other_word)

    # Count elements in list for iteration
    char_counter = len(letters_in_my_word_cleaned)

    # If number of elements in letters_in_other_word is the same as char_counter (letters in "my word")
    if len(letters_in_other_word) == char_counter:

        for i in range(char_counter):
            # Compare characters at the same index
            if my_word_cleaned[i] == other_word[i]:
                continue

            # Handle the gaps "_"
            elif my_word_cleaned[i] == "_" and other_word[i] not in letters_in_my_word_cleaned:
                continue
            else:
                # Word does not match with gaps
                return False
        # Word is matching with gaps
        return True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # Create a string containing other_words that match my_word to print.
    possible_matches = ""

    # Iterate through each other_word in wordlist
    for other_word in wordlist:

        # Add word too possible_matches if True
        if match_with_gaps(my_word, other_word):
            possible_matches += (other_word + " ")
        else:
            continue
    # When no matches are found
    if possible_matches == "":
        print("No matches found")
    # Print matches to console
    else:
        print(possible_matches)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # Initialize some variables
    letters_guessed = []
    guesses_left = 6
    warnings_left = 3

    # Print first message telling user how long the word is.
    print("I am thinking of a word that is ", len(secret_word), "letters long.")

    # Print number of warnings left for user.
    print("You have", warnings_left, "warnings left.")

    # Loop until is_word_guessed returns true, or guesses_left is 0.
    while not is_word_guessed(secret_word, letters_guessed) and guesses_left > 0:

        # print spacer
        print("----------")
        # Show user number of guesses left
        print("You have ", guesses_left, "guesses left.")
        # Show user available letters they can guess
        print(get_available_letters(letters_guessed))

        # print word displaying correct guesses and _ for letters not guessed
        print(get_guessed_word(secret_word, letters_guessed))

        # Grab user's guess
        userinput = input("Please guess a letter: ")

        # How to handle * as userinput. This means user wants hints.
        if userinput == "*":
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            guesses_left = guesses_left
            continue

        # If user input is anything other than a lowercase letter. Warnings or guesses are subtracted.
        if not is_guess_alpha_lower(userinput):
            # Check that warnings_left is greater than 0. Subtract a warning if greater than 0 else subtract a guess.
            if warnings_left > 1:
                warnings_left = warnings_left - 1
                print("Oops! That is not a valid letter. You have", warnings_left, "warnings left")
            else:
                guesses_left = guesses_left - 1
                print("Oops! That is not a valid letter. You have no warnings left so you loose one guess")

        # Check if the guess has previously been input before.
        else:
            if not is_guess_valid(letters_guessed, userinput):
                if warnings_left > 1:
                    warnings_left = warnings_left - 1
                    print("Oops! You've already guessed that letter. You have ", warnings_left, "warnings left.")
                else:
                    guesses_left = guesses_left - 1
                    print("Oops! That is not a valid letter. You have no warnings left so you loose one guess")
            # When the users input is a lowercase letter
            else:
                # When userinput is in secret word append to letters_guessed and inform user
                if is_guess_correct(userinput, secret_word):
                    letters_guessed.append(userinput)
                    print("Good Guess")
                else:
                    # When userinput is NOT in secret word. Append to letters_guessed and inform user.
                    letters_guessed.append(userinput)
                    print("Oops! That letter is not in my word")

                # If userinput is not found in secret word and is a vowel subtract 2 points
                if not is_guess_correct(userinput, secret_word):
                    if is_a_vowel(userinput):
                        guesses_left = guesses_left - 2
                    else:
                        # If userinput is not found in secret word and is NOT a vowel subtract 1 point
                        guesses_left = guesses_left - 1

    # Game ends. is_word_guessed is not true and guesses left is 0
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won! The word was", secret_word)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

     secret_word = choose_word(wordlist)
     hangman_with_hints(secret_word)