# Assignment 2 task 4 and 5
#
# Author: Mike Zhang 1555800 
#
# Allows the user to enter a template and returns all the words that are compatible
# with the template. Allows additional letters input to further narrow down the list
# of possible words. Both inputs from the user will be validated. 
# Program also calculates and displays the counts and percentage of each letter in the
# alphabet in the list of words. 


# import ScrabbleDict class
from Wordle175 import ScrabbleDict

def templateinput(dict1):
    '''
    Takes user input for template and checks if the input is valid. The input is 
    only valid if it is the specified length, contains at least one "*", and contains
    only letters other than "*". Returns the valid input.
        
    Parameters: 
    dict1 (ScrabbleDict): an instance of class ScrabbleDict

    Returns: 
    attempt (str): valid input in lowercase
    '''     
    
    validation = False
    
    # contiunes until input is valid    
    while not validation:
        
        # get user input and convert to lowercase
        attempt = input("Please enter a valid template for a hint: ").lower()
        
        # validate length of input
        if len(attempt) > dict1.getWordSize():   # call getWordSize() method for length
            print(attempt, "is too long")
        
        elif len(attempt) < dict1.getWordSize():
            print(attempt, "is too short")
        
        # check if input has at least one *    
        elif attempt.count("*") == 0:
            print("Template needs to contain at least one *")
        
        else:
            tracker = 0
            # check if characters in input are either letter or *
            for letter in attempt:
                if(letter.isalpha() or letter == "*"):
                    tracker += 1  
            # all characters in input are valid if tracker equals length of input
            if tracker == len(attempt):
                validation = True
            else:
                print(attempt, "contains invalid characters")

    # return the valid input as a string in lowercase
    return attempt


def letterinput(template):
    '''
    Takes user input for additional letters and checks if the input is valid. 
    The input is only valid if it less than the number of wildcards (*) in template,
    and the input has to contain letters only.
        
    Parameters: 
    template (str): the template used to check for compatible words

    Returns: user input as a list of letters
    '''     
    
    validation = False
    
    # contiunes until input is valid 
    while not validation:
        
        # get user input and convert to lowercase
        attempt = input("Please enter additional letters for hint, press enter to skip: ").lower()
        
        # validate length of input, cannot be more than number of * in template
        if len(attempt) > template.count("*"):
            print(attempt, "is too long")
        
        else:  
            # checks if input only contains letters or it is empty
            if (attempt.isalpha() or attempt == ""):
                validation = True
            else:
                print(attempt, "contains invalid characters")

    # returns input as a list 
    return list(attempt)


def countletters(alist):
    '''
    Count the frequency of each letter of the alphabet in these words in the list.
    Display the count, percentage, and a histogram.
        
    Parameters: 
    alist (list): list that contains the words to be analyzed

    Returns: None
    '''      
    # first join all word into one string and convert to upper
    bigstring = "".join(alist).upper()
    
    dict2 = {}  # dictionary to keep track of each letter and frequency
    
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    # create the dictionary where the keys are the letters and values are the frequency
    for letter in alpha:
        if letter not in dict2.keys():
            dict2[letter] = bigstring.count(letter)
    
    # calculate total letters by adding all counts
    total_letters = sum(dict2.values())
    
    # display results for each letter in alphabetical order        
    for key in sorted(dict2.keys()):
        percent = (dict2[key]/total_letters)*100  # percent as a float
        # formatted where percent is rounded to 2 decimal places and * based on rounding to the closes integer
        print(key+":"+ f'{dict2[key]:>5}'+ f'{percent:>6.2f}'+"%  "+ "*"*int(round(percent)))
    

def main():
    '''
    Main function of the program. Calls the specific functions for user input
    for template and additional letters. Calls the specific function to display
    the statistics for letter count. 
    
    Parameters: none
    
    Returns: None
    '''     
    # create instance of ScrabbleDict class
    dict1 = ScrabbleDict(5, "scrabble5.txt")
    
    # call templateinput() to get valid input for template
    template = templateinput(dict1)
    
    # call letterinput() to get valid input for additional letters
    letters = letterinput(template)
    
    # call getConstrainedWords() from ScrabbleDict class to get list of word
    # that are compatible
    possible_words = dict1.getConstrainedWords(template,letters)
    
    # display the possible word to user
    print()
    for aword in possible_words:
        print(aword)

    print()
    # call countletters() to display the statistics for letter count
    countletters(list(dict1.returnkeys()))   # call returnkeys() method to count all dictionary words


main()