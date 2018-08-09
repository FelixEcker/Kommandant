from os import system as sys
from colorama import init, Fore
init()

def exec(cmd):
	args = ""

	try:
		for Arg in cmd:
			if not Arg == "python":
				args = args + Arg + " "
		
		try:
			sys("python {}".format(args))
		except OSError:
			print("{}Error: python: An unknown Exception occured whilst executing command!".format(Fore.LIGHTRED_EX))
	except IndexError:
		print ("executing python3 interpreter!")
		sys("python3")
