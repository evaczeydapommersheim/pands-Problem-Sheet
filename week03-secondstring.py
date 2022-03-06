# This is my solution for Week03 Weekly task
# This program is to read in a sentence
# Output every second letter of the sentence in a reversed order

# Author: Eva Czeyda-Pommersheim

sentence = input("Please enter a sentence: ") # when the sentence "The quick brown fox jumps over the lazy dog." is typed in the output shuold be ".o zletrv pu o wr cu h".
print(sentence[::-2])  

# used the slicing of a string based on https://docs.python.org/3/library/functions.html#slice and 
# googling "read every second letter python code" and reviewing result:https://stackoverflow.com/questions/36003289/write-programs-that-read-a-line-of-input-as-a-string-and-print-every-second-lett/37201212