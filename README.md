# Duplicate File Name Deletion

## Description

A small and simple python script that deletes any file with a duplicate name in a file tree starting from a specifyed root directory cascading down the sub-directorys.

## How To Use

```bash
usage: fdd.py [-h] [-n] [-l LENGTH] [-p PATH]

        Goes through the directory tree alphabetically
        from specified root directory & deletes files with the same name
        or files with (*) at the end.

optional arguments:
  -h, --help            show this help message and exit
  -n, --notify          only echos dulpicate files and there paths
  -l LENGTH, --length LENGTH
                        skips any file that has a name shorter than LENGTH (including extention)
  -p PATH, --path PATH  the starting path (path is cwd by default)
```

## Usage Examples

Deletes all duplicate files starting at specified directory:

`python3 {PATH/TO/FILE/fdd.py -p 'PATH/TO/USE/DIR'}`