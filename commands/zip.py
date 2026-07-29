"""
Implements the Linux zip command.

Supports:

- Creates zip file
- Updates zip file
- Zips Multiple files/directories
"""

from zipfile import ZipFile
from pathlib import Path
import sys

def repeat(zipf, items, updt):
    if Path(items).exists():
        zipf.write(items)
        if not updt:
            print(f"adding: {items} (stored 0%)")
        else:
            print(f"updating: {items} (stored 0%)")
    else:
        print(f"zip warning: name not matched: {items}")

def run(args):
    if args.path:
        if len(args.path) > 1:
            zipper = args.path[0]
            files = args.path[1:]

            if not Path(zipper).exists():
                with ZipFile(zipper, "w") as zipfile:
                    for paths in files:
                        repeat(zipfile, paths, False)
            else:
                for paths in files:
                    if paths not in ZipFile(zipper).namelist():
                        with ZipFile(zipper, "a") as zipfile:
                            repeat(zipfile, paths, False)
                    else:
                        with ZipFile(zipper, "w") as zipfile:
                            for paths in files:
                                repeat(zipfile, paths, True)
                            sys.exit()
        else:
            print(f"zip error: Nothing to do! ({zipper}.zip)")
    else:
        pass