import os

source = "main.txt"

dest ="newfile.txt"

os.rename(source,dest)
print("source path has been renamed to dest path")