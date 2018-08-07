from colorama import init, Fore
import subprocess

def exec(cmd):
	try:
		subprocess.call(["ssh", cmd[1]])
	except IndexError:
		print("{}Error: ssh: ssh requires 1 argument but 0 were given".format(Fore.LIGHTRED_EX))