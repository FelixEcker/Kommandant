#!/usr/bin/env python3

from art import text2art

import config
import shell
from colorama import *
from term import Functions as tf
from shell.cmd import cmd_clear
from os import system as sys

init()

running = False
usr = ""
sd = ""

def main():
    cmd_clear.exec("")
    print (text2art("Kommandant",font="speed",chr_ignore=False))
    print ("{}https://www.github.com/FelixEcker/Kommandant".format(Fore.MAGENTA))
    print ("{}Version 1.0.0".format(Fore.LIGHTGREEN_EX))
    print ("Copyright (C) 2018 Felix Eckert\n\n{}".format(Fore.RESET))

    running = True

    if len(config.usrname) > 0:
        usr = config.usrname
    else:
        from getpass import getuser
        usr = getuser()

    if len(config.StandardDirectory) > 0:
        sd = config.StandardDirectory
    else:
        from pathlib import Path
        sd = str(Path.home())

    sheu = shell.ExternalUse(sd)

    while running:
        cmd = tf.prompt(usr)
        
        sheu.run(cmd)


if __name__ == "__main__":
    main()