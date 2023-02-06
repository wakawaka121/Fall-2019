####
#### Author: Derek Tominaga
#### Description: This program gets/opens a file
#### reads the data in the file and jumbles it up.
#### The writes an encrypted file and a key to decrypt
####

import random
def scramble(scramble_data, encrypt_key):
    """
    This function takesa two parameters to encrypt a file
    scramble_data = is the data read from a file
    that get scrambled_file
    encrypt_key = is the list of indexs that gets
    scrambled with relation to the scrambled file
    """
    for i in range (0,5):
        for i in range(len(scramble_data)):
            mix1 = random.randint(0, len(scramble_data)-1)
            mix2 = random.randint(0, len(scramble_data)-1)
            scramble_data[mix1],scramble_data[mix2] = scramble_data[mix2],scramble_data[mix1]
            encrypt_key[mix1],encrypt_key[mix2] = encrypt_key[mix2],encrypt_key[mix1]
    return scramble_data, encrypt_key
def write_file(scrambled_file, encryption_key):
    """
    This funtion takes two parameters to write to a file
    scrambled_file = the list of info to write to encrypted.txt
    encryption_key = the list opf info to write to index.txt
    """
    encrypted_file = open("encrypted.txt", "w")
    index_key = open("index.txt", "w")
    for i in range(0, len(scrambled_file)):
        encrypted_file.write(str(scrambled_file[i]))
        index_key.write(str(encryption_key[i])+ "\n")
    encrypted_file.close()
    index_key.close()
def main():
    random.seed(125)
    file_name = input("Enter a name of a text file to encrypt:\n")
    opened_file = open(file_name, "r")
    read_file_data = opened_file.readlines()
    encryption_index = []
    for lines in range(len(read_file_data)):
        encryption_index.append(lines+1)
    scrambled_file, encryption_key = scramble(read_file_data, encryption_index)
    write_file(scrambled_file,encryption_key)
    opened_file.close()
main()