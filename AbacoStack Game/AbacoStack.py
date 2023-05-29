# Assignment #3 Task 1-3
#
# Author: Mike Zhang 1555800
#
# Create the Card Class, Bounded Stack Class, and AbacoStack Class and implement the required methods

import random

# create class Card
class Card:
    
    def __init__(self, colours, depth):
        '''
        Constrcutor method for class Card. Initializes the instance attributes.
        One private property beads is a list that stores beads in each stack, 
        starting with the first stack to the last, each stack stored top to bottom.
        
        Parameters: 
        colours (int): number of stacks 
        depth (int): depth of each stack
        
        Returns: None
        '''         
        # Initialize the instance attributes 
        self._beads = []     # private property
        self.stacks = colours   # number of stacks
        self.depth = depth     # depth of each stack
        
        # create the list of beads 
        for i in range(self.stacks):
            for index in range(self.depth):
                # append the same letter self.depth times
                self._beads.append(chr(i + 65))    # use chr to convert int to letter
        
        # shuffle the list
        random.shuffle(self._beads)
    
    def reset(self):
        '''
        Reshuffle the card to generate a new configuration.
        
        Parameters: 
        None
        
        Returns: None
        '''         
        # reshuffle
        random.shuffle(self._beads)
    
    def show(self):
        '''
        Display a card following the specific format
        
        Parameters: 
        None
        
        Returns: None
        '''         
        # self.depth dictates how many rows to display
        for i in range(self.depth):
            print("|", end="")    # use end for formatting
            # within the list, increase i by self.depth each time
            # this way letter at the same index from each stack is printed horizontally
            for index in range(i, len(self._beads), self.depth):
                # last letter in row print without space
                if (index + self.depth) >= len(self._beads):    # last letter
                    print(self._beads[index], end="")
                else:
                    print(self._beads[index], end=" ")
            print("|")
        
        print()
        print("from a list", self._beads)
    
    def stack(self, number):
        '''
        Return the ordered list of elements top to bottom in the number stack.
        
        Parameters: 
        number (int): which stack to return 
        
        Returns: list representing the stack through slicing
        '''           
        # determine the start and end of slicing for stack
        start = (number - 1)*self.depth     # self.depth is the length of each stack
        end = start + self.depth 
        
        # slice the list of beads
        return self._beads[start:end]
    
    def __str__(self):
        '''
        Convert a Card instance into a string such that the string represents 
        the stacks in the configuration card.
        
        Parameters: 
        None
        
        Returns: 
        astring (str): Card instance as a string in specific format
        '''          
        # return items as a string
        
        astring = ''
        tracker = 0   # use to place | at the right positions
        
        # number of stacks to iterate
        for i in range(self.stacks):
            astring += "|"
            # add to string until the end of one stack
            # self.depth is the length of stacks, tracker keeps increase until end of list
            while (tracker < (i+1)*self.depth):
                astring += self._beads[tracker]
                tracker += 1
            astring += "|"
            
        return astring
    
    def replace(self, filename, n):
        '''
        Reads from the file filename the nth config card and replaces the 
        card state with the new configuration.
        
        Parameters: 
        filename (file): filename of the file
        n (int): the line in the file to use to replace
        
        Returns: 
        None
        '''         
        
        # read the text file
        file = open(filename,'r')
        content = file.readlines()    # returns a list where elements are lines
        file.close()
        
        # get the nth line
        line = content[n]      
        line = line.strip()      # remove newline at the end of line
        newline = line.split()      # split line at space into a list
        
        # replace beads list with newline
        self._beads = newline


class BStack:
    def __init__(self, capacity):
        '''
        Constrcutor method for class BStack. Initializes the instance attributes.
   
        Parameters: 
        capacity (int): max size of each stack
        
        Returns: None
        '''         
        # initialize the BStack object and capacity
        self.__items = []
        self.__capacity = capacity
    
    def push(self, item):
        '''
        Insert item at the end of the list/stack.
   
        Parameters: 
        item (str): the item to be pushed
        
        Returns: None
        '''                
        # raise exception is this method is invoked on full stack
        # check full or not using capacity
        if len(self.__items) >= self.__capacity:
            raise Exception("Error: Stack is full")
        self.__items.append(item)        


    def pop(self):  
        '''
        Remove and return an item at the end of the list.
   
        Parameters: 
        None
        
        Returns: the item on top of the stack that was just removed
        '''          
        # raise an exception if method is invoked on empty stack
        
        if len(self.__items) <=0:
            raise Exception("Error: Stack is empty")
        return self.__items.pop() 


    def peek(self):  
        '''
        Return the item at the last location of the list.
   
        Parameters: 
        None
        
        Returns: the item on top of the stack 
        '''        
        # raise an exception if method is invoked on empty Stack      
        if len(self.__items) <= 0:            
            raise Exception('Error: Stack is empty')        
        
        # get index of last item using len()
        return self.__items[len(self.__items)-1]    
    
    def isFull(self):
        '''
        Check if the stack is full. Return true if it is, false if not
   
        Parameters: 
        None
        
        Returns: True if stack is full, False if not
        '''                
        # use capacity to check if stack is full
        return len(self.__items) == self.__capacity
          
    def isEmpty(self):
        '''
        Check if the stack is empty. Return true if it is, false if not
   
        Parameters: 
        None
        
        Returns: True if stack is empty, False if not
        '''          
        # stack empty if it is equal to an empty list
        return self.__items == []
    
    def size(self):
        '''
        Return how many items are in the Stack.
   
        Parameters: 
        None
        
        Returns: number of items in stack as an integer 
        '''         
        # return length of stack
        return len(self.__items)
     
    def capacity(self):  
        '''
        Returns the max capacity of the Stack
   
        Parameters: 
        None
        
        Returns: max capacity as an integer 
        '''         
        return self.__capacity    
    
    def show(self):
        '''
        Print the list/stack.
   
        Parameters: 
        None
        
        Returns: None
        '''         
        # print the list
        print(self.__items)
    
    def __str__(self):
        '''
        Return items in Stack as a string.
   
        Parameters: 
        None
        
        Returns: 
        stackAsString (str): stack as a string in specific format
        '''         
        
        stackAsString = ''
        
        # add each item in list to string
        for index in range(len(self.__items)):
            # add space after items except last item
            if index < len(self.__items)-1:
                stackAsString += self.__items[index] + ' '
            else:
                stackAsString += self.__items[index]

        return stackAsString
    
    def joiningstack(self):
        '''
        Return items in Stack as a string, with no spaces.
   
        Parameters: 
        None
        
        Returns: stack as a string without spaces between items
        '''          
        # use join to get string without spaces
        return "".join(self.__items)
    
    def clear(self):
        '''
        Remove all items in the Stack.
   
        Parameters: 
        None
        
        Returns: None
        '''         
        # use .clear() to remove all items in the Stack
        self.__items.clear()
    
class AbacoStack:
    
    def __init__(self, nostacks, depth):
        '''
        Constructor method for class AbacoStack. Initializes the instance attributes.
        An instance of this class stores bounded stacks and a list representing the top row. 
        The size of the list will be the number of bounded stacks + 2.
        
        Parameters: 
        nostacks (int): number of stacks 
        depth (int): depth of each stack
        
        Returns: None
        '''         
        # initialize the instance attributes
        self.stacks = nostacks
        self.depth = depth
        self.listofstacks = []    # put all BStacks into a list
        self.toprow = []
        self.moves = 0      # track total moves
        
        # create top row with proper size and fill it with "."
        for i in range(self.stacks + 2):
            self.toprow.append(".")           
        
        # create BStacks each with one color and append to list
        for i in range(self.stacks):
            astack = BStack(self.depth)
            # self.depth is how many letter for each stack
            for index in range(self.depth):
                astack.push(chr(i + 65))     # use chr() to convert int to str
            self.listofstacks.append(astack)
    
    def returnmoves(self):
        '''
        Returns total moves.
        
        Parameters: 
        None
        
        Returns: None
        '''          
        
        return self.moves
    
    def moveBead(self, move):
        '''
        Changes the state of the AbacoStack instance based on the move provided.
        Check if move is valid, raise Exception if it is not.
        
        Parameters: 
        move (str): 2 characters, first one is position, second is direction
        
        Returns: None
        '''          
        # first check if move is the correct format
        if len(move) != 2:
            raise Exception("Error: invalid move")
        else:
            if not move[0].isnumeric() or not move[1] in ["u", "d", "r", "l"]:
                raise Exception("Error: invalid move")
                
        # call removedots() to remove the "." from each stack
        self.removedots(self.listofstacks)
        
        # position is the first character of move
        position = int(move[0])
        
        # Divide into 4 directions to check if move is valid:
        
        #up direction
        # if a move is not in the ifs then it is not valid and raise exception
        if move[1] == "u":
            # position has to be within range
            if position > 0 and position < len(self.toprow)-1:
                # stack has to have something to pop, corresponding top row position cannot be taken
                if not self.listofstacks[position-1].isEmpty() and self.toprow[position] == ".":
                    # perform move
                    temp = self.listofstacks[position-1].pop()
                    self.toprow[position] = temp
                    self.moves += 1
                
                else:
                    raise Exception("Error: invalid move")
            
            else:
                raise Exception("Error: invalid move")
        
        # down direction
        # if a move is not in the ifs then it is not valid and raise exception
        if move[1] == "d":
            # position has to be within range
            if position > 0 and position < len(self.toprow)-1:
                # stack has to not be full, and corresponding top row cannot be "."
                if not self.listofstacks[position-1].isFull() and self.toprow[position]!= ".":
                    # perform move
                    temp = self.toprow[position]
                    self.listofstacks[position-1].push(temp)
                    self.toprow[position] = "."
                    self.moves += 1
                
                else:
                    raise Exception("Error: invalid move")
            
            else:
                raise Exception("Error: invalid move") 
            
        # right direction
        # if a move is not in the ifs then it is not valid and raise exception
        if move[1] == "r":
            # position has to be within range
            if position >= 0 and position < len(self.toprow)-1:
                # right has to be "empty" and position has to have something to move
                if self.toprow[position]!= "." and self.toprow[position+1] == ".":
                    # perform move
                    temp = self.toprow[position]
                    self.toprow[position+1] = temp
                    self.toprow[position] = "."
                    self.moves += 1
                
                else:
                    raise Exception("Error: invalid move")   
            else:
                raise Exception("Error: invalid move")   
        
        # left position
        # if a move is not in the ifs then it is not valid and raise exception
        if move[1] == "l":
            # position has to be within range
            if position > 0 and position <= len(self.toprow)-1:
                # left has to be "empty" and position has to have something to move
                if self.toprow[position]!= "." and self.toprow[position-1] == ".":
                    # perform move
                    temp = self.toprow[position]
                    self.toprow[position-1] = temp
                    self.toprow[position] = "."
                    self.moves += 1
                
                else:
                    raise Exception("Error: invalid move")   
            else:
                raise Exception("Error: invalid move")   
    
    
    def removedots(self, alist):
        '''
        Removes the "." from each stack in the list of stacks.
        
        Parameters: 
        alist (str): list of BStacks
        
        Returns: None
        '''          
        # use peek() and pop()
        # if peek() is "." then pop() until it is not
        for item in alist:
            tracker = 0
            while tracker < self.depth:
                if item.peek() == ".":
                    item.pop()
                tracker += 1
                
    def pushdots(self, alist):
        '''
        Add "." to each stack in the list of stacks, until all stacks are full.
        
        Parameters: 
        alist (str): list of BStacks
        
        Returns: None
        '''        
        # as long as capacity is not reached then add "." to each stack
        for item in alist:
            while item.size() < item.capacity():
                item.push(".")    
     
    
    def isSolved(self, card):
        '''
        Returns TRUE if the state of the instance corresponds to the 
        configuration card, FALSE otherwise.
        
        Parameters: 
        card (Card): instance of Card Class
        
        Returns: TRUE if the state of the instance corresponds to the 
        configuration card, FALSE otherwise
        '''        
        
        valid = True
        
        # check each stack one at a time
        for i in range(self.stacks):
            strcard = ' '.join(card.stack(i+1))   # stack from card as a string
            strgame = str(self.listofstacks[i])   # stack from game as a string
            strgamer = strgame[::-1]     # reverse the stack from game to compare
            
            # compare and only return true if all stacks are the same
            if strcard != strgamer:
                valid = False
                
        
        return valid
    
    
    def reset(self):
        '''
        Resets the number of moves to zero and rearrange the stack to the initial 
        position with each stack having its own beads.
        
        Parameters: 
        None
        
        Returns: None
        '''          
        
        # follow the codes used to create the board in init
        self.listofstacks = []
        self.toprow = []
        self.moves = 0
        
        for i in range(self.stacks + 2):
            self.toprow.append(".")           
        
        for i in range(self.stacks):
            astack = BStack(self.depth)
            for index in range(self.depth):
                astack.push(chr(i + 65))  
            self.listofstacks.append(astack)
            
    
    def show(self, card = None):
        '''
        Takes an optional parameter card and displays the state of the AbacoStack instance.
        When the parameter card is provided, card config is displayed beside AbacoStack 
        instance in addition to the number of moves.
        
        Parameters: 
        card (Card): instance of Card Class
        
        Returns: None
        '''          
                
        # call pushdots to all "." to all stacks until full
        # this helps with displaying
        self.pushdots(self.listofstacks)
        
        # print the numbers
        for i in range(len(self.toprow)):
            print(i, end = " ")
        print()
        
        # print the top row
        for item in self.toprow:
            print(item, end = " ")
        if card!= None:     # if card is provided
            print(" "*(len(self.listofstacks)+1), "card")   # formatting
        else:
            print()
        
        # print each row at a time    
        for i in range(self.depth):
            print("| ", end = "")
            # iterate through all the stacks
            # print the element at the correct index for each stack
            for index in range(len(self.listofstacks)):
                # get stack as a str and the locate the letter by calculating the index
                print(self.listofstacks[index].joiningstack()[self.depth-1-i], end = " ")
            
            # if card is provided then contiune printing on same row            
            if card != None:          
                print("|    |", end = "")
                # iterate through all stacks of card by calling stack() each time
                for index in range(len(self.listofstacks)): 
                    # get stack as str first the locate index
                    temps = ''.join(card.stack(index+1))
                    # last letter not followed by space
                    if index == len(self.listofstacks)-1 :
                        print(temps[i], end = "")
                    else:
                        print(temps[i], end = " ")
            
            print("|")
        
        # values to proper format    
        value = (len(self.listofstacks))*2 + 1
        value2 = (len(self.listofstacks))*2 + 1 + 5
        
        # display total moves on last line if card is provided
        if card!= None:
            print("+" + "-"*value + "+" + " "*value2, self.moves, "moves" )
        else:
            print("+" + "-"*value + "+")
                    

        

def main():
    
    card1 = Card(3,3)
    card1.show()
    card1.reset()
    card1.show()
    print(card1.stack(1))
    print(card1.stack(2))
    print(card1.stack(3))    
    print(str(card1))
    # tested using the example on eclass and produced same config
    card1.replace("test.txt", 0)
    card1.show()
    
    # many functions are implemented following stack in lecture and labs and tested
    stack1 = BStack(3)
    stack1.push("a")
    stack1.push("b")
    stack1.push("c")
    temp = stack1.pop()
    print(temp)
    stack1.show()
    print(str(stack1)+"p")
    stack1.push(".")
    print(stack1.joiningstack()[0])
    print(stack1.joiningstack())
    print(stack1.isFull())
    
    # test for abacostack:
    game1 = AbacoStack(3,3)
    game1.show(card1)
    game1.moveBead("1u")
    game1.show()
    game1.moveBead("1l")
    game1.show()  
    game1.moveBead("2u")
    game1.show()   
    game1.moveBead("2l")
    game1.show()   
    game1.moveBead("1d")
    game1.show(card1) 
    print(game1.isSolved(card1))
    
    game1.reset()
    game1.show(card1)
    
    try:
        game1.moveBead("0u")
    except Exception as moveError:
        print(moveError.args)


if __name__ == '__main__':
    main()