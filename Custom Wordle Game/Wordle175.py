# Assignment 2 task 2 (and task 4)
#
# Author: Mike Zhang 1555800 
#
# Create the ScrabbleDict class and implement the required methods

class ScrabbleDict:
    
    def __init__(self, size, filename):
        '''
        Initializes a dictionary using the content of the file specified by filename.
        The keys are the first element of each line where its length is equal to the
        specified size. The value in the dictionary would be the full line. 
        
        Parameters: 
        size (int): specified length of the keys in dictionary
        filename (file): name of the file to be read and used in creating dictionary
        
        Returns: None
        '''         
        # Initialize dictionary and key length
        self.dictionary = {}
        self.size = size
        
        # read the text file
        file = open(filename,'r')
        content = file.readlines()    # returns a list where elements are lines
        file.close()
        
        for line in content:
            line = line.strip()    # remove newline at the end of line
            newline = line.split()    # split line at space into a list
            # check for length of first element of splitted line
            if len(newline[0]) == self.size:
                self.dictionary[newline[0]] = line
            
    
    def check(self, word): 
        '''
        Check if a word in is the dictionary by checking through the keys.
        
        Parameters: 
        word (str): the word to be checked 
        
        Returns: True if word is in the dictionary and False otherwise
        '''               
        # look for word in the dictionary keys to check
        if word in self.dictionary.keys():
            return True
        
        else:
            return False
        
    
    def getSize(self): 
        '''
        Returns the number of words in the dictionary using the keys
        
        Parameters: none
        
        Returns: number of words in the dictionary as int
        '''        
        # obtain the number of words using the length of all keys
        return len(self.dictionary.keys())
    
    def getWords(self, letter): 
        '''
        Find all the words in dictionary keys that start with the specified letter,
        then return them in a sorted list.
        
        Parameters: 
        letter (str): the specified starting letter
        
        Returns: 
        relatedwords (list): sorted list of all words in dictionary with the starting letter
        '''         
        # sort all the dictionary keys first
        sortedwords = sorted(self.dictionary.keys())
        
        relatedwords = []
        
        # go through the sorted keys, if the key starts with the specified letter then append to list
        for word in sortedwords:
            if word[0] == letter:
                relatedwords.append(word)
        
        return relatedwords
    
    
    def getWordSize(self): 
        '''
        Returns the length of the words stored in the dictionary, which is the
        length of every key.
        
        Parameters: none
        
        Returns: 
        self.size (int): value size provided when initializing the dictionary
        '''         
        # return length of every key
        return self.size
    
    def getMaskedWords(self, template):
        '''
        Find all the words in dictionary keys that follow the template provided, 
        where * can be any letter. Return all the words in a sorted list.
        
        Parameters: 
        template (str): the template used to check for compatible words
        
        Returns: sorted list that contains all the compatible words
        '''          
        # obtain how many letters are in the template
        lettercount = self.size - template.count("*")
        
        wordlist =[]   # list of compatible words
        
        # if the template only has *, then all the words are compatible
        if lettercount == 0:
            return sorted(list(self.dictionary.keys()))    # return all the keys sorted
        
        # if the template contains at least one letter
        else:
            # go through all the words
            for word in self.dictionary.keys():
                tracker = 0    # tracks how many letters match at the right position
                # if letter in word matches letter in template at the right index
                # tracker increase by 1
                for index in range(self.size):
                    if word[index] == template[index]:
                        tracker = tracker+1
                # word is compatible if and only if tracker is the same as 
                # the number of letters in the template, this means every letter 
                # matches at the right position
                if tracker == lettercount:
                    wordlist.append(word)     # only add compatible words
        
        # returns sorted list with all compatible words
        return sorted(wordlist)
                        
    def getConstrainedWords(self, template,letters):
        '''
        Find all the words in dictionary keys that follow the template provided, 
        and *s can be replaced by a letter from letters. Return the words in a sorted list.
        
        Parameters: 
        template (str): the template used to check for compatible words
        letters (list): list of characters to replace wildcards
        
        Returns: sorted list of words that follow the template provided and 
        the wildcards can be replaced by a letter from the letters
        '''          
        # first call getMaskedWords() methods to obtain list of words compatible with template
        templatelist = self.getMaskedWords(template)
        
        # create a new list
        new_templatelist = []
        
        # if letters is empty then templatelist is the compatible list of words
        if len(letters) == 0:
            return templatelist
        
        # if user input additional letters for hint
        else:
            # create new list based on templatelist, where each word is modified so
            # that if the letter already matches with the template it is replaced with a space. 
            for word in templatelist:
                word_aslist = list(word)    # convert word to list to modify
                for index in range(self.size):    # iterate over every index of word
                    if template[index] != "*":    # means template at this index is a letter
                        word_aslist[index] = " "   # modify the word at the same index to space
                # obtain new list with words that have spaces in them
                new_templatelist.append("".join(word_aslist))    # join to convert list to str
            
            # create list that will be returned
            returnlist = [] 
            
            # iterate over the new list where words have spaces
            for word in new_templatelist:
                tracker = 0     # refreshes tracker to 0 for every word check
                # check if each letter from user is in the word with spaces
                for letter in letters:
                    if letter in word:
                        tracker += 1   # tracker increase if a letter is in word
                # only when all the letters input by user are in a word can this word
                # be compatible. This occurs when the tracker equals length of letters
                if tracker == len(letters):
                    # newlist where words have spaces has the same "word" at each index
                    # as template list, the compatible word is obtained from templatelist
                    returnlist.append(templatelist[new_templatelist.index(word)])
            
            # return list of compatible words 
            return returnlist
                    
    
    def returnkeys(self):
        '''
        Return all words in dictionary to be used to other program for convenience
        
        Parameters: none
        
        Returns: all keys of dictionary
        '''              
        return self.dictionary.keys()
    
    
    # method used for testing purpose to ensure dictionary initalized correctly
    
    # def returndict(self):
    #    return self.dictionary    


def main():
    '''
    Main function of the program. Used to test all the methods for class ScrabbleDict.
    
    Parameters: none
    
    Returns: None
    '''     
    # tests
    
    # following will not create a dictionary because every word in txt file has length 5
    # dict2 = ScrabbleDict(6, 'scrabble5.txt')
    
    # create instance of class ScrabbleDict
    dict1 = ScrabbleDict(5, 'scrabble5.txt')
    # print(dict1.returndict())   # test if dictionary initialized correctly
    
    # following prints True
    print(dict1.check("aahed"))
    
    # following prints False
    print(dict1.check("abcde"))
    
    # following prints how many words which is 8913
    print(dict1.getSize())
    
    # following prints sorted list of all words that start with z
    print(dict1.getWords("z"))
    
    # following prints size of word which is 5
    print(dict1.getWordSize())
    
    # following prints sorted list of all words that is compatible with the template
    words = dict1.getMaskedWords('t**er')
    print(words)
    
    # following prints sorted list of all words compatible with template and additional letters
    words2 = dict1.getConstrainedWords('t**er', ["i"])
    print(words2)
    
    
if __name__ == "__main__":
    main()