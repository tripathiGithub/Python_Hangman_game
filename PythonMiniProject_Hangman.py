#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    """
    print("Loading words...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline() #all words are in a long single line seperated by ' '
    wordlist = line.split()  #convert that {space} seperated line of words into list 
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
      
    letters_guessed: list (of letters), which letters have been guessed so far
      
    returns: boolean, True if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    secret_words = set(secret_word)
    letters_guessed = set(letters_guessed)
    return secret_words.issubset(letters_guessed)

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    
    letters_guessed: list (of letters), which letters have been guessed so far
    
    returns: string, comprised of letters, underscores (_), and spaces that represents
             which letters in secret_word have been guessed so far.
             
    example: secret_word = 'secret'
             letters_guessed = ['a','b','e','t','d']
             get_guessed_word(secret_word, letters_guessed) -> returns '_ e _ _ e t'
    '''
    lst = [i if i in set(letters_guessed) else '_' for i in secret_word]
    return ' '.join(lst)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    
    returns: list (of letters), comprised of letters that represents which letters have not
             yet been guessed.
      
    example: letters_guessed = ['a','b','c','d','e','f','g','h','i','j'.'k','l','m','n']
             get_available_letters(letters_guessed) -> returns ['o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
             
    '''
    all_letters = set(string.ascii_lowercase)
    avail_letters = sorted(all_letters - set(letters_guessed))
    return list(avail_letters)

def match_with_gaps(my_word, letters_guessed, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    
    letters_guessed: list (of letters), which letters have been guessed so far
    
    other_word: string, regular English word
    
    returns: boolean, True if all the actual letters of my_word match the 
             corresponding letters of other_word, or the letter is the special symbol
             _ , and my_word and other_word are of the same length
             False otherwise
        
    '''
    my_word = my_word.split(' ')
    
    if len(my_word) == len(other_word):
        
        for i,j in zip(my_word, other_word):            
            if i!= '_' and i!=j:
                return False            
            elif i=='_' and j in letters_guessed:
                return False
        else:
            return True        
    
    else:
        return False 
    
def show_possible_matches(my_word, letters_guessed, wordlist):
    '''
    my_word: string with _ characters, current guess of secret word
    
    letters_guessed: list (of letters), which letters have been guessed so far
    
    wordlist (list): list of words (strings)
    
    returns: nothing, but print out every word in wordlist that matches my_word

    '''
    matches = filter(lambda x : match_with_gaps(my_word, letters_guessed, x), wordlist)
    print('\nPossible Matches: ', ' '.join(list(matches)))

def hangman_with_hints():

    '''    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 5 guesses , call it 'life'.
    
    * Before each round, display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    '''
    wordlist = load_words() #load the words
    secret_word = choose_word(wordlist) #choose a random word
    score = 100 #initial score to start with
    lives = 5 
    warnings = 3
    letters_guessed=[]
    
    print(f'\n\nI am thinking of {len(secret_word)} letters long word\n')
    print('No life will be used on correct guesses, ')
    print('but you will loose one life on every incorrect guess and loose 10pts on score\n')
    
    while all( ( not is_word_guessed(secret_word, letters_guessed), lives!=0, warnings!=0)):
        print('#'*100,end='\n\n')
        print('Current Score: ', score)
        print('Lives Remaining :', lives)
        print('\nAvailable Letters :', get_available_letters(letters_guessed))
        print('\nYour progress :', get_guessed_word(secret_word, letters_guessed))
        
        guessed_letter = input('\nChoose your guess letter from given Available Letters : ').lower()
        
        if len(guessed_letter)==1 and guessed_letter in get_available_letters(letters_guessed):
            letters_guessed.append(guessed_letter)
            if guessed_letter in secret_word:
                print('\n*****Thats a Good Guess*****\n')
            else:
                lives -= 1
                score -= 10
                print('\n*****Thats not a good guess*****\n')
                        
        elif guessed_letter=='*':
            score -= 10
            show_possible_matches(get_guessed_word(secret_word, letters_guessed), letters_guessed, wordlist)
            
        else:          
            print(f'\nWarning!! Chosen letter :{guessed_letter}: not in the list of Available Letters')
            warnings -= 1 
            print(f'You have {warnings} warnings left!!')
            
    if is_word_guessed(secret_word, letters_guessed):
        print(f'\nCongrats!!You succesfully guessed the word :{secret_word}: with a score: {score}')
    else:
        reason = 'Lives' if lives==0 else 'Warnings'
        print(f'\nSorry you lost,because you exhausted all your {reason}, The word was: {secret_word}')


# In[4]:


hangman_with_hints()


# In[ ]:





# In[ ]:





# In[ ]:




