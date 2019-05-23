import os
import shutil


def create_folders(f):    
    for i in range(1,4):
        os.mkdir(f + str(i))

if os.path.isdir(r"D:\python_excercise"):
    shutil.rmtree(r"D:\python_excercise")

os.mkdir(r"D:\python_excercise")

L = ["x", "y", "z", "a", "b", "c" ]

for i in range(1, 7):
    os.mkdir( r"D:\python_excercise\t" + str(i))
    create_folders(r"D:\python_excercise\t" + str(i) + r"\\" + L[i-1])