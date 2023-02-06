###
### Author: Derek Tominaga
### Description: This program reads a file and generations a dictionary
### of unique words and the number of times the unique words occures.
### after catagorizing into small medium and large we determine which unique
### word for each catatory occured the most. We display the results in text and
### graphical format through graphics object.
###

from graphics import graphics
def process_file(file_name):
    """
    This fucntion takes one parameter to build list of words in a file
    file_name = "variable" string opened and read
    returns the list of words
    """
    words_in_file = []
    set_of_words = set()
    word_bank = open(file_name, "r")
    for lines in word_bank:
        words_in_line = lines.strip("\n").split()
        for i in range(len(words_in_line)):
           words_in_file.append(words_in_line[i])
           set_of_words.add(words_in_line[i])
    word_bank.close()
    return words_in_file , set_of_words
def word_count(words_in_file):
    """
    This function takes one parameter and generates a dictionary.
    words_in_file = list of words from the file
    dictionary kyes = words, values = occurences
    """
    count_dictionary = {}
    for i in range(len(words_in_file)):
        if words_in_file[i] not in count_dictionary:
            count_dictionary[words_in_file[i]] = 1
        else:
            count_dictionary[words_in_file[i]] += 1
    return count_dictionary
def word_size_list(set_of_words):
    """
    This function takes one parameter to generate and retrun
    3 lists, small words (0-4), medium words(5-7), and large words(>8)
    set_of_words = set of unique words generated from file
    """
    small_list = []
    medium_list = []
    large_list = []
    for i in set_of_words:
        if len(i) >= 8:
            large_list.append(i)
        elif len(i) <= 4:
            small_list.append(i)
        else:
            medium_list.append(i)
    return small_list, medium_list, large_list
def most_occurance(small_list, medium_list, large_list, count_dictionary):
    """
    This function takes 4 parameters to determine the small medium and large words
    that occur the most and returns them
    small_list = list of words up to 4 characters
    medium_list = list of words contaiing 5-7 characters
    large_list = list of words containing 8 or more characters
    count_dictionary = dictionary with words as keys and values
    are number of occurences
    """
    small_word = small_list[0]
    medium_word = medium_list[0]
    large_word = large_list[0]
    for i in range(len(small_list)):
        if int(count_dictionary[small_word]) < int(count_dictionary[small_list[i]]):
            small_word = small_list[i]
    for i in range(len(medium_list)):
        if int(count_dictionary[medium_word]) < int(count_dictionary[medium_list[i]]):
            medium_word = medium_list[i]
    for i in range(len(large_list)):
        if int(count_dictionary[large_word]) < int(count_dictionary[large_list[i]]):
            large_word = large_list[i]
    return small_word, medium_word, large_word
def number_capitalized_punctuated(count_dictionary):
    """
    This function takes one paraemeter to determine if the word
    is capitalized or has punctuation
    count_dictionary = a dictionary where the keys become the
    unique word list
    """
    unique_list = []
    cap_count = 0
    punct_count = 0
    for keys in count_dictionary:
        unique_list.append(keys)
    for i in range(0,len(unique_list)):
        if unique_list[i][0].isupper():
            cap_count += 1
        if unique_list[i][-1] == ",":
            punct_count += 1
        elif unique_list[i][-1] == ".":
           punct_count += 1
        elif unique_list[i][-1] == "?":
           punct_count += 1
        elif unique_list[i][-1] == "!":
           punct_count += 1
    return cap_count, punct_count
def print_text(gui, file_name, unique_words, small_times,
    medium_times, large_times,):
    """
    This fucntion takes 6 parameters to print text
    gui = graphics oject used to draw
    file_name = name of the file that was read
    unique_words = list of unique words from the file
    (small/medium/large)_times = are int values of occurences
    """
    gui.text(35, 35, file_name, "turquoise1", 20)
    gui.text(35, 70, "Total Unique Words: "+ str(unique_words) , "white", 20)
    gui.text(35, 120, "Most used words(s/mn/l):", "white", 18)
    gui.text(250, 120, small_times + medium_times + large_times, "turquoise1", 18)
    gui.text(35, 160, "Word lengths", "white", 25)
    gui.text(250, 160, "Cap/Non-Cap", "white", 25)
    gui.text(450, 160, "Punct/Non-Punct", "white", 25)
def draw_canvas_word_chart(unique_words, small_offset, medium_offset,
    large_offset):
    """
    This function takes 4 parameters to draw the canvas and barchart
    unique_words = list of "unique" words from the file
    small_offset = int value indicating pixels of small words
    medium_offset = in value indicating pixels of medium words
    large_offset = int value indicating pixels of large words
    """
    gui = graphics(650, 700, "infographic")
    gui.rectangle(0, 0, 650, 700, "darkgrey")
    y_cord = 200
    gui.rectangle(35, y_cord, 150, small_offset, "DeepSkyBlue4")
    y_cord += small_offset
    gui.rectangle(35, y_cord, 150, medium_offset, "dark green")
    y_cord += medium_offset
    gui.rectangle(35, y_cord, 150, large_offset, "DeepSkyBlue4")
    y_cord = 200
    gui.text(38, y_cord, "small words", "white", 10)
    y_cord += (small_offset + 5)
    gui.text(38,y_cord, "medium words", "white", 10)
    y_cord += medium_offset +5
    gui.text(38, y_cord, "large words", "white", 10)
    return gui
def draw_cap_chart(gui, unique_words, cap_count):
    """
    This function takes 3 parameters to draw and label
    the capitalized chart.
    gui = grapics object to used to draw
    unique_words = list of unique words
    cap_count = int value of number of capitalized words
    """
    y_cord = 200
    gui.rectangle(250, y_cord, 150, (450/unique_words) * cap_count, "DeepSkyBlue4")
    y_cord += (450/unique_words) * cap_count
    gui.rectangle(250, y_cord, 150, (450/unique_words) * (unique_words - cap_count), "darkgreen")
    if cap_count != 0:
        gui.text(255, 200, "Capitalized", "white", 10)
    if (unique_words - cap_count) != 0:
        gui.text(255, 205 + (450/unique_words) * cap_count, "Non Capitalized", "white", 10)
def draw_punct_chart(gui, unique_words, punct_count):
    """
    This function takes 3 parameters to draw the
    punctuated words chart
    gui = graphics object used to draw
    unique_words = list of unique words
    punct_count = int value of punctuated words
    """
    y_cord = 200
    gui.rectangle(450, y_cord, 150, (450/unique_words) * punct_count, "DeepSkyBlue4")
    y_cord += (450/unique_words) * punct_count
    gui.rectangle(450, y_cord, 150, (450/unique_words) * (unique_words - punct_count), "dark green")
    if punct_count != 0:
        gui.text(455, 200, "Punctuated", "white", 10)
    if (unique_words - punct_count) != 0:
        gui.text(455, 205 + (450/unique_words) * punct_count, "Non Punctuated", "white", 10)
def main():
    file_name = input("Enter name of file:\n")
    words_in_file, set_of_words = process_file(file_name)
    count_dictionary = word_count(words_in_file)
    list_small, list_medium, list_large = word_size_list(set_of_words)
    small_word, medium_word, large_word = most_occurance(list_small, list_medium,
    list_large, count_dictionary)
    cap_count, punct_count = number_capitalized_punctuated(count_dictionary)
    unique_words = int(len(set_of_words))
    small_offset = (450/unique_words) * int(len(list_small))
    medium_offset = (450/unique_words) * int(len(list_medium))
    large_offset= (450/unique_words) * int(len(list_large))
    gui = draw_canvas_word_chart(unique_words, small_offset, medium_offset,
    large_offset)
    draw_cap_chart(gui, unique_words, cap_count)
    draw_punct_chart(gui, unique_words, punct_count)
    small_times = small_word + " (" + str(count_dictionary[small_word]) + "x) "
    medium_times = medium_word + " (" + str(count_dictionary[medium_word]) + "x) "
    large_times = large_word + " (" + str(count_dictionary[large_word]) + "x) "
    print_text(gui, file_name, unique_words, small_times, medium_times, large_times)
main()