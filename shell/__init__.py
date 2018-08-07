from colorama import *
init()

from os import chdir as cd
from os import system as sys

from .cmd import cmd_clear
from .cmd import cmd_exit
from .cmd import cmd_python
from .cmd import cmd_cd
from .cmd import cmd_cat
from .cmd import cmd_del
from .cmd import cmd_dir
from .cmd import cmd_cmds
from .cmd import cmd_play
from .cmd import cmd_ssh
from .cmd import cmd_restart

commands = {
    "clear":cmd_clear,
    "exit":cmd_exit,
    "python3":cmd_python,
    "cd":cmd_cd,
    "cat":cmd_cat,
    "del":cmd_del,
    "dir":cmd_dir,
    "cmds":cmd_cmds,
    "play":cmd_play,
    "ssh":cmd_ssh,
    "restart":cmd_restart
}


class ExternalUse:
    def __init__(self, sd):
        self.standardDir = sd
        cd(sd)


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