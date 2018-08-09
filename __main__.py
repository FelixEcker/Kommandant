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

def main():
    cmd_clear.exec("")
    print (text2art("Kommandant",font="speed",chr_ignore=False))
    print ("{}https://www.github.com/".format(Fore.MAGENTA))
    print ("{}Version 1.0.0".format(Fore.LIGHTGREEN_EX))
    print ("Copyright (C) 2018 Felix Eckert\n\n{}".format(Fore.RESET))

    running = True
    
    sheu = shell.ExternalUse(config.StandardDirectory)

    while running:
        cmd = tf.prompt(config.usrname)
        
        sheu.run(cmd)


if __name__ == "__main__":
    main()