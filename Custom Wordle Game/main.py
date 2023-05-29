# Assignment 2 task 3
#
# Author: Mike Zhang 1555800 
#
# Create the Wordle175 game while using the ScrabbleDict class. 
# The user has 6 tries to guess a random 5 letter word obtain from dictionary in 
# ScrabbleDict class. After each attempt, a feedback is provided with 3 lists of letters
# Letters in red list are not in the target word, letters in orange list are in
# the target word but the position is wrong, letters in green list are correct and
# in the right position. The program validates the user input and accounts for cases
# of duplicate letters in both target and guess word when providing feedback.
# The game ends when user guesses correctly or runs out of guesses.

import random
# import ScrabbleDict class
from Wordle175 import ScrabbleDict


def targetword(dict1):
    '''
    Generates a random 5 letter words as the target word using the dictionary created
    with the ScrabbleDict class.
        
    Parameters: 
    dict1 (ScrabbleDict): an instance of class ScrabbleDict

    Returns: target word as a string in uppercase
    '''     
    # call returnkeys() methods to get all the words in the dictionary
    word_list = list(dict1.returnkeys())
    
    # pick a random word from all the words in dictionary
    word = random.choice(word_list)
    
    # return the word in uppercase as a string
    return word.upper()


def guesswithdup(alist):
    '''
    Takes in a list, if the list contains duplicate elements then number them
    accordingly. Returns a newlist where duplicate elements are numbered.
        
    Parameters: 
    alist (list): list that is checked for duplicate elements

    Returns: 
    newlist (list): newlist where duplicate elements are numbered
    '''     
    newlist = []
    
    for index in range(len(alist)):
        # if the count of an element is bigger than one then duplicates exist
        if alist.count(alist[index]) > 1:
            letter = alist[index]
            # number the element by counting how many times it occured so far in the list with slice
            letter += str(alist[0:index+1].count(alist[index]))   # string concatenation to number duplicate
            newlist.append(letter)     # append the numbered element to newlist
        else:
            # append to new list normally if no duplicates
            newlist.append(alist[index])
    
    # return the newlist where duplicate elements are numbered
    return newlist


def getinput(dict1, times, allguesses):
    '''
    Takes user input and checks if the input is valid. The input is only valid if
    it is the specified length, exists in the dictionary as a word, and it has not
    been used previously. Returns the valid input.
        
    Parameters: 
    dict1 (ScrabbleDict): an instance of class ScrabbleDict
    times (int): the current try
    allguesses (list): list with all previous valid entries

    Returns: 
    attempt (str): valid input in uppercase
    '''      
    validation = False
    
    # contiunes until input is valid
    while not validation:
        
        # get user input and convert to uppercase
        attempt = input("Attempt " +str(times)+ ": Please enter a 5 five-letter word: ").upper()
        
        # validate length of input
        if len(attempt) > dict1.getWordSize():  # call getWordSize() method for length
            print(attempt, "is too long")
        
        elif len(attempt) < dict1.getWordSize():
            print(attempt, "is too short")
        
        # check if input has been used before   
        elif attempt in allguesses:
            print(attempt, "was already entered")
        
        else:
            # call check() method to check if input is a recognized word
            if dict1.check(attempt.lower()):    # lowercase to compare with keys
                allguesses.append(attempt)     # add to allguesses if valid
                validation = True     # get out of the while loop with valid input
            else:
                print(attempt, "is not a recognized word")
    
    # return the valid input in uppercase
    return attempt


def greencheck(guess_list, target_list, guess_dup, green):
    '''
    Check the user input with the target word and determine if there are any
    letters from input that belongs to the green list. Modify the guess_list, 
    target_list, guess_dup list and green list accordingly.
        
    Parameters: 
    guess_list (list): user guess as a list
    target_list (list): target word as a list
    guess_dup (list): user guess as a list where duplicate elements are numbered
    green (list): list of letters that belong in the green for feedback, in the word
    and right position

    Returns: None
    '''     
    # if letter at index for guess and target is the same then letter is in green list
    for index in range(len(guess_list)):
        if guess_list[index] == target_list[index]:
            # append to green list from guess_dup because this accounts for duplicate letters
            green.append(guess_dup[index])
            # modify the guess and target lists
            # the letter at index of guess and target is changed to space to avoid counting again
            guess_list[index] = " "
            target_list[index] = " "            


def orangecheck(guess_list, target_list, guess_dup, orange):
    '''
    Check the user input with the target word and determine if there are any
    letters from input that belongs to the orange list. This function occurs
    after greencheck, therefore the lists passed in are potentially modify. This 
    helps with this step's checking. After checking, modify the guess_list, 
    target_list, guess_dup list and orange list accordingly.
        
    Parameters: 
    guess_list (list): user guess as a list (potentially modify)
    target_list (list): target word as a list (potentially modify)
    guess_dup (list): user guess as a list where duplicate elements are numbered
    orange (list): list of letters that belong in the orange for feedback, in the word
    but the position is wrong

    Returns: None
    '''    
    # check if every remaining letter in guess is in the remaining target list after greencheck
    for index in range(len(guess_list)):
        if guess_list[index] != " ":    # spaces modified from greencheck are skipped
            if guess_list[index] in target_list:
                # append from guess_dup because this accounts for duplicate letters in guess
                orange.append(guess_dup[index])
                # each time a letter in guess in confirmed to be in target, change an
                # occurrence of this letter in target to space to avoid counting again
                letter = guess_list[index]
                target_list[target_list.index(letter)] = " "
                # change letter in guess to space if it is confirmed in target               
                guess_list[index] = " "  


def redcheck(guess_list, guess_dup, red):
    '''
    Check the user input with the target word and determine if there are any
    letters from input that belongs to the red list. This function occurs
    after greencheck and orangecheck therefore the lists passed in are potentially modify. 
    Because greencheck and orangecheck already occured, any letters left in guess belongs
    in the red list. 
        
    Parameters: 
    guess_list (list): user guess as a list (potentially modify)
    guess_dup (list): user guess as a list where duplicate elements are numbered
    red (list): list of letters that belong in the red for feedback, not in the target

    Returns: None
    '''    
    # any remaining letters in guess_list belongs in red because green and orange already checked
    # append the corresponding elements in guess_dup with the same index
    for index in range(len(guess_list)):
        if guess_list[index] != " ":  
            red.append(guess_dup[index])  # append from guess_dup to account for duplicate
   
def main():
    '''
    Main function of the program. Executing the Wordle175 game by calling the 
    specific functions.
    
    Parameters: none
    
    Returns: None
    '''         
    # create instance of ScrabbleDict class
    dict1 = ScrabbleDict(5, "scrabble5.txt")
    
    #obtain target word by calling targetword() function
    target = targetword(dict1)

    feedback_list = []    # tracks feedback from every attempt
    allguesses = []     # tracks all valid attempts
    tries = 1     # tracks how many tries
    contiune = True    # tracks if game is finished or not
    
    # game contiunes when both conditions are met
    while tries < 7 and contiune == True:
        
        # obtain the lists
        target_list = list(target)         
        guess = getinput(dict1, tries, allguesses)  # call getinput() for user input
        guess_list = list(guess)
        # callguesswithdup() for guess list where duplicates are numbered
        guess_dup = guesswithdup(guess_list)   
        
        # 3 color lists
        green = []
        orange = []
        red = []
        
        # call the 3 checks where each color list will be modified accordingly        
        greencheck(guess_list, target_list, guess_dup, green)   
        orangecheck(guess_list, target_list, guess_dup, orange)
        redcheck(guess_list, guess_dup, red)
        
        # obtain the feedback message as a string using joing and in the right format
        feedback = guess+" Green={"+', '.join(sorted(green))+"} - Orange={"+', '.join(sorted(orange))+"} - Red={"+', '.join(sorted(red))+"}"
        # add message to a list in order to display all previous messages with each guess
        feedback_list.append(feedback)
        # display all previous messages with each guess
        for item in feedback_list:
            print(item)
        
        # game ends if user guesses the target    
        if guess == target:
            print("Found in",tries,"attempts. Well done. The Word is", target)
            contiune = False   # get out of the while loop
        
        # tries increase each time
        tries += 1

    # if program gets out of the while loop but contiune is still true
    # this means user lost and did not guess the target after 6 tries
    if contiune == True:
        print("Sorry you lose. The Word is", target)
    

main()
