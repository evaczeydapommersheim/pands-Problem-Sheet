# This program reads in text file created as week07CreateFile.py, then outputs the number of e's it contains.

# Author: Eva Czeyda-Pommersheim

filename = r"C:\Users\Dancsa\Desktop\GMIT_PANDS2022\Evawork\week07\moby-dick.txt" 
# SyntaxError: (unicode error) 'unicodeescape' codec 
# can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
# above message was received when running the program 
# googled the error message and selected the solution to add an r before the path, 
# alternative solution could have been to add double backward slash as a separator(\\)
# Source: https://exerror.com/syntaxerror-unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-truncated-uxxxxxxxx-escape/

def letterQuantity(filename):       #defining a function to do the required subtasks (researched online best ways to count a character in a text)
    #1. we need to read in the text file.
    # Sources: https://www.pythontutorial.net/python-basics/python-read-text-file/ // https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
    
   with open(filename, 'rt') as f:
       content = f.read() #2. The file content would need to be stored as a variable
       return content.count("e") 
        #3. Use the count() method to as explained in W3 Schools () syntax being: list.count(value) Any type (string, number, list, tuple, etc.). The value to search for.
        # Source: https://www.w3schools.com/python/ref_list_count.asp
   
    #4. display the number of characters
letterE = letterQuantity(filename)
print(letterE)
