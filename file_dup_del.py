"""
this script finds and deletes duplicate files in a set of dir paths
"""

from os import listdir, remove, getcwd
import sys

comparison_list = []
dir_list = []

# gets initial path
try: # if inline argument
    path = sys.argv[1]
except: # current dir
    path = getcwd()

def cycle(path, initial=False):
    if initial == True:
        try:
            files = listdir(path)
        except:
            print(f"error: {path} does not exist")
            sys.exit()

        for file in files:
            if "." in file: # if file
                if file not in comparison_list:
                    comparison_list.append(file)
    
                elif file in comparison_list:
                    print(f"{file} at {path} is a duplicate") # temp
                
                elif "(" in file:
                    print(f"{file} at {path} is a duplicate") # temp
            else: # if dir
                dir_list.append(f"{path}\{file}")

    else:
        pass

cycle(path, initial=True)

# while dir_list:
#     cycle(dir_list)









# if initial == False:
#     for i in dir_list:
#         print(i)
#     dir_list.remove(file)
#     path = file
#     # file = listdir(path)
#     # print(path)
#     # for i in file:
#     #     print(f"    {i}")

# if "." in file: # if file
#     if file not in comparison_list:
#         comparison_list.append(file)
    
#     elif file in comparison_list:
#         print(f"{file} at {path} is a duplicate")
    
#     elif "(" in file:
#         print(f"{file} at {path} is a duplicate")
# else: # if dir
#     if initial == True:
#         dir_list.append(f"{path}\{file}")
#     else:
#         dir_list.append(f"{file}")