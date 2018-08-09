from sys import platform

def osname():
    platforms = {
        "linux1" : "Linux",
        "linux2" : "Linux",
        "darwin" : "OS X",
        "win32" : "Windows"
    }

    if platform not in platforms:
        return platform

    return platforms[platform]