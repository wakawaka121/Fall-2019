####
#### Author: Derek Tominaga
#### Description: Prints a shape with fucntions
#### while taking input for, the shape displayed,
#### a symbol to display with, and an int value
#### to dictate row height


def get_design(shape):
    while not shape.isalpha():
        if not shape.isalpha():
            shape = input("Enter shape to display:")
        else:
            return shape
# function to get validate shape
def print_up_arrow(character):
    count = 1
    while count <=6:
        print (" " * (6 - count) + character * ((count*2)-1) + " " * (6 - count ))
        count += 1
# function to print an up arrow, taking a parameter of an input character
def print_down_arrow(character):
    count = 6
    while count >= 1:
        print (" " * (6 - count) + character * ((count*2)-1) + " " * (6 - count ))
        count -= 1
# function to print down arrow, taking a parameterof an input character
def row_height(height):
    print ("|---------|\n" * height, end = "")
# function to print row-height, dictated by int value taken from input
def main():
    shape = input ("Enter shape to display:\n")
    get_design(shape)
    character = str (input ("Enter arrow character:\n"))
    height = int (input("Enter row-area height:\n"))
    if shape == "hourglass":
        print("")
        row_height(height)
        print_down_arrow(character)
        print_up_arrow(character)
        row_height(height)
    elif shape == "plumbbob":
        print ("")
        print_up_arrow(character)
        row_height(height)
        print_down_arrow(character)
    elif shape == "house":
        print("")
        print_up_arrow(character)
        row_height(height)
# main function that prints based on the shape specified
# each shape will call the functions required to print that shape.
main()
