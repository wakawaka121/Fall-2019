###
### Author: Derek Tominaga
### Description: Print with alingnment to the
### right, using a while loop
###

string = input ("Enter bar string:\n")
## get user input (as a number)
rows = len(string)
## determine length of string
count = 1
## an index/counter
print ("+" + "-" * 9 + "+")
## sets top border
while count <= rows:
    hashtags = int (string[count - 1])
    ## determines the character at an index and converts to a int data type
    print("|" + " " * (9 -hashtags) + "#" * (hashtags) + "|")
    count += 1
## set of code to determine how mnay hashtages to print
## run as many times as the length of the string input.
print ("+" + "-" * 9 + "+")
## sets bottom border