# Assignment 2 task 1
#
# Author: Mike Zhang 1555800 
#
# Takes in a corrupted file where words separated by “#” a few per line.
# Generates a new file where there is one word per line. 


def main():
    '''
    Main function of the program. Read the word5Dict.txt file and generate a new
    file scrabble5.txt where there is one word per line.
    
    Parameters: none
    
    Returns: None
    '''     

    # read the text file
    file = open('word5Dict.txt','r')
    content = file.readlines()    # returns a list where elements are lines
    file.close()
    
    # writing to new file
    newfile = open('scrabble5.txt','w')
    
    for line in content:
        line = line.strip()     # remove newline at the end of line
        line = line.strip("#")   # remove "#" at the end of the line
        line = line.split("#")   # split line at # into a list
        for word in line:
            newfile.write(word + '\n')
    
    # closes the file after writing   
    newfile.close()

main()