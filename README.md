# Linux Terminal Clone

A Python-based Linux terminal clone that simulates common Linux commands in a custom command-line interface.

## Features
- Interactive command-line interface
- Argument parsing
- Support for common Linux commands
- File and directory management
- Permission handling
- Error messages similar to a real Linux terminal
- Archive creation

## Supported Commands
- pwd
- cd
- ls
- touch
- mkdir
- cp
- mv
- grep
- rm
- rmdir
- chmod
- chown
- zip

More commands will be added in future updates.

## Project Structure
```text
linux-terminal-clone/
├── commands/
    ├── pwd.py
    ├── cd.py
    ├── ls.py
    ├── touch.py
    ├── mkdir.py
    ├── cp.py
    ├── mv.py
    ├── grep.py
    ├── rm.py
    ├── rmdir.py
    ├── chmod.py
    ├── chown.py
    ├── zip.py
├── shell.py
├── requirements.txt
└── README.md
```
## Running the Project
- Open terminal
- Go to the project directory (Example: cd Downloads/linux-terminal-clone)
- Run: python shell.py `<command>` 

## Purpose

This project was created as part of my journey toward becoming a cybersecurity professional. While it is not a security tool, building a terminal clone provided practical experience with:

- Command parsing
- File system operations
- Permission management
- Python application architecture
- Linux command behavior

## Future Improvements
- Add more Linux commands
- Command history
- Environment variables
- Shell scripting support
- Better error handling
- Cross-platform compatibility

## Technologies Used
- Python 3
- argparse
- os
- pathlib
- shutil
- pwd
- grp
- sys
- zipfile

## License

This project is licensed under the MIT License.
