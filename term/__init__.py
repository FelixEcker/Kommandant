from colorama import *
init()

from os import getcwd as cwd

class Functions:
    def prompt(usrname):
        return input("{0}{1}@Kommandant:{2}{3} -${4} ".format(Fore.LIGHTBLUE_EX, usrname, Fore.GREEN, cwd(), Fore.WHITE))