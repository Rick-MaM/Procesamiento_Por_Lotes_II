import os
from random import randint

Directory = os.getcwd() + "\Archivos"

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

#----------------CARPETAS------------------
def new_folder(directory):
    list = directory.split("\\")
    list.pop()
    list = "\\".join(list)
    os.chdir(list)
    os.mkdir("Archivos_Copiados")
    return list + "\Archivos_Copiados"



def folder_contents(directory):
    os.chdir(directory)
    contests = os.listdir()
    file, folder = identify(contests)

    copy_folder = new_folder(directory)
    
    

    while len(file) != 0:
        os.chdir(directory)
        text = files_copy(file[0])
        os.chdir(copy_folder)
        create_file(text,file[0])
        file.pop(0)
    

def create_folder_directory(name):
    new_name = "Copia_"+name
    os.mkdir(new_name)
    return os.getcwd() + "/" + name, os.getcwd() + "/" + new_name


def folder_copy(folder):
    for count_folder in range(len(folder)):
        origin,copy = create_folder_directory(folder[count_folder])
        

folder_contents(Directory)

            


