from os import system as sys
from colorama import init, Fore
init()

def exec(cmd):
	args = ""
	try:
		try:
			if len(cmd[2]) > 0:
				for arg in cmd:
					if not arg == cmd[0]:
						args = args + " " + arg

			sys("cat {}".format(args))
		except IndexError:
			sys("cat {}".format(cmd[1]))
	except IndexError:
		print("{}Error: cat: cat requires atleast 1 argument but 0 were given".format(Fore.LIGHTRED_EX))