from os import mkdir
from colorama import init, Fore
init()

def exec(cmd):
	try:
		path = cmd[1]
		try:
			mkdir(path, 755 )
		except FileExistsError:
			print("{}Error: mkdir: File / Directory already exists".format(Fore.LIGHTRED_EX))
			return


		print("Directory was created Succesfully")
	except IndexError:
		print("{}Error: mkdir: mkdir requires 1 argument but 0 were given".format(Fore.LIGHTRED_EX))
		return