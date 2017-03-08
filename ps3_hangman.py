# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/DatTran/Documents/python/words.txt"

def loadWords():
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
    print len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    true = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            true +=1
    # if all letter in secretWord can be found in lettersGuessed        
    if true == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessWord = ''
    # string is immutable so we use concatation
    for letter in secretWord:
        if letter in lettersGuessed:
            guessWord = guessWord + letter
        else:    
            guessWord = guessWord + '_ '
            
    return guessWord  


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    result = ''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            result = result + letter
    return result
    
def isLetterCorrect(secretWord, letterGuessed):
    '''
    isLetterCorrect: check is guessed letter is in secretWord
    return True if guessed letter is represnt and False otherwise
    '''
    for letter in secretWord:
        if letter == letterGuessed:
            return True
    return False


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    # greeting
    print "Welcome to the word, I'm Hangman!"
    print "I'm thinking about the word that is " + str(len(secretWord)) + ' letters long'
    
    # letter that has been guessed
    lettersGuessed = []
    
    # number of mistake
    mistakesMade = 0    
    
    # continue the game until no more life or the whole word guessed
    while mistakesMade < 8:
         print '--------------'
         print 'You have ' + str(8 - mistakesMade) + ' guesses left'
         print 'Available letters: ' + getAvailableLetters(lettersGuessed)
         print 'Please guess a letter: ',
         letter = raw_input()
         letterInLowerCase = letter.lower()
         
         # if letter had been guess
         if letterInLowerCase in  lettersGuessed:
             print "Oops! You've already guessed that letter: ",
             print getGuessedWord(secretWord, lettersGuessed)
         else:
            #  check if the guessed letter is correct?   
            if isLetterCorrect(secretWord, letterInLowerCase):
                print 'Good guess:',
            else:
                print 'Oops! That letter is not in my word:',
                mistakesMade += 1
            
            # print the guessed word
            lettersGuessed.append(letterInLowerCase)
            print getGuessedWord(secretWord, lettersGuessed)
         
         # when the word is guessed completely
         if isWordGuessed(secretWord, lettersGuessed):
             break
    # check if player win or lose
    print '--------------' 
    if mistakesMade == 8:  
        print 'Sorry, you ran out of guesses. The word was ' + secretWord
    else:
        print 'Congratulations, you won!' 


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman('zzz')
