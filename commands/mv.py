"""
Implements the Linux mv command.

Supports:

- Moves file
- Moves Directory
- Multiple sources
"""

import shutil, os
from pathlib import Path
from commands import lessArgs

def run(args):
    if args.path:
        if len(args.path) > 1:
            length = len(args.path)
            des = args.path[-1]
            src = args.path[:-1]
            for paths in src:
                try:
                    if os.path.isfile(paths):
                        if length == 2:
                            if not Path(des).exists():
                                Path(des).touch()
                                shutil.move(paths, des)
                            else:
                                shutil.move(paths, des)
                        elif os.path.isdir(des):
                            shutil.move(paths, des)
                    elif os.path.isdir(paths) and os.path.isdir(des):
                        shutil.move(paths, des)
                except FileNotFoundError:
                    print(f"mv: cannot stat '{paths}': No such file or directory")
                except NotADirectoryError:
                    print(f"mv: target '{des}': Not a directory")
                except PermissionError:
                    print(f"mv: cannot stat '{paths}': Permission denied")
        else:
            print(f"mv: missing destination file operand after '{args.path[0]}'")
            print("Try 'mv --help' for more information.")
    else:
        lessArgs.ZeroArgs(args.command)