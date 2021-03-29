"""
This script finds and deletes duplicate files in a set of dir paths
"""

from os import listdir, remove, getcwd, path
import sys
from argparse import ArgumentParser

class ScanDirectory:

    """
    Scans files and directorys then deletes files with the same name.
    This is done from root dir (given as argument or current working directory)
    to all subsequent directorys.
    """

    def __init__(self, args):
        self.args = args
        self.comparison_list = [] # array to check file names against 
        self.dir_list_1 = []
        self.dir_list_2 = []

    def file_cycle(self, files, dir_path, switch=False):
        for file in files:
            if "." in file: # if file
                if file not in self.comparison_list:            
                    self.comparison_list.append(file)

                elif file in self.comparison_list:
                    # print(f"{file} at {dir_path} is a duplicate") # temp
                    pass

                elif "(" in file:            
                    # print(f"{file} at {dir_path} is a duplicate") # temp
                    pass

            else: # if dir
                if switch == True:
                    self.dir_list_2.append(f"{dir_path}/{file}") # appends directory path to dir_list_2
                else:
                    self.dir_list_1.append(f"{dir_path}/{file}") # appends directory path to dir_list_2

    def initial_cycle(self):

        """Does the first scan in the root directory"""

        # gets initial path
        if self.args.path == None: # if inline argument
            dir_path = getcwd()
        
        else: # current dir
            dir_path = self.args.path

        try:
            if dir_path[0] == "/": # if arg is absolute path
                files = listdir(dir_path)

            else: # if arg is relative path
                dir_path = path.abspath(dir_path)
                files = listdir(dir_path)
        
        except:
            raise Exception(f"{dir_path} does not exist")

        self.file_cycle(files, dir_path, switch=False)

    def subsequent_cycle(self):

        switch = True

        while self.dir_list_1 or self.dir_list_2: # until both lists are empty
            if switch == True:
                for dir_path in self.dir_list_1:
                    files = listdir(dir_path)

                    self.file_cycle(files, dir_path, switch=True)

                # print(f"dir_list_2: {self.dir_list_2}\n")
                switch = False
                self.dir_list_1.clear()

            elif switch == False:
                for dir_path in self.dir_list_2:

                    files = listdir(dir_path)

                    self.file_cycle(files, dir_path, switch=False)

                # print(f"dir_list_1: {self.dir_list_1}\n")
                switch = True
                self.dir_list_2.clear()

parser = ArgumentParser() # need to add description
parser.add_argument("-l", "--length", type=int, help="length of file name (including extention)")
parser.add_argument("-p", "--path", type=str, help="the starting path (path is cwd by default")
args = parser.parse_args()
# print(args)

scan = ScanDirectory(args)
scan.initial_cycle()
# print(f"dir_list_1: {scan.dir_list_1}\n")
scan.subsequent_cycle()
