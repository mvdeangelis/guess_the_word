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

    flag = True

    for letter in secret_word:

        if not letter in letters_guessed:
            flag = False

    return flag

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ""

    for letter in secret_word:

        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_ "

    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    available_letters = string.ascii_lowercase

    for letter in letters_guessed:
        available_letters = available_letters.replace(letter, '')

    return available_letters

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    max_letters = 100
    max_guesses = 6
    max_warnings = 3
    warnings_remaining = 3
    i = 0
    vowels = 'aeiou'
    n_letters = len(secret_word)
    letters_guessed = [''] * max_letters
    guesses_remaining = max_guesses

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(n_letters) + " letters long")
    print("You have " + str(warnings_remaining) + " warnings left.")

    while(guesses_remaining > 0):
        print("----------------------------")

        print("You have " + str(guesses_remaining) + " guesses left.")
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: ", available_letters)

        check_continue_warning = True

        while(check_continue_warning):
            letter = input("Please guess a letter: ")

            if not letter.isalpha():
                warnings_remaining -= 1

                print("Oops! That is not a valid letter.")

                if warnings_remaining >= 0:
                    print("You have " + str(warnings_remaining) + " warnings remaining.")
                else:
                    guesses_remaining -= 1
                    print("You have no more warnings left, so you lose a guess.")
                    print("You have " + str(guesses_remaining) + " guesses left.")
                    warnings_remaining = 3
            else:
                check_continue_warning = False

        letters_guessed[i] = letter.lower()

        for letter in  letters_guessed:
            if letter == letters_guessed[i]:
                print("Oops! You've already guessed that letter.")

                if warnings_remaining >= 0:
                    print("You now have " + str(warnings_remaining) + " warnings remaining.")
                else:
                    guesses_remaining -= 1
                    print("You have no more warnings left, so you lose a guess.")
                    print("You have " + str(guesses_remaining) + " guesses left.")
                    warnings_remaining = 3

        guessed_word = get_guessed_word(secret_word, letters_guessed)

        if not letters_guessed[i] in secret_word:
            if letters_guessed[i] in vowels:
                guesses_remaining -= 2
                print("Oops! That letter is not in my word: " + guessed_word)
            else:
                guesses_remaining -= 1
                print("Oops! That letter is not in my word: " + guessed_word)
        else:
            print("Good guess: " + guessed_word)

        i += 1




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



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
    pass



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
    pass



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
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
     #pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    #hangman(secret_word)
    hangman('obama')

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
