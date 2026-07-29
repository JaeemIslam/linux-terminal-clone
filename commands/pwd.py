"""
Implements the Linux pwd command.

Supports:

- Prints cwd
"""

import os

def run(args):
    print(os.getcwd())