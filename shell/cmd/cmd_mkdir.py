from os import mkdir
from colorama import init, Fore
init()

def exec(cmd):
	try:
		path = cmd[1]
		try:
			try:
				perms = int(cmd[2])
				try:
					mkdir(path, perms)
					print("Directory was created Succesfully")
					return
				except FileExistsError:
					print("{}Error: mkdir: File / Directory already exists".format(Fore.LIGHTRED_EX))
					return
			except (ValueError, IndexError) as ex:
				if type(ex).__name__ == "ValueError":
					print("{}Error: mkdir: 2nd argument needs to be an integer not a string".format(Fore.LIGHTRED_EX))
					return
				else:
					mkdir(path)
					print("Directory was created Succesfully")
					return

		except FileExistsError:
			print("{}Error: mkdir: File / Directory already exists".format(Fore.LIGHTRED_EX))
			return


	except IndexError:
		print("{}Error: mkdir: mkdir requires atleast 1 argument but 0 were given".format(Fore.LIGHTRED_EX))
		return