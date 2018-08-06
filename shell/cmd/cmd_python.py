from os import system as sys
from colorama import init, Fore
init()

def exec(cmd):
	args = ""

	try:
		for Arg in cmd:
			if not Arg == "python3":
				args = args + Arg + " "
		
		try:
			sys("python3 {}".format(args))
		except Exception:
			print ("{}Error: An unknown error occured whilst executing script!".format(Fore.LIGHTRED_EX))
	except IndexError:
		print ("executing python3 interpreter!")
		sys("python3")