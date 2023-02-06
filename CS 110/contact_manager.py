def open_file_make_set():
    """
    This function takes no parameters to
    opens a file and adds tuples to a set
    """
    contact_file = open("contacts.txt", "r")
    contact_set = set()
    #iterates through the info from the file line by line
    for lines in contact_file:
        temp_list = []
        line_info = lines.strip("\n").split(" | ")
        for i in range(len(line_info)):
            #appends email and phone number through iterations
            temp_list.append(line_info[i])
        #tuples added to contact set
        contact_set.add(tuple(temp_list))
    contact_file.close()
    return (contact_set)
def get_contact_info(command, contact_set):
    """
    This function takes two parameters to search the
    set for the user input based on "search for contacts with"
    command.
    command = string user input
    contact_set = set of tuples, that have contact info
    """
    matches = set()
    input_list = command.split()
    info_1 = input_list[3]
    info_2 = " "
    if info_1 == "name":
            name = input_list[4:]
            info_2 = info_2.join(name)
    else:
        info_2 = input_list[-1]
    for item in contact_set:
        if info_2 in item:
            matches.add(item)
    if len(matches) == 0:
        print("None")
    else:
        # prints contact details
        for contact in sorted(matches):
            print(contact[0]+ "'s", "contact info:" )
            print ("  email: " + contact[1])
            print ("  phone: " + contact[2])
def add_contact(contact_set):
    """
    This function takes one parameter and will prompt a user
    to input name, email, and phone number
    contact_set = set of tuples, that has contact info
    """
    # new contact list to add to contact_set
    new_contact = []
    name = input("name: \n")
    new_contact.append(name)
    email = input("email: \n")
    new_contact.append(email)
    phone = input("phone: \n")
    new_contact.append(phone)
    # check if tuple in contact set
    if tuple(new_contact) in contact_set:
        print("Contact already exists!")
    else:
        # adds new_contact tuple to contact_set
        contact_set.add(tuple(new_contact))
        print("Contact added!")
    # returns sorted contact_set after adding
    return sorted(contact_set)
def save_file(contact_set):
    """
    This function takes one parameter to write to
    a file and close the file.
    contact_set = set of tuples, with contact info
    """
    contact_file = open("contacts.txt", "w")
    for items in sorted(contact_set):
        contact_string = ""
        for i in range(len(items)):
            contact_string += items[i]
            # to get the format that is expected in a file add " | "
            # on first two items in the tuple
            if i <= 1:
                contact_string += " | "
        contact_file.write(contact_string + "\n")
    contact_file.close()
def main():
    contact_set = open_file_make_set()
    print("Welcome to the contacts app!")
    command = input(">\n")
    while command != "exit":
        if command == "add contact":
            add_contact(contact_set)
            command = input(">\n")
        # if string entered starts with show contacts with
        elif command[:18] == "show contacts with":
            get_contact_info(command, contact_set)
            command = input(">\n")
        else:
            print("Huh?")
            command = input(">\n")
    save_file(contact_set)
    print("Goodbye!")

main()