####
#### Author: Derek Tominaga
#### Description: This program will decrypt a file using
#### a provided decoder file. The encrypted file and decoder file
#### are realated through indexes
###
import random
def decrypted_file(file_lines, key_index):
    """
    This function takes two parameters to decode and write to file
    file_lines = a list of the scrambled file lines
    key_index = a list of int "indexes" reflecting how lines were scrambled
    loop through the values in the list and write based on index in the list.
    """
    decoded_file = open("decrypted.txt", "w")
    for i in range(1, len(key_index)+1):
        decoded_file.write(file_lines[key_index.index(i)])
    decoded_file.close()
def main():
    random.seed(125)
    file_name = input("Enter the name of an encrypted text file:\n")
    file_key = input("Enter the name of the encryption index file:\n")
    file_data = open(file_name, "r")
    file_lines = file_data.readlines()
    key_data = open(file_key, "r")
    key_index = key_data.readlines()
    for i in range(0, len(key_index)):
        key_index[i] = int(key_index[i].strip("\n"))
    decrypted_file(file_lines, key_index)
    file_data.close()
    key_data.close()
main()