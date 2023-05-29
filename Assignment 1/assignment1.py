# Assignment 1   
#
# Author: Mike Zhang 1555800 
#
# Take in 4 text files that contain information for books, students, borrow list
# and return list respectively. The the program will generate a new text file that
# contains 2 tables for each classroom: list of books not returned yet along with student
# name and due date, list of student that owns money to the library and amounts due. 


def create_bookdict():
    '''
    Read the books.txt file and generate a dictionary where the keys are the
    book IDs and values are name, author, and price in a list.
    
    Parameters: none
    
    Returns:
    dict_books (dict): dictionary for all books
    '''   
    # read the text file
    file = open('books.txt','r')
    content = file.readlines()    # returns a list where elements are lines
    file.close()
    
    dict_books = {}
    
    for line in content:
        line = line.strip()     # remove newline at the end of line
        line = line.split("#")   # split line at # into a list
        entries = []
        # add all entries of the splitted line from index 1 to the end to a list
        for entry in range(1,len(line)):
            entries.append(line[entry]) 
        # create dictionary where keys are first entry of line, values are everything after in a list
        dict_books[line[0]] = entries
            
    return dict_books


def create_studict():
    '''
    Read the students.txt file and generate a dictionary where the keys are the
    student IDs and values are name and classroom in a list.
    
    Parameters: none
    
    Returns:
    dict_stu (dict): dictionary for students
    '''        
    # read the text file
    file = open('students.txt','r')
    content = file.readlines()    # returns a list where elements are lines
    file.close()
    
    dict_stu = {}
    
    for line in content:
        line = line.strip()     # remove newline at the end of line
        line = line.split(",")    # split line at , into a list
        entries = []
        # add all entries of the splitted line from index 1 to the end to a list
        for entry in range(1,len(line)):
            entries.append(line[entry])
        # create dictionary where keys are first entry of line, values are everything after in a list
        dict_stu[line[0]] = entries
            
    return dict_stu


def create_classdict():
    '''
    Read the students.txt file and generate a dictionary where the keys are the
    classrooms and values are names of students in that class in a list.
    
    Parameters: none
    
    Returns:
    dict_cla (dict): dictionary for classrooms
    '''          
    # read the text file
    file = open('students.txt','r')
    content = file.readlines()    # returns a list where elements are lines
    file.close()
    
    allclass = []    
    for line in content:
        line = line.strip()
        line = line.split(",")
        allclass.append(line[-1])    # list of every line's last entry which are all the classrooms 
    
    # convert list of all classrooms to a set so duplicates are removed
    unique_class = set(allclass)
    # convert set back to list of unique classrooms then sort it
    sortedclass = sorted(list(unique_class))
    
    dict_cla = {}
    
    for value in sortedclass:
        entries = []
        # create a list of student names for every classroom
        for line in content:
            line = line.strip()
            line = line.split(",")
            if line[-1] == value:     # check if student is in this classroom
                entries.append(line[1])    # append student name for easier comparison later
        # create dictionary where keys are classroom names and values are students names in a list
        dict_cla[value] = entries
            
    return dict_cla


def create_borrowdict():
    '''
    Read the borrowers.txt file and generate a dictionary where the keys are the
    book IDs and values are student ID that borrowed it, borrow date, and due date in a list.
    
    Parameters: none
    
    Returns:
    dict_bor (dict): dictionary for borrows
    '''           
    # read the text file
    file = open('borrowers.txt','r')
    content = file.readlines()    # returns a list where elements are lines
    file.close()
    
    dict_bor = {}
    
    for line in content:
        line = line.strip()     # remove newline at the end of line
        line = line.split(";")     # split line at ; into a list
        entries = []
        # add all entries of the splitted line from index 1 to the end to a list
        for entry in range(1,len(line)):
            entries.append(line[entry])
        # create dictionary where keys are first entry of line, values are everything after in a list
        dict_bor[line[0]] = entries
            
    return dict_bor


def create_returndict():
    '''
    Read the returns.txt file and generate a dictionary where the keys are the
    book IDs and values are student ID that borrowed it, return date, and state of book in a list.
    
    Parameters: none
    
    Returns:
    dict_ret (dict): dictionary for returns
    '''        
    # read the text file
    file = open('returns.txt','r')
    content = file.readlines()    # returns a list where elements are lines
    file.close()
    
    dict_ret = {}
    
    for line in content:
        line = line.strip()     # remove newline at the end of line
        line = line.split(";")     # split line at ; into a list
        entries = []
        # add all entries of the splitted line from index 1 to the end to a list
        for entry in range(1,len(line)):
            entries.append(line[entry])
        # create dictionary where keys are first entry of line, values are everything after in a list
        dict_ret[line[0]] = entries
            
    return dict_ret


def convert_date(date):
    '''
    Take in a date represented as a string of 6 numbers and convert it into 
    mmm dd, yyyy format as a string.
    
    Parameters: 
    date (str): date as a 6 characters string of numbers
    
    Returns:
    time (str): string that represents a day in mmm dd, yyyy format
    '''       
    # take first 2 characters of date and obtain a year in the 21th century
    year = '20' + date[0:2]
    
    # take middle 2 characters of date and obtain the 3 letter month correspond to it
    months = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
    month = months[int(date[2:4])-1]
    
    # take the last 2 characters of date and obtain the day
    day = date[4:6]
    
    # concatenate and get date in the right format
    time = month + ' ' + day + ', ' + year
    
    return time


def difference_keys(dict1, dict2):
    '''
    Take in 2 dictionaries and generate a list that contains keys that are only present 
    in the first dictionary.
    
    Parameters: 
    dict1 (dict): first dictionary
    dict2 (dict): second dictionary
    
    Returns:
    keydif (list): list that contains all the keys that are in dictionary 1 but not 2
    '''       
    # obtain list of keys for each dictionary
    list1 = dict1.keys() 
    list2 = dict2.keys()
    
    # compare and get list of keys only in dictionary 1
    keydif = []
    for key in list1:
        if key not in list2:
            keydif.append(key)
    
    # return list of book IDs only in dictionary 1
    return keydif    


def table1_data(key,dict_books,dict_stu,dict_borrow):
    '''
    Create a list that contains values associated with the book ID passed in which will
    be used in table 1. This includes the name of the book, name of the student who
    borrowed it, and the due date.
    
    Parameters: 
    key (str): book ID from the list of books not returned
    dict_books (dict): dictionary for all books 
    dict_stu (dict): dictionary for all students
    dict_borrow (dict): dictionary for borrows   
    
    Returns:
    values (list): list that contains values associated with the not returned book for table 1
    '''            
    values = []
    
    # obtain student ID through borrow dictionary first
    # obtain student name that borrowed the book using student dictionary
    values.append(dict_stu[dict_borrow[key][0]][0])
    
    # obtain name of the book using book dictionary
    values.append(dict_books[key][0])
    
    # obtain due date by calling the convert_date() function
    due = convert_date(dict_borrow[key][2])
    values.append(due)
    
    # return list that contains student name, book name, and due date
    return values  


def book_dues(dict1):
    '''
    Take in a dictionary and generate a list of keys where the last entry 
    of the value associated with the key is not 0,2,or 3.
    
    Parameters: 
    dict1 (dict): dictionary for returns   
    
    Returns:
    list_of_dues (list): list that contains all keys whose value's last entry is not 0,2 or 3
    '''       
    
    list_of_dues = []
    
    # check if last entry of the key's value is 0,2,or 3, if not then append key to list
    for key in dict1.keys():
        if dict1[key][-1] not in ['0','2','3']:
            list_of_dues.append(key)
    
    # return list of keys which are books IDs 
    return list_of_dues
            

def table2_data(key,dict_books,dict_stu,dict_return):
    '''
    Create a list that contains values associated with the book ID passed in which will
    be used in table 2. This includes name of the student who returned it and the price of book.
    
    Parameters: 
    key (str): book ID from the list of books where the dues are not paid
    dict_books (dict): dictionary for all books 
    dict_stu (dict): dictionary for all students
    dict_return (dict): dictionary for returns   
    
    Returns:
    values (list): list that contains all values associated with the returned book for table 2
    '''       
    
    values = []
    
    # obtain student ID through return dictionary first
    # obtain student name that returned the book using student dictionary 
    values.append(dict_stu[dict_return[key][0]][0])
    
    # obtain price of book using book dictionary
    values.append(dict_books[key][-1])
    
    # return list that contains student name and book price
    return values
    
    
def display_table1(newfile,sorted_not_returned,dict_class,cla,total_bor):
    '''
    Write table 1 for the classroom to the new text file following the right formatting.
    Display the total books of the classroom to the screen.
    
    Parameters: 
    newfile: the file to be write in
    sorted_not_returned (list): lists of list where each list contains values 
                                (student name, book name and due date) associate with the not returned book
    dict_class (dict): dictionary for classrooms 
    cla (str): the classroom name
    total_bor (int): total books not returned yet for the classroom 
    
    Returns: None
    '''      
    # write top of table
    newfile.write("Class: " + cla +'\n')
    newfile.write("+" + "-"*18 + "+" + "-"*37 + "+" + "-"*14 + "+" +'\n')
    newfile.write("| " + f'{"Student Name":<16}'+ " | " + f'{"Book":<35}' + " | " + f'{"Due Date":<12}' + " |" +'\n')
    newfile.write("+" + "-"*18 + "+" + "-"*37 + "+" + "-"*14 + "+" +'\n')
    
    # for every classroom, go through the sorted list of lists (sorted_not_returned) passed in 
    # where each list contains values associated with a not returned book: stu name, book name, due date
    for entry in sorted_not_returned:
        # if student name is in the classroom by checking classroom dictionary
        # then print the values which are student name, book name, due date in right format
        if entry[0] in dict_class[cla]:
            newfile.write("| " + f'{entry[0][0:16]:<16}'+ " | " + f'{entry[1][0:35]:<35}' + " | " + entry[2] + " |" +'\n')
            total_bor += 1     # keep track of total not returned book for the class
    # if no books for the classroom then write No Books
    if total_bor == 0:
        newfile.write(f'{"No Books":^73}' +'\n')
    
    # write bottom of table
    newfile.write("+" + "-"*18 + "+" + "-"*37 + "+" + "-"*14 + "+" +'\n')
    newfile.write("| " + f'{"Total Books":<54}' + " | " + f'{total_bor:>12}' + " |" +'\n')   # total for class
    newfile.write("+" + "-"*18 + "+" + "-"*37 + "+" + "-"*14 + "+" +'\n')
    print("Total books currently borrowed:",total_bor)   # print summary to screen


def display_table2(newfile,sorted_book_dues,dict_class,cla,total_due):
    '''
    Write table 2 for the classroom to the new text file following the right formatting.
    Display the total dues of the classroom to the screen.
    
    Parameters: 
    newfile: the file to be write in
    sorted_book_due (list): lists of list where each list contains values 
                            (student name and amount due) associate with the returned book
    dict_class (dict): dictionary for classrooms 
    cla (str): the classroom name
    total_due (int): total amount due for the classroom 
    
    Returns: None
    '''        
    
    # write top of table   
    newfile.write("+" + "-"*18 + "+" + "-"*10 + "+" +'\n')
    newfile.write("| " + f'{"Student Name":<16}'+ " | " + f'{"Due":<8}' + " |" +'\n')
    newfile.write("+" + "-"*18 + "+" + "-"*10 + "+" +'\n')
    
    # for every classroom, go through the sorted list of lists (sorted_book_dues) passed in 
    # where each list contains values associated with a book that has dues: stu name and book price    
    for due in sorted_book_dues:
        # if student name is in the classroom by checking classroom dictionary
        # then print the values which are student name and amount due in right format        
        if due[0] in dict_class[cla]:
            price = "${:.2f}".format(float(due[1]))   # format price and add leading dollar sign
            newfile.write("| " + f'{due[0][0:16]:<16}'+ " | " + f'{price:>8}' + " |" +'\n')
            total_due += float(due[1])     # keep track of total dues for class
    # if no dues for the classroom then write No dues
    if total_due == 0:
        newfile.write(f'{"No dues":^31}' +'\n')
    
    # write bottom of table 
    newfile.write("+" + "-"*18 + "+" + "-"*10 + "+" +'\n')
    totalprice = "${:.2f}".format(total_due)   # format price and add leading dollar sign
    newfile.write("| " + f'{"Total Books":<16}' + " | " + f'{totalprice:>8}' + " |" +'\n')   # total dues for class
    newfile.write("+" + "-"*18 + "+" + "-"*10 + "+" +'\n')
    newfile.write('\n')
    print("Total amount due for books:",totalprice +'\n')   # print summary to screen
 

def main():
    '''
    Main function of the program. Create the 5 dictionaries, obtain list of books not returned
    and list of books that have dues, get the required values for each book in those 2 lists,
    then write to new file following the right formatting. All of the above are achieved by calling
    the specific functions for each task. 
    
    Parameters: none
    
    Returns: None
    '''       
    
    # create dictionary for books, students, classrooms, borrows and returns 
    # by calling the respective function    
    dict_books = create_bookdict()
    dict_stu = create_studict()  
    dict_class = create_classdict()
    dict_borrow = create_borrowdict()   
    dict_return = create_returndict()
    

    # table 1:
    
    # call difference_keys() function to get list of book IDs that are not returned yet
    not_returned = difference_keys(dict_borrow,dict_return)
      
    # obtain a list of lists where each list contains values correspond to a not returned book
    # the values are: student name that borrowed the book, the book name, and due date respectively
    list_of_all_not_returned = []
    # for every book ID that is not returned, call table1_data() function and get the values associated with it in a list
    for key in not_returned:
        list_of_all_not_returned.append(table1_data(key,dict_books,dict_stu,dict_borrow))
    
    # sort the list of lists so it is in alphabetical order of student name which is the first entry of every list   
    sorted_not_returned = sorted(list_of_all_not_returned)
    
    
    # table 2
    
    # call book_dues() function to get list of book IDs that have money owned
    book_due = book_dues(dict_return)
    
    # obtain a list of lists where each list contains values correspond to a book that have money owned
    # the values are: student name that returned the book and the book price    
    list_of_dues = []
    # for every book ID that is not paid, call table2_data() function and get the values associated with it in a list
    for key in book_due:
        list_of_dues.append(table2_data(key,dict_books,dict_stu,dict_return)) 
    
    # sort the list of lists so it is in alphabetical order of student name which is the first entry of every list
    sorted_book_dues = sorted(list_of_dues)
    
    
    # display 
    
    # writing to new file
    newfile = open('standing.txt','w')
    
    # go through all the classrooms, for each classroom call display_table1() and
    # display_table2() functions to write the tables and display info on screen
    for cla in dict_class.keys():
        total_bor = 0     # keep track of total number of borrowed books for the class
        total_due = 0     # keep track of total amount due for the class
        print("Class:", cla)
        # call display functions and pass in the 5 arguments
        display_table1(newfile,sorted_not_returned,dict_class,cla,total_bor)
        display_table2(newfile,sorted_book_dues,dict_class,cla,total_due)
    
    # closes the file after writing   
    newfile.close()    

main()