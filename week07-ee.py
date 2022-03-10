# This program reads in text file created as week07CreateFile.py, then outputs the number of e's it contains.

# Author: Eva Czeyda-Pommersheim

def letterQuantity():       #defining a function to do the required subtasks (researched online best ways to count a character in a text)
    #1. we need to read in the text file.
            # Sources: https://www.pythontutorial.net/python-basics/python-read-text-file/ // https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
    # moby-dick file was found in Github as js file: https://gist.github.com/StevenClontz/4445774.js
    # Researching how to read in a js file to python (st.github.com/StevenClontz/4445774.js").

    # js is for Java Script, there is a module in python "js2py" which translates 
    # Source:  https://www.infoworld.com/article/3209651/how-to-convert-python-to-javascript-and-back-again.html
    file = open("fileName/URL", 'r')

    #2. The file content would need to be stored as a variable
    content = file.read()

    #3. Use the count() method to as explained in W3 Schools () syntax being: list.count(value) Any type (string, number, list, tuple, etc.). The value to search for.
    # Source: https://www.w3schools.com/python/ref_list_count.asp
    return content.count("e")

    #4. display the number of characters
print(letterQuantity("fileName/URL", "e"))
    
