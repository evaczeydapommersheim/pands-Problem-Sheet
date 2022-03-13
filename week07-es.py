# This program reads in text file created as week07CreateFile.py, then outputs the number of e's it contains.

# Author: Eva Czeyda-Pommersheim

# create a file called moby-dick.txt using the request module in python
# in order to get access to the text file of the book Moby Dick using a URL
# by using writing the file it will be created in the folder where the program will run
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
print(content.count("e"))           # using the count() built in function it counts the number of string/character "e"