from .. import utils as ut
from os import system as sys
from colorama import init, Fore
from os.path import realpath, dirname, join
from pathlib import Path
init()

def exec(cmd):
	home = str(Path.home())
	args = ""
	bashPath = ""
	winPath = ''
	indx = 0

	try:
		for Arg in cmd:
			if not Arg == "nano":
				bashPath = bashPath + "\\ " + Arg
				print(bashPath)

		bashPath = bashPath[2:]
		print(bashPath)


		for Arg in cmd:
			if not Arg == "nano":
				winPath = winPath + " " + Arg

		winPath = winPath.lstrip()
		winPath = '"' + winPath + '"'

		args = args.lstrip()

		if winPath.startswith("~"):
			winPath = winPath.replace("~", home)

		if bashPath.startswith("~"):
			bashPath = bashPath.replace("~", home)

		try:
			sys("nano {0} {1}".format(bashPath, args) if ut.osname() == "OS X" or ut.osname() == "Linux" else "{0} {1} {2}".format(join(dirname(realpath(__file__)), "../builtinexecutables/nano.exe"), winPath, args))
		except Exception:
			print("{}Error: An unknown error occured whilst executing nano!".format(Fore.LIGHTRED_EX))
	except IndexError:
		print("{}Error: nano: nano requires atleast 1 argument but 0 were given!".format(Fore.LIGHTRED_EX))