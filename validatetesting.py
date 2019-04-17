# Write a python script that will do the following. Rename all files in this folder to abide by a naming convention of data_
## where ## is an arbitrary number used to define orderering.
#You can use the following methods from the os module.
# `os.getcwd()`
# this will return the path to the current directory python is being executed in
# `os.listdir()`
# returns a list of files in the current directory
# `os.rename(src,dst)`
# where src is the source path and dst path of the src and paths are inclusive of filenames

# Python code to rename multiple files in a directory or folder

# import os
import os

i = 0


#Function to reanme multiple files
def main():

    for filename in os.listdir("file"):
        dst = "g" + str(i) + ".jpg"
        src = 'file'+ filename
        dst = 'file'+ dst

        list = os.listdir('src')
# rename() function will rename all the files
        os.rename(src, dst)
        i += 1
#calls main for the file 
if __name__ == 'main':
    main()