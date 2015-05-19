# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()


def partial_word(secret_word, guessed_letters):
    """
    Return the secret_word in user-visible format, with underscores used
    to replace characters that have not yet been guessed.
    """
    result = ''
    for letter in secret_word:
        if letter in guessed_letters:
            result = result + letter
        else:
            result = result + '_'
    return result


def hangman():

word = choose_word(wordlist)
chances = 8
status = '_' * len(word)
letters = "abcdefghijklmnopqrstuvxyz"
correct = False


print "Welcome to the game, Hangman!\nI am thinking of a word that is %d letters long." % len(word)

while chances > 0 and correct == False:
    print "_" * 50
    print "You have %d guesses left." % chances
    print "Available letters: %s" % letters
    attempt = raw_input("Please guess a letter: ")

    #Check whether attempt is in word. If yes, replace character with attempt.
    #If no, reduce chances and give message.



    for l in word:
        if l == attempt:
            status.replace(word, '_', attempt)
            print "Good guess: %s" % status

        else:
            print "Oops! That letter is not in my word: %s" % status
            chances -= 1

    #Update available letters






#End result

if chances == 0:
    print "Bad luck! You lost..."

elif correct == True:
    print "Congratulations, you won!"


