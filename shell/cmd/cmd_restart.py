import subprocess
from os.path import dirname, realpath, join
from . import cmd_clear

def exec(cmd):
	cmd_clear.exec(cmd)
	path = join(dirname(realpath(__file__)), "../../__main__.py")
	print(path)
	subprocess.call(["killall","Python"])
	subprocess.call(["python3",path])