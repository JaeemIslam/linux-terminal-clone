"""
Implements the Linux chown command.

Supports:

- Owner change
- Group change
- Multiple files/directories
"""

import os, pwd, grp
from commands import lessArgs

def run(args):
    if args.path:
        if len(args.path) > 1:
            oGiven = False
            gGiven = False
            oValid = False
            gValid = False
            owner = ""
            group = ""

            owngrp = args.path[0]
            files = args.path[1:]
            if ":" in owngrp and owngrp.count(":") == 1:
                if owngrp.startswith(":"):
                    group = owngrp.removeprefix(":")
                    gGiven = True
                elif owngrp.endswith(":"):
                    owner = owngrp.removesuffix(":")
                    oGiven = True
                else:
                    list_owngrp = owngrp.split(":")
                    owner = list_owngrp[0]
                    group = list_owngrp[1]
                    oGiven = True
                    gGiven = True
            elif ":" not in owngrp:
                owner = owngrp
                oGiven = True
            else:
                print(f"chown: invalid group: '{owngrp}'")

            try:
                if (oGiven and not gGiven):
                    if pwd.getpwnam(owner):
                        oValid = True
                        uid = pwd.getpwnam(owner).pw_uid
                elif (gGiven and not oGiven):
                    if grp.getgrnam(group):
                        gValid = True
                        gid = grp.getgrnam(group).gr_gid
                elif (oGiven and gGiven):
                    if pwd.getpwnam(owner):
                        oValid = True
                        uid = pwd.getpwnam(owner).pw_uid
                    if grp.getgrnam(group):
                        gValid = True
                        gid = grp.getgrnam(group).gr_gid
            except KeyError:
                pass

            
            for paths in files:
                try:
                    if oGiven and gGiven:
                        if oValid and gValid:
                            os.chown(paths, uid, gid)
                        elif not oValid:
                            print(f"chown: invalid user: '{owngrp}'")
                        else:
                            print(f"chown: invalid group: '{owngrp}'")
                    elif oGiven:
                        if oValid:
                            os.chown(paths, uid, -1)
                        else:
                            print(f"chown: invalid user: '{owngrp}'")
                    elif gGiven:
                        if gValid:
                            os.chown(paths, -1, gid)
                        else:
                            print(f"chown: invalid group: '{owngrp}'")
                except FileNotFoundError:
                    print(f"chown: cannot access '{paths}': No such file or directory")
                except PermissionError:
                    print(f"chown: cannot access '{paths}': Permission denied")
        else:
            lessArgs.LessArgs(args.command, args.path[0])
    else:
        lessArgs.ZeroArgs(args.command)