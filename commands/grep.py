"""
Implements the Linux grep command.

Supports:

- Text finding in file
- Multiple files
"""

from pathlib import Path

def run(args):
    if args.path:
        if len(args.path) > 1:
            text = args.path[0]
            paths = args.path[1:]
            for files in paths:
                try:
                    with Path(files).open() as file:
                        for line in file:
                            if text in line:
                                if len(paths) == 1:
                                    print(line)
                                else:
                                    print(f"{files}: {line}")
                except FileNotFoundError:
                    print(f"grep: {files}: No such file or directory")
                except IsADirectoryError:
                    print(f"grep: {files}: Is a directory")
                except PermissionError:
                    print(f"grep: cannot access '{files}': Permission denied")
        else:
            while True:
                input()
    else:
        print("Usage: grep [OPTION]... PATTERNS [FILE]...")
        print("Try 'grep --help' for more information.")