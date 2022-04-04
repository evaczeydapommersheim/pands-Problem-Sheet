# This program reads in text file moby-dick.txt, then outputs the number of e's it contains.
# The program is to take the filename from an argument on the command line.

# Author: Eva Czeyda-Pommersheim

# create a file called moby-dick.txt using the request module in python
# in order to get access to the text file of the book Moby Dick. The request module uses the URL
# to access the file content and it creates the moby-dick.txt file in the folder where the program will run
# sources: https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-urllib3-and-requests-modul
#  https://www.gutenberg.org/files/2701/old/moby10b.txt

import requests
file = "moby-dick.txt"
with open(file, "wt") as f1:
    f1.write((requests.get('https://www.gutenberg.org/files/2701/old/moby10b.txt').text))

# using the import sys module so that this file can be accessed as an argument in the command line
# argv[1] being the second element of the list object that is created by importing sys module
# and using it to add argument via the command line
import sys
filename = sys.argv[1]
with open(filename, 'rt') as f:     # opens the file defined under the argv[1]
    content = f.read()              # reads the file
print(content.count("e"))           # using the count() Python String method (https://www.w3schools.com/python/python_ref_string.asp) it counts the number of string/character "e"