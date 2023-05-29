# Assignment #3 task 4
#
# Author: Mike Zhang 1555800
#
# Program to play the game, import the required Classes and write the game loops.

from AbacoStack import Card
from AbacoStack import BStack
from AbacoStack import AbacoStack


def getinput():
    '''
    Takes user input for number of stacks and depth of each stack.
    Checks if each input is valid, the input is only valid if
    it is a number in the specified range. Returns valid inputs.
        
    Parameters: 
    None

    Returns: a tuple that contains the valid number of stacks and depth respectively
    '''      
    # two validations
    validations = False
    validationd = False
    
    # contiunes until input is valid
    while not validations:       

        size = input("Please enter number of stacks between 2 and 5: ")
        
        # check if input is a number
        if size.isnumeric() == False:  
            print("Please enter a number")
        
        else:
            # check if input is within range
            if int(size) >= 2 and int(size) <= 5:    
                validations = True     # get out of the while loop with valid input
            else:
                print("Please enter a number in range")
    
    while not validationd:       
            
        depth = input("Please enter depth of stacks between 2 and 4: ")
        
        # check if input is a number    
        if depth.isnumeric() == False:  
            print("Please enter a number")
                    
        else:
            # check if input is within range
            if int(depth) >= 2 and int(depth) <= 4:    
                validationd = True     # get out of the while loop with valid input
            else:
                print("Please enter a number in range")    
    
    # return the valid input for size and depth as a tuple
    return (int(size), int(depth))


def main():    
    '''
    Main function of the program. Contains the game loops, calls functions and methods 
    from imported Classes to execute the game. 
        
    Parameters: 
    None

    Returns: None
    '''     
    # tracks if the user wants to play another game
    contiune = True
    
    # outer loop which contiunes with new games until user decides to stop
    while contiune:
        
        # get user input for the number of stacks and depth of this game
        board = getinput()     # a tuple
        
        # create card using user inputs
        card1 = Card(board[0], board[1])
        
        # create game which is an instance of AbacoStack class
        game1 = AbacoStack(board[0], board[1])    # same size and depth as card
        game1.show(card1)     # what the game looks like initially
        
        # tracks if the user want to quit completely with "Q"
        quit = False
        
        # game contiunes to run until either the puzzle is solved or user quits
        while not game1.isSolved(card1) and not quit:
            
            # takes input for moves
            moves = input("Enter your move(s) [Q for quit and R to reset]: ")
            
            # Respond to Q and R appropriately
            if moves == "Q":
                quit = True     # turns quit to True
            
            elif moves == "R":
                # reset the current game with reset() and shows board
                game1.reset()
                game1.show(card1)
            
            # else the user attempted to move
            else:
                # split input at space
                newmoves = moves.split()
                if len(newmoves) >= 5:
                    newmoves1 = newmoves[:5]    # slice input if it is longer than 5 moves
                else:
                    newmoves1 = newmoves
                
                # for each move use try and except and call moveBead()
                # moveBead() will check the validity of input
                # if input invalid then exception will be raised in moveBead() and catched here
                # display proper error message and the games loop contiunes to ask new input
                for index in range(len(newmoves1)):
                    try:
                        # try each move
                        game1.moveBead(newmoves1[index])
                    
                    except Exception as moveError:
                        # handle exception here with message
                        print(moveError.args[0], ":", newmoves1[index])
                        # set index as max in order to exit the for loop 
                        # this way as soon as a move is invalid other moves after will not be checked
                        index = len(newmoves1)-1
                
                # show game state after all moves are performed            
                game1.show(card1)
                
            
        # if the puzzle is solved then print message and ask to play again
        if game1.isSolved(card1):
            print("Congratulations, you solved the puzzle! Total moves:", game1.returnmoves())
            
            again = input("Would you like to play again? Y or N ").upper()
            if again == "Y":
                contiune = True
            else:
                # this would exit the outer loop and the program finishes
                contiune = False
                
        # this will only happen if the user quit with "Q"
        # therefore contiune will be False so user can quit properly
        else:
            contiune = False

main()