from os import rename
from itertools import islice
from pathlib import Path
from colorama import init, Fore
init()

def exec(cmd):
    orgpath = ""
    mvpath = ""
    indx = 0
    home = str(Path.home())

    if not any(">" in i for i in cmd):
        print("{}Error: mv: mv requires > after first path".format(Fore.LIGHTRED_EX))
        return

    try:
        for index, i in enumerate(cmd):
            if not i == "mv":
                if not i == ">":
                    orgpath = orgpath + " " + i
                else:
                    indx = int(index)
                    break

        orgpath = orgpath.lstrip()

        for i in islice(cmd, indx, None):
            if not i == ">":
                mvpath = mvpath + " " + i

        mvpath = mvpath.lstrip()

        if orgpath.startswith("~"):
            orgpath = orgpath.replace("~", home)

        if mvpath.startswith("~"):
            mvpath = mvpath.replace("~", home)

        try:
            rename(orgpath, mvpath)
        except (FileNotFoundError, OSError) as ex:
            if type(ex).__name__ == "FileNotFoundError":
                print("{}Error: mv: no such file or directory".format(Fore.LIGHTRED_EX))
                return
            elif type(ex).__name__ == "OSError":
                print("{0}Error: mv: directory '{1}' not empty".format(Fore.LIGHTRED_EX, mvpath))
                return
        
    except IndexError:
        print("{}Error: mv: mv requires 2 arguments but 0 were given".format(Fore.LIGHTRED_EX))