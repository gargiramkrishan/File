import os
import shutil

source = "C:/source"
des = "C:/dest"

listOfFile = os.listdir(source)

for file in listOfFile:
    root,exe = os.path.splitext(file)
    print(root,exe)