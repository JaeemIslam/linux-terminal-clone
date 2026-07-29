"""
Implements the Linux rmdir command.

Supports:

- Removes directory
- Multiple directories
"""

import os
from commands import lessArgs

def run(args):
    if args.path:
        for paths in args.path:
            try:
                os.rmdir(paths)
            except FileNotFoundError:
                print(f"rm: cannot remove '{paths}': No such file or directory")
            except NotADirectoryError:
                print(f"rmdir: failed to remove '{paths}': Not a directory")
            except PermissionError:
                print(f"rmdir: failed to remove '{paths}': Permission denied")
    else:
        lessArgs.ZeroArgs(args.command)