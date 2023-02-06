###
### Author: Derek Tominaga
### Description: This programs takes two files
### parses the info into a dictinary with keys of misspelled words
### mapped to correct spelling. There are two modes replace and suggest
### based on user input one of two modes will be run.
###
def replace_mode(line_list, missed_word):
    """
    This function take two parameters to rewrite the file with
    correct spelling
    line_list = dictionary with keys = lines and values = words in a line
    missed_word = a dictionary that contains misspelled words mapped to correct spelling
    """
    for key in line_list:
        check_list = line_list[key]
        index = 0
        capitaliz_indicatior = 0
        while index < len(check_list):
            check_list[index], character = punctuation(check_list[index])
            check_list[index], indicator = capitalization(check_list[index])
            if check_list[index] in missed_word:
                check_list[index] = missed_word[str(check_list[index])]
            if indicator > 0:
                check_list[index] = check_list[index].capitalize() + character
            else:
                check_list[index] = check_list[index] + character
            index += 1
    return line_list
def suggest_mode(line_list, missed_word):
    """
    This function takes two parameters to make suggest of words to correct
    line_list = dictionary with keys = lines , values = words in a line
    missed_word = dictionary of misspelled words and keyed to correct words
    """
    legend = []
    value_of_misspelled = 1
    for key in line_list:
        check_list = line_list[key]
        character = ""
        for index in range(len(check_list)):
            check_list[index], character = punctuation(check_list[index])
            check_list[index], indicator = capitalization(check_list[index])
            if check_list[index] not in missed_word:
                check_list[index] = check_list[index] + character
            if check_list[index] in missed_word and indicator > 0:
                legend.append(missed_word[str(check_list[index])].capitalize())
                check_list[index] = check_list[index] + character + " (" + str(value_of_misspelled) + ")"
                value_of_misspelled += 1
            if check_list[index] in missed_word:
                legend.append(missed_word[str(check_list[index])])
                check_list[index] = check_list[index] + character + " (" + str(value_of_misspelled) + ")"
                value_of_misspelled += 1
            if indicator > 0:
                check_list[index] = check_list[index].capitalize()
    return legend
def open_text(check_file):
    """
    This function takes one parameter to open a file and assign to a dictionary
    check_file = the input file that needs to be checked for missspelled words
    """
    file_data = open(check_file, "r")
    line_list = {}
    for lines in file_data:
        word_in_line = lines.strip("\n").split(" ")
        line_list[lines] = word_in_line
    file_data.close()
    return line_list
def build_dictionary(word_bank):
    """
    This fucnton takes one parameters to build a dictionary
    word_bank = file containing a word with common mispelling
    """
    missed_word = {}
    line_list = []
    for lines in word_bank:
        line_list = lines.strip("\n").split(":")
        temp_split = line_list[1].split(",")
        i = 0
        while i < len(temp_split):
            missed_word[temp_split[i]] = line_list[0]
            i += 1
    return missed_word
def punctuation(word):
    """
    This fucntion take ones parameter to removed punctuaton and then check the spelling
    word = is a string passed w/punctuation if present
    """
    symbol = ""

    if len(word) != 0 and word[len(word)-1] == ",":
        symbol = ","
        word = word[0:int(len(word)-1)]
    if len(word) != 0 and word[len(word)-1] == ".":
        symbol = "."
        word = word[0:int(len(word)-1)]
    if len(word) != 0 and word[len(word)-1] == "?":
        symbol = "?"
        word = word[0:int(len(word)-1)]
    if len(word) != 0 and word[len(word)-1] == "!":
        symbol = "!"
        word = word[0:int(len(word)-1)]
    return word, symbol
def capitalization(word):
    """
    This funciton takes one parameter to change a word to lowercase inorder to check dicitonary
    word = a string passsed to check if the word is capitalized
    """
    letter_change = 0
    if len(word) != 0 and word[0].isupper():
        word = word.lower()
        letter_change = 1
    return word, letter_change
def print_replace(line_list):
    """
    This function takes one parametsr to print in repalce mode
    line_list = dictionary, keys = lines and values are words of a sentence
    """
    print ("\n--- OUTPUT ---")
    for key in line_list:
        sentence_list = line_list[key]
        sentence = ""
        i = 0
        while i < len(sentence_list):
            sentence += sentence_list[i] + " "
            i += 1
        print(sentence)
def print_suggest(line_list, legend):
    """
    This function takes two parameters to print in suggest mode
    line_list = a dictionary, keys = lines and values are words of a sentence
    legend = the list of correct words that
    """
    print ("\n--- OUTPUT ---")
    for key in line_list:
        sentence_list = line_list[key]
        sentence = ""
        i = 0
        while i < len(sentence_list):
            sentence += sentence_list[i] + " "
            i += 1
        print(sentence)
    print ("\n--- LEGEND ---")
    legend_index = 0
    while legend_index < len(legend):
        print("(" + str(legend_index + 1) + ") " + legend[legend_index])
        legend_index += 1
def main():
    word_bank = open("misspellings.txt", "r")
    missed_word = build_dictionary(word_bank)
    check_file = input("Enter input file:\n")
    check_mode = input("Enter spellcheck mode (replace or suggest):\n")
    line_list = open_text(check_file)
    if check_mode == "replace":
        replace_mode(line_list, missed_word)
        print_replace(line_list)
    elif check_mode == "suggest":
        legend = suggest_mode(line_list, missed_word)
        print_suggest(line_list, legend)
    word_bank.close()
main()