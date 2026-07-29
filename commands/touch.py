"""
Implements the Linux touch command.

Supports:

- Creates file
- Multiple files
"""

from pathlib import Path
from commands import lessArgs

def run(args):
    if args.path:
        for paths in args.path:
            try:
                Path(paths).touch()
            except FileExistsError:
                continue
            except PermissionError:
                print(f"touch: cannot touch 'path': Permission denied")
    else:
        lessArgs.ZeroArgs(args.command)