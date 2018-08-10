from os import system as sys
from os import name as nm

def exec(cmd):
    sys("cls" if nm == "nt" else "clear")