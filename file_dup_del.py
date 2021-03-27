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
            if absolute == True:
                raise Exception(f"{init_path} does not exist")
            
            else:
                raise Exception(f"{absolute_initial_path} does not exist")
            
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

    def subsequent_cycle(self):

        switch = True

        while self.dir_list_1 or self.dir_list_2: # until both lists are empty
            if switch == True:
                for dir_path in self.dir_list_1:

                    files = listdir(dir_path)

                    for file in files:
                        if "." in file: # if file
                            if file not in self.comparison_list:
                                self.comparison_list.append(file)

                            elif file in self.comparison_list:
                                print(f"{file} at {dir_path} is a duplicate") # temp

                            elif "(" in file:
                                print(f"{file} at {dir_path} is a duplicate") # temp
                        
                        else:
                            self.dir_list_2.append(f"{dir_path}/{file}") # appends directory path to dir_list_2

                # print(f"dir_list_2: {self.dir_list_2}\n")
                switch = False
                self.dir_list_1.clear()

            elif switch == False:
                for dir_path in self.dir_list_2:

                    files = listdir(dir_path)

                    for file in files:
                        if "." in file: # if file
                            if file not in self.comparison_list:
                                self.comparison_list.append(file)

                            elif file in self.comparison_list:
                                print(f"{file} at {dir_path} is a duplicate") # temp

                            elif "(" in file:
                                print(f"{file} at {dir_path} is a duplicate") # temp

                        else:
                            self.dir_list_1.append(f"{dir_path}/{file}") # appends directory path to dir_list_1

                # print(f"dir_list_1: {self.dir_list_1}\n")
                switch = True
                self.dir_list_2.clear()

scan = ScanDirectory()

scan.initial_cycle()
# print(f"dir_list_1: {scan.dir_list_1}\n") # for testing purposes
scan.subsequent_cycle()
