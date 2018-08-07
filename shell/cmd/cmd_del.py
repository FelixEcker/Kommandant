import os
from shutil import rmtree
from pathlib import Path
from colorama import init, Fore
init()

def exec(cmd):
    try:
        path = str(cmd[1])

        if path.startswith("~"):
            home = str(Path.home())
            path = path.replace("~", home)
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                rmtree(path)
            else:
                print("{}Error: del: this file / directory doesn't exist".format(Fore.LIGHTRED_EX))
        else:
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
            else:
                print("{}Error: del: this file / directory doesn't exist".format(Fore.LIGHTRED_EX))

    except IndexError:
        print("{}Error: del: del requires 1 argument but 0 were given".format(Fore.LIGHTRED_EX))
