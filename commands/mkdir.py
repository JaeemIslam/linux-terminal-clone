"""
Implements the Linux mkdir command.

Supports:

- Creates directory
- Multiple directories
"""

import os
from commands import lessArgs

def run(args):
    if args.path:
        for paths in args.path:
            try:
                os.mkdir(paths)
            except FileExistsError:
                print(f"mkdir: cannot create directory '{paths}': File exists")
            except PermissionError:
                print(f"mkdir: cannot create directory '{paths}': Permission denied")
    else:
        lessArgs.ZeroArgs(args.command)