"""
Implements the Linux rm command.

Supports:

- Removes file
- Multiple files
"""

import os
from commands import lessArgs

def run(args):
    if args.path:
        for paths in args.path:
            try:
                os.remove(paths)
            except FileNotFoundError:
                print(f"rm: cannot remove '{paths}': No such file or directory")
            except IsADirectoryError:
                print(f"rm: cannot remove '{paths}': Is a directory")
            except PermissionError:
                print(f"rm: cannot remove '{paths}': Permission denied")
    else:
        lessArgs.ZeroArgs(args.command)
