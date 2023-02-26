import os
from random import randint

Directory = os.getcwd() + "\Archivos"
os.chdir(Directory)
Conetnido = os.listdir()

def random_number(minimum, maximum):
    return randint(minimum,maximum)

def read_file(name):
    with open(name, 'r') as file:
        contents = file.read()
    return contents

def create_file(character, name):
    with open("Copy_"+name, "a") as file:
        file.write(character)

def identify(Contents):
    files = []
    folder = []
    for count in Contents:
        if ".txt" in count:
            files.append(count)
        else:
            folder.append(count)
    return files, folder

def files_copy(files):
    for count_file in range(len(files)):
        file_name = files[count_file]
        text = read_file(file_name)
        for count_char in range(len(text)):
            letter = text[count_char]
            if (ord(text[count_char]) >= 48 and ord(text[count_char]) <= 57):
                letter = chr(random_number(65, 90))
            elif ((ord(text[count_char]) >= 65 and ord(text[count_char]) <= 90) or (ord(text[count_char]) >= 97 and ord(text[count_char]) <= 122)):
                letter = chr(random_number(48, 57))
            create_file(letter, file_name)


txt, carp = identify(Conetnido)
files_copy(txt)
print("Listo jalisco")

            


