from os import chdir as cd
from colorama import init, Fore
from pathlib import Path
init()

def exec(cmd):
	try:
		if cmd[1] == "~":
			cd(str(Path.home()))
		else:
			cd(cmd[1])
	except IndexError:
		print ("{}Error: cd: cd requires 1 argument but 0 were given!".format(Fore.LIGHTRED_EX))