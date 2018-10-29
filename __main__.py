#!/usr/bin/env python3

from art import text2art

import config
import shell
from colorama import *
from time import sleep
from term import Functions as tf
from shell.cmd import cmd_clear
from os import system as sys

init()

running = False
usr = ""
sd = ""
sheu = None

def preperation():

    print("MAIN=>preperation():: Preparing all variables...")

    #Check if there is a username specified in the config.py, else use the actual System usernam
    if len(config.usrname) > 0:
        usr = config.usrname
    else:
        from getpass import getuser
        usr = getuser()

    #Check if there is a "home" directory specified in the config.py, else use the actual home dir
    if len(config.StandardDirectory) > 0:
        sd = config.StandardDirectory
    else:
        from pathlib import Path
        sd = str(Path.home())

    print("MAIN=>preperation():: Done!")
    print("MAIN=>preperation():: Initializing the shell...")

    sheu = shell.ExternalUse(sd) #Finally initialize the shell

    print("MAIN=>preparation():: Clearing screen in 3 seconds...")
    sleep(3)
    cmd_clear.exec(None)


def main():

    print(text2art("Kommandant",font="speed",chr_ignore=False))
    print("{}https://www.github.com/FelixEcker/Kommandant".format(Fore.MAGENTA))
    print("{}Version 1.0.0".format(Fore.LIGHTGREEN_EX))
    print("Copyright (C) 2018 Felix Eckert\n\n{}".format(Fore.RESET))

    running = True

    while running:
        cmd = tf.prompt(usr)

        sheu.run(cmd)


if __name__ == "__main__":
    print("Kommandant Version 1.0.0 is starting...")
    preperation()
    main()
