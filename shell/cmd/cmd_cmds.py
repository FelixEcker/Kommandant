from os import listdir as ls
from os.path import isfile, join, dirname, realpath

def exec(cmd):
	scptdir = dirname(realpath(__file__))
	files = [f for f in ls(scptdir) if isfile(join(scptdir, f))]

	for file in files:
		if file.startswith("cmd_"):
			file = file.replace("cmd_", "")
			file = file.replace(".py", "")
			file = file.replace("python", "python3")
			print (file)