"""
This script finds and deletes duplicate files in a set of dir paths
"""

from os import listdir, remove, getcwd, path
import sys

class ScanDirectory:

    """
    Scans files and directorys then deletes files with the same name.
    This is done from root dir (given as argument or current working directory)
    to all subsequent directorys.
    """

    def __init__(self):
        self.comparison_list = [] # array to check file names against 
        self.dir_list_1 = []
        self.dir_list_2 = []

    def initial_cycle(self):

        """Does the first scan in the root directory"""

        absolute = False

        # gets initial path
        try: # if inline argument
            init_path = sys.argv[1]
        except: # current dir
            init_path = getcwd()

        try:
            if init_path[0] == "/": # if arg is absolute path
                absolute = True
                files = listdir(init_path)
            else: # if arg is relative path
                absolute_initial_path = path.abspath(init_path)
                files = listdir(absolute_initial_path)
        except:
            print(f"error: {init_path} does not exist")
            sys.exit()

        for file in files:
            if "." in file: # if file
                if file not in self.comparison_list:
                    self.comparison_list.append(file)
    
                elif file in self.comparison_list:
                    print(f"{file} at {init_path} is a duplicate") # temp
                
                elif "(" in file:
                    print(f"{file} at {init_path} is a duplicate") # temp
            
            else: # if dir
                if absolute == True: # if path was and absolute path
                    self.dir_list_1.append(f"{init_path}/{file}") # appends directory path to dir_list_1
                else: # if path was relitive
                    self.dir_list_1.append(f"{absolute_initial_path}/{file}") # appends directory path to dir_list_1

scan = ScanDirectory()

scan.initial_cycle()

for i in scan.dir_list_1:
    print(i)

#     for directory in path:
        
#         files = listdir(directory)

#         for file in files:
#             # if "." in file: # if file
#             #     if file not in comparison_list:
#             #         comparison_list.append(file)
    
#             #     elif file in comparison_list:
#             #         pass
#             #         # print(f"{file} at {directory} is a duplicate") # temp
                
#             #     elif "(" in file:
#             #         pass
#             #         # print(f"{file} at {directory} is a duplicate") # temp
#             # else: # if dir
#             if array_2 == True:
#                 # print(f"array_2 is {array_2}")
#                 dir_list_2.append(f"{directory}/{file}")
#             else:
#                 # print(f"array_2 is {array_2}")
#                 dir_list.append(f"{directory}/{file}")
        
#     array_2 = not array_2
    
#     if array_2 == True:
#         dir_list_2.clear()
#     else:
#         dir_list.clear()


# cycle(init_path, initial=True)

# dir_list_switch = True

# while len(dir_list) and len(dir_list_2) > 0:

#     if dir_list_switch == True:
#         cycle(dir_list)
#     else:
#         cycle(dir_list_2, array_switch=False)

#     print("\ndir_list")
#     for i in dir_list:
#         print(i)

#     print("\ndir_list_2")
#     for i in dir_list_2:
#         print(i)

#     dir_list_switch = not dir_list_switch
