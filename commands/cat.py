"""
Implements the Linux cat command.

Supports:

- Open file
- Multiple files
"""

def run(args):
    if args.path:
        for paths in args.path:
            try:
                with open(paths) as file:
                    print(file.read())
                print()
            except FileNotFoundError:
                print(f"cat: '{paths}': No such file or directory")
            except PermissionError:
                print(f"cat: cannot open '{paths}': Permission denied")
            except IsADirectoryError:
                print(f"cat: {paths}: Is a directory")
    else:
        while True:
            text = input()
            print(text)