# Kommandant
A "shell" written in python3

# Installation
Installation is really simple, just move it to where you want to have it and execute it with `python3 __main__.py` or `./__main__.py`.

You'll also have to enter your Standard directory in the config.py file, just place the path in the Variable `StandardDirectory`.

You can set your username in the variable usrname in the config.py file, if you don't set it, your OS username will be used.

# Requirements

Python 3.5 or higher

Colorama (`pip3 install colorama`)

Art (`pip3 install art`)

Pygame (`pip3 install pygame`Used for playing sounds on windows)

# Commands

`nano` executes nano (Also on windows, check it out [https://www.nano-editor.org/dist/win32-support/](here))

`python3` executes python3 with given args

`python` executes python with given args

`cd` changes working directory

`mkdir` creates new directory

`mv` moves given file / dir

`clear` clears the terminal

`exit` exits Kommandant

`cat` executes the cat command just like in bash

`del` deletes files / directories / directories with contents

`dir` gets  directory contents of given path or current directory (if no path is included)

`cmds` lists all current commands

`play` plays a sound (executes afplay on macosx or pygames in game mixer on windows)

`ssh` establishes an ssh connection (`ssh usr@ip`)

`restart` restarts Kommandant (**Has some major bugs**)


