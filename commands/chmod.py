"""
Implements the Linux chmod command.

Supports:

- Only numeric mode
- File permission modify
- Directory permission modify
- Multiple files/directories
"""

import os
from commands import lessArgs

def run(args):
    perms = [1,2,3,4,5,6,7]
    if args.path:
        if len(args.path) > 1:
            permission = args.path[0]
            files = args.path[1:]
            flag = True
            for chr in permission:
                if int(chr) not in perms:
                    flag = False
                    break
            if flag:
                for paths in files:
                    try:
                        os.chmod(paths,int(permission, 8))
                    except PermissionError:
                        print(f"chmod: cannot access '{paths}': Permission denied")
                    except FileNotFoundError:
                        print(f"chmod: cannot access '{paths}': No such file or directory")
            else:
                print(f"chmod: invalid mode: '{permission}'")
                print("Try 'chmod --help' for more information.")
        else:
            lessArgs.LessArgs(args.command, permission)
    else:
        lessArgs.ZeroArgs(args.command)