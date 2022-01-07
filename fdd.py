"""
This script finds and deletes duplicate files in a set of dir paths
"""

from os import listdir, remove, getcwd, path
from argparse import ArgumentParser, RawDescriptionHelpFormatter

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
                if file not in self.comparison_list and len(file) > self.args.length:            
                    self.comparison_list.append(file)

                elif file in self.comparison_list and len(file) > self.args.length:
                    if self.args.notify == True:
                        # comparison_path = [path for path in self.comparison_list if file in path]
                        print(f"{file} at {dir_path} is a duplicate")
                    else: # delete file
                        remove(f"{dir_path}/{file}")
                        print(f"removed: {dir_path}/{file}")

                elif "(" in file and len(file) > self.args.length:
                    if self.args.notify == True:
                        # comparison_path = [path for path in self.comparison_list if file in path]
                        print(f"{file} at {dir_path} is a duplicate")
                    else: # delete file
                        remove(f"{dir_path}/{file}")
                        print(f"removed: {dir_path}/{file}")

            else: # if dir
                if switch == True:
                    self.dir_list_2.append(f"{dir_path}/{file}") # appends directory path to dir_list_2
                else:
                    self.dir_list_1.append(f"{dir_path}/{file}") # appends directory path to dir_list_1

    def initial_cycle(self):

        """Does the first scan in the root directory"""

        # gets initial path
        if self.args.path == None: # if no path given
            dir_path = getcwd()
        
        else: # if path given
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
        # print("dir_list_1:")
        # for i in self.dir_list_1:
        #     print(i)

    def subsequent_cycle(self):

        """Does every cycle after initial cycle method"""

        switch = True

        while self.dir_list_1 or self.dir_list_2: # until both lists are empty
            if switch == True:
                for dir_path in self.dir_list_1:
                    files = listdir(dir_path)

                    self.file_cycle(files, dir_path, switch=True)

                # print("dir_list_2:")
                # for i in self.dir_list_2:
                #     print(i)
                switch = False
                self.dir_list_1.clear()

            elif switch == False:
                for dir_path in self.dir_list_2:

                    files = listdir(dir_path)

                    self.file_cycle(files, dir_path, switch=False)

                # print("dir_list_1:")
                # for i in self.dir_list_1:
                #     print(i)
                switch = True
                self.dir_list_2.clear()

parser = ArgumentParser(
    formatter_class=RawDescriptionHelpFormatter, 
    description="""
        Goes through the directory tree alphabetically
        from specified root directory & deletes files with the same name
        or files with (*) at the end."""
        )
parser.add_argument("-n", "--notify", action="store_true", help="only echos dulpicate files and their paths (does not delete)")
parser.add_argument("-l", "--length", default=0, type=int, help="skips any file that has a name shorter than LENGTH (including extention)")
parser.add_argument("-p", "--path", type=str, help="the starting path (path is cwd by default)")
args = parser.parse_args()
# print(args)

scan = ScanDirectory(args)
scan.initial_cycle()
scan.subsequent_cycle()
# print(scan.comparison_list)
