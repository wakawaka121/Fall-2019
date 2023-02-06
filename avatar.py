####
#### Author: Derek Tominaga
#### Description: This program allows a user to create an
#### avatar. They can choose from presets, or make their own
#### with variables for: Hat, Hair, Eyes, Arms, Body length,
#### Leg length, and Shoe look
####

def start_up_prompt():
    '''
    This funciton returns an input string
    while validating that the input srting is one of
    either accepted input of: exit, custom, Jeff, Adam or Chris
    '''
    avatar_selection = input ("Select an Avatar or create your own:\n")
    while avatar_selection.isalpha():
        if avatar_selection == "exit":
            return avatar_selection
        elif avatar_selection == "Jeff":
            return avatar_selection
        elif avatar_selection == "Adam":
            return avatar_selection
        elif avatar_selection == "Chris":
            return avatar_selection
        elif avatar_selection == "custom":
            print ("Answer the following questions to create a custom avatar")
            return avatar_selection
        else:
            avatar_selection = input ("Select an Avatar or create your own:\n")
def hat(direction):
    '''
    This function prints the custom avatars hat with direction parameters
    direction: is a string and determines how the hat is printed
    '''
    if direction == "left":
        print ("\n" + "       ~-~")
        print ("     /-~-~-\\")
        print (" ___/_______\\")
    elif direction == "right":
        print ("\n" + "       ~-~")
        print ("     /-~-~-\\")
        print ("    /_______\\___")
    elif direction == "both":
        print ("\n" + "       ~-~")
        print ("     /-~-~-\\")
        print (" ___/_______\\___")
    elif direction == "front":
        print ("\n" + "       ~-~")
        print ("     /-~-~-\\")
        print ("    /_______\\")
def face(hair,eyes):
    '''
    This function prints the custom avatar face with hair and face parameters
    hair: is a string (shaggy(true)/not shaggy(false))
    eyes: is one string character used to represent the avatars eyes
    '''
    if hair == "True":
        print ('    |"""""""|')
    else:
        print ("    |'''''''|")
    print ("    |", eyes + "  ", eyes, "|")
    print ("    |   V   |")
    print ("    |  ~~~  |")
    print ("     \_____/")
def arms(arm_symbol):
    '''
    This function prints arms of the custom avatar with arm_symbol parameter
    arm_symbol: is one string character used to represent style of the
    avatar's arms
    '''
    arm_print = " 0"
    count = 0
    while count < 4:
        arm_print += arm_symbol
        count += 1
    arm_print += "|---|"
    while count > 0:
        arm_print += arm_symbol
        count -= 1
    arm_print += "0"
    print (arm_print)
def torso(body_length):
    '''
    This function prints the body of the custom avatar with body_length parameter
    body_length: is an int value, used to loop through to avoid string multiplicaiton
    '''
    count = 0
    while count < body_length:
        print ("      |-X-|")
        count += 1
def legs(leg_length, shoe_look):
    '''
    This function prints the "belt" legs and shoes of the custom avatar
    with leg_length and shoe_look parameters.
    leg_length: is a int value used to determine how longs the legs must be.
    shoe_look: is a string value used to represnt the avatars shoes.
    '''
    max_leg_layout = "///       "
    count = 0
    leg_width_count = 2
    print ("      HHHHH")
    while count < leg_length:
        print (max_leg_layout[3:(8 - count)] + max_leg_layout[0:2 + leg_width_count] + "\\\\\\")
        count += 1
        leg_width_count += 2
    print (shoe_look + "       " + shoe_look)
def avatar_jeff():
    '''
    This function prints a preset "Jeff" avatar
    functions are called with set arguments
    to follow design
    '''
    hat("both")
    face("True","0")
    arms("=")
    torso(2)
    legs(2, "#HHH#")
def avatar_adam():
    '''
    This function prints a preset "Adam" avatar
    functions are called with set arguments
    to follow design
    '''
    hat("right")
    face("False","*")
    torso(1)
    arms("T")
    torso(3)
    legs(3, "<|||>")
def avatar_chris():
    '''
    This function prints a preset "Chris" avatar
    functions are called with set arguments
    to follow design
    '''
    hat("front")
    face("True","U")
    torso(1)
    arms("W")
    torso(1)
    legs(4, "<>-<>")
def main():
    '''
    This function is the code for the main program
    it asks for input of: direction, eyes, hair, arm_symbol,
    body_length, leg_length, shoe_look, and passes them into
    functions combined to print an avatar.
    '''
    print ("----- AVATAR -----")
    avatar_selection = start_up_prompt()
    if avatar_selection == "custom":
        direction = input ("Hat style ? \n")
        eyes = input ("Character for eyes ?\n")
        hair = input ("Shaggy hair (True/False) ?\n")
        arm_symbol = input ("Arm style ?\n")
        body_length = int (input ("Torso length ?\n"))
        leg_length = int (input ("Leg length (1-4) ?\n"))
        shoe_look = input ("Shoe look ?\n")
        hat(direction)
        face(hair,eyes)
        arms(arm_symbol)
        torso(body_length)
        legs(leg_length, shoe_look)
    elif avatar_selection == "Jeff":
        avatar_jeff()
    elif avatar_selection == "Adam":
        avatar_adam()
    elif avatar_selection == "Chris":
        avatar_chris()
main()