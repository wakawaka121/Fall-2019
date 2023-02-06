####
#### Author: Derek Tominaga
#### Description: This program will compare a user input
#### a non-english word and convert it to english by refrencing
#### a dictionary.
####
def get_word_conversions(words_file_name):
    '''
    This function takes a single parameter to
    generate and retrun a dictionary from a file
    words_file_name = name of a file
    '''
    word_dictionary = {}
    word_refrence = open(words_file_name , "r")
    for lines in word_refrence:
        word_list = lines.strip("\n").split(",")
        i = 1
        while i < len(word_list):
            word_dictionary[word_list[i]] = word_list[0]
            i += 1
    return word_dictionary
def print_conversion(word, conversions):
    '''
    This function takes two parameters to check the dictioary
    and for the word and give its "conversions"
    word = user input "forigen" word that needs translation
    conversions = dictionary of non-English words
    '''
    if word not in conversions:
        print("\n" + "Not sure.")
    else:
        print("\n" + "English version is: " + conversions[word])
def main():
    file_name = input('Enter name of words file:\n')
    conversions = get_word_conversions(file_name)

    word = input('Enter word to convert to English:\n')
    print_conversion(word, conversions)

main()