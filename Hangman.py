# assignment: programming assignment 1
# author: Sean Andre Membrido
# date: 1/23/23
# file: hangman.py is a program that simulates the game of hangman. 
# input: Takes numbers and letters as input.
# output: Displays number of lives and hidden words. 
#outline = dictionary with all words to be sorted into lists based on number of words. Dictionary key will be number of letters
#will loop to play the game

from random import choice, random, randint

dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located

# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary (filename) :
    dictionary = {}
    max_size = 12
    maxDictionary = [[],[],[],[],[],[],[],[],[],[],[],[]]

    with open(filename) as file:
        fileInputs = file.readlines()
        fileInputs = [i.strip() for i in fileInputs]
    fileInputs.pop()
    for i in range(max_size):
        for word in fileInputs:
            if len(word) == i+1:
                maxDictionary[i].append(word)
            elif len(word) > max_size:
                maxDictionary[max_size-1].append(word)

    for i in range(len(maxDictionary)):
        dictionary[i+1] = maxDictionary[i]
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    print(dictionary) 

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options() :
    try:
        usersize=int(input('Please choose a size of a word to be guessed [3 – 12, default any size]:\n'))
        if (usersize < 3) or (usersize > 12):
            raise ValueError
        print(f'The word size is set to {usersize}.')
    except ValueError:
        usersize = randint(1,12)
        print('A dictionary word of any size will be chosen.')
    size = usersize

    try:
        userlives = int(input('Please choose a number of lives [1 - 10, default 5]:\n'))
        if (userlives < 1) or (userlives > 10):
            raise ValueError
        lives = userlives
    except ValueError:
        lives = 5
    print(f'You have {lives} lives.')
    return (size, lives)


# MAIN

if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print the dictionary (use only for debugging)
    # print a game introduction
    print('Welcome to the Hangman Game!')
    # START MAIN LOOP (OUTER PROGRAM LOOP)
    while True:
    # set up game options (the word size and number of lives)
        (wordsize, lives)=get_game_options()
    

    # select a word from a dictionary (according to the game options)
    # use choice() function that selects an item from a list randomly, for example:
    # mylist = ['apple', 'banana', 'orange', 'strawberry']
    # word = choice(mylist)
        word = choice(dictionary[wordsize]).upper()
        chosenlist = []
        hiddenletters = ['__' for i in range(wordsize)]
        (life,index)=(['O' for i in range(lives)],0)
        win=False
        loss=False
        skip=False
        # START GAME LOOP   (INNER PROGRAM LOOP)
        while((not loss) and not(win)):
            if (skip==False):
                print("Letters chosen: ", end='')
                for i in chosenlist:
                    print(i, end='')
                    if chosenlist[-1] != i:
                        print(', ' , end = '')
                print()
                for i in range(len(hiddenletters)):
                    if word[i] == '-':
                        hiddenletters[i] = word[i]
                        print(hiddenletters[i], end = '  ')
                    else:
                        print(hiddenletters[i], end = '  ')
                print(f' lives: {lives} ', end = '')
                for i in life:
                    print(i, end = '')
                print()
            skip = False
        
        # format and print the game interface:
        # Letters chosen: E, S, P                list of chosen letters
        # __ P P __ E    lives: 4   XOOOO        hidden word and lives

        # ask the user to guess a letter
        # update the list of chosen letters
        # if the letter is correct update the hidden word,
        # else update the number of lives
        # and print interactive messages    

            try:
                print("Please choose a new letter >")
                newletter = str(input()).strip().upper()
                if newletter in chosenlist:
                    print('You have already chosen this letter')
                    raise ValueError
                elif len(newletter) > 1:
                    raise ValueError
                elif newletter.isalpha() == False:
                    raise ValueError
                elif newletter in word:
                    print('You guessed right!')
                    chosenlist.append(newletter)
                    for i in range(wordsize):
                        if word[i] == newletter:
                            hiddenletters[i] = newletter
                else:
                    print('You guessed wrong, you lost one life.')
                    chosenlist.append(newletter)
                    lives = lives - 1
                    life[index] = 'X'
                    index = index + 1
                hiddenword=''
                for i in hiddenletters:
                    hiddenword = hiddenword + i
                if (hiddenword==word):
                    win=True
                if (lives<=0):
                    loss=True
            except ValueError:
                skip=True
      

        # END GAME LOOP   (INNER PROGRAM LOOP)

        # check if the user guesses the word correctly or lost all lives,
        # if yes finish the game

        print('Letters chosen: ', end = '')
        for i in chosenlist:
            print(i, end ='')
            if chosenlist[-1] != i:
                print(', ', end = '')
        print()

        for i in hiddenletters:
            print(i, end ='  ')
        print(f' lives: {lives} ', end = '')
        for i in life:
            print(i, end = '')
        print()

        
           
    


        if win:
            print(f'Congratulations!!! You won! The word is {word}!')
        if loss:
            print(f'You lost! The word is {word}!')
            
            
    # END MAIN LOOP (OUTER PROGRAM LOOP)

    # ask if the user wants to continue playing, 
    # if yes start a new game, otherwise terminate the program
        try:
            print('Would you like to play again [Y/N]?')
            newgameyn = input()
            if newgameyn == 'Y' or newgameyn == 'y':
                continue
            else:
                raise ValueError
        except ValueError:
            print('Goodbye!')
            break
    
    
    
