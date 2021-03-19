"""
this script finds and deletes duplicate files in a set of dir paths
"""

from os import listdir, remove
# from sys import argv

comparison_list = []
dir_list = []

try: # if inline argument
    with open("paths.txt", "r") as file:
        paths = file.readlines()
except: # current dir
    pass

for path in paths:
    
    try:
        files = listdir(path)
    except:
        print(f"error: {path} does not exist")
        continue

    for file in files:
        
        if "." in file: # if file
            if file not in comparison_list:
                comparison_list.append(file)
            
            elif file in comparison_list:
                print(f"{file} is a duplicate")
            
            elif "(" in file:
                print(f"{file} is a duplicate")
            # print(f"{file} is a file")
        else: # if dir
            dir_list.append(f"{path}\{file}")
            # print(f"{file} is a dir")
