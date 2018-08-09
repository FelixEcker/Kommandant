from os import system as sys
from os import name
from os import listdir as ls
from os import getcwd as cwd
from pathlib import Path
from colorama import init, Fore
init()

def exec(cmd):
    args = ""
    path = ""
    home = str(Path.home())
    for cmd in cmd: #peace the path back together
        if not cmd == "dir":
            path = path + " " + cmd

    if path.startswith(" "):
        path = path.lstrip()

    if len(path) > 0:
        if path.startswith("~"):
            path = path.replace("~", home)

            try:
                dir = ls(path)
            except FileNotFoundError:
                print("{0}Error: dir: no such file or directory '{1}'".format(Fore.LIGHTRED_EX, path))
                return

            for i in dir:
                print(i)
        else:
            try:
                dir = ls(path)
            except Exception:
                print("{0}Error: dir: no such file or directory '{1}'".format(Fore.LIGHTRED_EX, path))
                return

            for i in dir:
                print(i)
    else:
        for i in ls(cwd()):
            print(i)