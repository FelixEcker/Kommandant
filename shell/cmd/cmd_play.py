from .. import utils as ut

from os import system as sys
from os.path import dirname, realpath, join
from colorama import init, Fore
init()

def exec(cmd):
	bashPath = ""
	winPath = '"'
	title = ""

	try:
		for i in cmd:
			if not i == "play":
				bashPath = bashPath + "\ " + i

		for i in cmd:
			if not i == "play":
				winPath = winPath + " " + i

		winPath = winPath.lstrip()
		print(winPath)
		winPath = winPath + '"'

		print(winPath)

		bashPath = bashPath[2:]
		bashPath = bashPath.replace("(", "\(")
		bashPath = bashPath.replace(")", "\)")
		
		for i in cmd:
			if not i == "play":
				title = title + " " + i

		title = title.lstrip()

		print("{0}Now playing: {1}".format(Fore.MAGENTA, title))

		if ut.osname() == "OS X":
			sys("afplay {}".format(bashPath))
		elif ut.osname() == "Linux":
			sys("aplay {}".format(bashPath))
		elif ut.osname() == "Windows":
			alt(winPath)
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
