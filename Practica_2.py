import os
from random import randint
from tkinter import *
from tkinter import filedialog

list_origin_directory = []
list_copy_directory = []

def random_number(minimum, maximum):
    return randint(minimum,maximum)

def read_file(name):
    with open(name, 'r') as file:
        contents = file.read()
    return contents

def create_file(character, name):
    with open(name, "a") as file:
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

def new_folder_origin(directory):
    before = directory.split("\\")
    new_folder = "Copy_" + before[len(before)-1]
    before.pop()
    before = "\\".join(before)
    os.chdir(before)
    os.mkdir(new_folder)
    return before +"\\"+ new_folder

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
    if len(folder) != 0:
        create_copy_folder(origin_directory,copy_directory,folder)

def create_copy_folder(original_directory, copy_director, name):
    global list_origin_directory, list_copy_directory
    for count_folder in range(len(name)):
        os.mkdir(name[count_folder])
        list_origin_directory.append(original_directory+"\\"+name[count_folder])
        list_copy_directory.append(copy_director+f"\{name[count_folder]}")


def batch_processing(origin_directory):
    global list_origin_directory, list_copy_directory
    copy_folder = new_folder_origin(origin_directory)
    print(copy_folder)
    folder_contents(origin_directory, copy_folder)

    while len(list_copy_directory) != 0:
        folder_contents(list_origin_directory[0],list_copy_directory[0])
        list_origin_directory.pop(0)
        list_copy_directory.pop(0)

root = Tk()
root.title("Buscador")
root.geometry("450x150")

def search():
    filename = filedialog.askdirectory(title="Abrir carpeta") 
    lblDirectory = Label(text=filename).place(x=20,y=50)
    filename = filename.split("/")
    batch_processing("\\".join(filename))

btnSearch = Button(root, text="...", command=search,width=20).place(x=20,y=10)

root.mainloop()
