from os import chdir as cd
from colorama import init, Fore
from pathlib import Path
init()

def exec(cmd):
    path = ""

    try:
        for cmd in cmd: #peace the path back together
            if not cmd == "cd":
                path = path + " " + cmd

        if path.startswith(" "):
            path = path.lstrip()      

        try:
            if path == "~":
                cd(str(Path.home()))
            elif path.startswith("~"):
                home = str(Path.home())
                path = path.replace("~", home)
                cd(path)
            else:
                cd(path)
        except FileNotFoundError:
            print ("{0}Error: cd: no such file or directory '{1}'".format(Fore.LIGHTRED_EX, path))
    except IndexError:
        print ("{}Error: cd: cd requires 1 argument but 0 were given!".format(Fore.LIGHTRED_EX))