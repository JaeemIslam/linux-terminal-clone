from commands import pwd, ls, cat, touch, mkdir, cp, mv, rm, rmdir, grep, chmod, chown, zip

import argparse

COMMANDS = {"pwd" : pwd.run,
            "ls" : ls.run,
            "cat" : cat.run,
            "touch" : touch.run,
            "cp" : cp.run,
            "mv" : mv.run,
            "rm" : rm.run,
            "rmdir" : rmdir.run,
            "mkdir" : mkdir.run,
            "grep" : grep.run,
            "chmod" : chmod.run,
            "chown" : chown.run,
            "zip" : zip.run}

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest="command")

# pwd
pwd_parser = sub.add_parser("pwd")

# ls
ls_parser = sub.add_parser("ls")
ls_parser.add_argument("path", nargs="*", default=".")

# cat
cat_parser = sub.add_parser("cat")
cat_parser.add_argument("path", nargs="*")


# touch
touch_parser = sub.add_parser("touch")
touch_parser.add_argument("path", nargs="+")

# mkdir
mkdir_parser = sub.add_parser("mkdir")
mkdir_parser.add_argument("path", nargs="*")

# cp
cp_parser = sub.add_parser("cp")
cp_parser.add_argument("path", nargs="*")

# mv
mv_parser = sub.add_parser("mv")
mv_parser.add_argument("path", nargs="*")

# rm
rm_parser = sub.add_parser("rm")
rm_parser.add_argument("path", nargs="*")

# rmdir
rmdir_parser = sub.add_parser("rmdir")
rmdir_parser.add_argument("path", nargs="*")

# grep
grep_parser = sub.add_parser("grep")
grep_parser.add_argument("path", nargs="*")

# chmod
chmod_parser = sub.add_parser("chmod")
chmod_parser.add_argument("path", nargs="*")

# chown
chown_parser = sub.add_parser("chown")
chown_parser.add_argument("path", nargs="*")

# zip
zip_parser = sub.add_parser("zip")
zip_parser.add_argument("path", nargs="*")

args = parser.parse_args()

if args.command in COMMANDS:
    COMMANDS[args.command](args)
else:
    parser.print_help()
