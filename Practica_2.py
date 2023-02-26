import os

Directory = os.getcwd() + "\Archivos"
os.chdir(Directory)
Conetnido = os.listdir()


def identify(Contents):
    files = []
    folder = []
    for count in Contents:
        if ".txt" in count:
            files.append(count)
        else:
            folder.append(count)
    return files, folder


Arch, Carp = identify(Conetnido)
print(Arch)
print(Carp)
