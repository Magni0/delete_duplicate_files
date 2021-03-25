"""
this script finds and deletes duplicate files in a set of dir paths
"""

from os import listdir, remove, getcwd
import sys

comparison_list = []
init_path = []
dir_list = []
dir_list_2 = []

# gets initial path
try: # if inline argument
    init_path.append(sys.argv[1])
except: # current dir
    init_path.append(getcwd())

def file_check(file):
    pass

def cycle(path: list, initial=False, array_switch=True):

    array_2 = array_switch

    if initial == True:
        try:
            files = listdir(path[0])
        except:
            print(f"error: {path} does not exist")
            sys.exit()

        for file in files:
            if "." in file: # if file
                if file not in comparison_list:
                    comparison_list.append(file)
    
                elif file in comparison_list:
                    print(f"{file} at {path[0]} is a duplicate") # temp
                
                elif "(" in file:
                    print(f"{file} at {path[0]} is a duplicate") # temp
            else: # if dir
                dir_list.append(f"{path[0]}/{file}")

    else:
        for directory in path:
            
            files = listdir(directory)

            for file in files:
                if "." in file: # if file
                    if file not in comparison_list:
                        comparison_list.append(file)
        
                    elif file in comparison_list:
                        pass
                        # print(f"{file} at {directory} is a duplicate") # temp
                    
                    elif "(" in file:
                        pass
                        # print(f"{file} at {directory} is a duplicate") # temp
                else: # if dir
                    if array_2 == True:
                        # print(f"array_2 is {array_2}")
                        dir_list_2.append(f"{directory}/{file}")
                    else:
                        # print(f"array_2 is {array_2}")
                        dir_list.append(f"{directory}/{file}")
            
        array_2 = not array_2
        
        if array_2 == True:
            dir_list_2.clear()
        else:
            dir_list.clear()


cycle(init_path, initial=True)

dir_list_switch = True

while len(dir_list) and len(dir_list_2) > 0:

    if dir_list_switch == True:
        cycle(dir_list)
    else:
        cycle(dir_list_2, array_switch=False)

    print("\ndir_list")
    for i in dir_list:
        print(i)

    print("\ndir_list_2")
    for i in dir_list_2:
        print(i)

    dir_list_switch = not dir_list_switch
