#Koshell for Kommandant version 1.0.2
#Copyright (c) 2018 Felix Eckert
#
#This is a modified version of the original Koshell
#for Kommandant, visit the original at https://github.com/FelixEcker/Koshell

from colorama import *
init()

from os import chdir as cd

from .cmd import cmd_clear
from .cmd import cmd_exit
from .cmd import cmd_python
from .cmd import cmd_python3
from .cmd import cmd_cd
from .cmd import cmd_cat
from .cmd import cmd_del
from .cmd import cmd_dir
from .cmd import cmd_cmds
from .cmd import cmd_play
from .cmd import cmd_ssh
from .cmd import cmd_restart
from .cmd import cmd_mkdir
from .cmd import cmd_mv
from .cmd import cmd_nano

commands = {
    "clear":cmd_clear,
    "exit":cmd_exit,
    "python3":cmd_python3,
    "python":cmd_python,
    "cd":cmd_cd,
    "cat":cmd_cat,
    "del":cmd_del,
    "dir":cmd_dir,
    "cmds":cmd_cmds,
    "play":cmd_play,
    "ssh":cmd_ssh,
    "restart":cmd_restart,
    "mkdir":cmd_mkdir,
    "mv":cmd_mv,
    "nano":cmd_nano
}


class ExternalUse:
    def __init__(self, sd):
        print("shell/INIT=>ExternalUse=>__init__():: Starting shell preparation...")
        print("shell/INIT=>ExternalUse=>__init__():: Changin working directory to {}".format("VAR__sd::"+sd))
        self.standardDir = sd
        cd(sd)
        print("shell/INIT=>ExternalUse=>__init__():: All shell preparation done! returning to function preparation()")


    def run(self, cmd):
        cmd = cmd.split()
        if len(cmd) > 0:
            if cmd[0] in commands:
                commands.get(cmd[0]).exec(cmd)
            else:
                print("{0}Kommandant Shell: {1}: command not found".format(Fore.LIGHTRED_EX, cmd[0]))
        else:
            print("\n\n")
            return None
