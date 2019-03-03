from sys import argv
from os.path import exists
script, fileToBeCopied, fileToCopyIn = argv
existence = exists(fileToCopyIn)

def copyFun ():
    inPutDataFile = open(fileToBeCopied).read()
    outPutDataFile = open(fileToCopyIn, 'w').write(inPutDataFile)

if existence == False:
    copyFun ()
else:
    print("This file already exists!!\nPress e to exit or c to continue:\n")
    entry = input("> ")
    if entry == 'c':
        copyFun ()


