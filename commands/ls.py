"""
Implements the Linux ls command.

Supports:

- Lists cwd contents
- Lists specific directory contents
- Multiple directories
"""

import os

def run(args):
    if args.path:
        for paths in args.path:
            try:
                for files in os.listdir(paths):
                    print(files)
                print()
            except FileNotFoundError:
                print(f"ls: cannot  access '{paths}': No such file or directory")
            except NotADirectoryError:
                print(paths)
            except PermissionError:
                print(f"ls: cannot access '{paths}': Permission denied")
    else:
        for files in os.listdir(paths):
            print(files)