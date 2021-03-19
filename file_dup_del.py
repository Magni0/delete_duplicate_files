"""
this script finds and deletes duplicate files in a set of dir paths
"""

from os import listdir, remove, getcwd
import sys

comparison_list = []
dir_list = []
init_path = []
pop_list = []

# gets initial path
try: # if inline argument
    init_path.append(sys.argv[1])
except: # current dir
    init_path.append(getcwd())

def file_check(file):
    pass

def cycle(path: list, initial=False):
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
                dir_list.append(f"{path[0]}\{file}")

    else:
        for directory in path:
            # print(directory)
            files = listdir(directory)
            # dir_list.remove(directory)

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
                    dir_list.append(f"{directory}\{file}")
                    # print(f"{directory}\{file}")
                # pop_list.append(dir_list.pop(dir_list.index(directory)))


cycle(init_path, initial=True)

# for i in dir_list:
#     print(i)

cycle(dir_list)

# print("\n")
# for i in dir_list:
#     print(i)

# print("\n")
# for i in pop_list:
#     print(i)