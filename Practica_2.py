import os
from random import randint

Directory = os.getcwd() + "\Archivos"
os.chdir(Directory)
Conetnido = os.listdir()

def random_number(minimum, maximum):
    return randint(minimum,maximum)

def identify(Contents):
    files = []
    folder = []
    for count in Contents:
        if ".txt" in count:
            files.append(count)
        else:
            folder.append(count)
    return files, folder


