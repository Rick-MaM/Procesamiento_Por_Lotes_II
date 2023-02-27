import os
from random import randint


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

def files_copy(file):
    text = read_file(file)
    letter = ""
    for count_char in range(len(text)):
        
        if (ord(text[count_char]) >= 48 and ord(text[count_char]) <= 57):
            letter = letter + chr(random_number(65, 90))
        elif ((ord(text[count_char]) >= 65 and ord(text[count_char]) <= 90) or (ord(text[count_char]) >= 97 and ord(text[count_char]) <= 122)):
            letter = letter + chr(random_number(48, 57))
        else:
            letter = letter + text[count_char]
    return letter

# ----------------CARPETAS------------------

def new_folder(directory):
    list = directory.split("\\")
    list.pop()
    list = "\\".join(list)
    os.chdir(list)
    os.mkdir("Archivos_Copiados")
    return list + "\Archivos_Copiados"


def folder_contents(origin_directory,copy_directory):
    os.chdir(origin_directory)
    contests = os.listdir()
    file, folder = identify(contests)

    while len(file) != 0:
        os.chdir(origin_directory)
        text = files_copy(file[0])
        os.chdir(copy_directory)
        create_file(text, file[0])
        file.pop(0)
 
    list_origin_directory, list_copy_directory = create_copy_folder(origin_directory,copy_directory,folder)

def create_copy_folder(original_directory, copy_director, name):
    list_origin_directory = []
    list_copy_directory = []
    for count_folder in range(len(name)):
        new_name_folder = "Copy_" + name[count_folder]
        os.mkdir(new_name_folder)
        list_origin_directory.append(original_directory+"\\"+name[count_folder])
        list_copy_directory.append(copy_director+"\\"+new_name_folder)
    return list_origin_directory, list_copy_directory


def main():
    origin_directory = os.getcwd() + "\Archivos"
    copy_folder = new_folder(origin_directory)
    folder_contents(origin_directory, copy_folder)


main()

            


