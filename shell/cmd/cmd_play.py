from os import system as sys
from os import name
from os.path import dirname, realpath, join
from colorama import init, Fore
init()

def exec(cmd):
	bashPath = ""
	title = ""
	orgcmd = cmd

	try:
		for cmd in cmd:
			if not cmd == "play":
				bashPath = bashPath + "\ " + cmd

		bashPath = bashPath[2:]
		bashPath = bashPath.replace("(", "\(")
		bashPath = bashPath.replace(")", "\)")

		print(bashPath)
		
		for cmd in orgcmd:
			if not cmd == "play":
				title = title + " " + cmd

		title = title.lstrip()

		print("{0}Now playing: {1}".format(Fore.MAGENTA, title))
		sys("afplay {0} > {1}".format(bashPath, str(join(dirname(realpath(__file__)), "../stdout.txt"))) if not name == "nt" else alt(title))
	except IndexError:
		print("{}Error: play: play takes 1 argument but 0 were given".format(Fore.LIGHTRED_EX))


def alt(snd):
	from pygame import mixer
	try:
		mixer.init()
		mixer.music.load(snd)
		mixer.music.play()
	except Exception:
		print("{}Error: play: Unspecified Exception".format(Fore.LIGHTRED_EX))