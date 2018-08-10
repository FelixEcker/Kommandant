from os import system as sys
from itertools import islice
from pathlib import Path
from .. import utils as ut
from colorama import init, Fore
init()

def exec(cmd):
	home = str(Path.home())
	args = ""
	bashPath = ""
	winPath = ''
	indx = 0

	
	try:
		for index, Arg in enumerate(cmd):
			if not Arg == "python":
				bashPath = bashPath + "\\ " + Arg
				print(bashPath)
			if ".py" in Arg:
				indx = index
				break

		bashPath = bashPath[2:]


		for index, Arg in enumerate(cmd):
			if not Arg == "python":
				winPath = winPath + " " + Arg

			if ".py" in Arg:
				indx = index
				break

		winPath = winPath.lstrip()
		winPath = '"' + winPath + '"'

		for Arg in islice(cmd, indx, None):
			if not Arg == ".py":
				args = args + " " + Arg

		args = args.lstrip()

		if winPath.startswith("~"):
			winPath = winPath.replace("~", home)

		if bashPath.startswith("~"):
			bashPath = bashPath.replace("~", home)


		try:
			sys("python {}".format(args))
		except OSError:
			print("python {0} {1}".format(bashPath, args) if ut.osname() == "OS X" or ut.osname() == "Linux" else "python {0} {1}".format(winPath, args))
	except IndexError:
		print ("executing python interpreter!")
		sys("python")
