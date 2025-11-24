
import sys,platform

def current_system():
    plat = sys.platform
    if plat == "win32":
        return "windows"
    elif plat == "darwin":
        return "mac"
    elif plat.startswith("linux"):
        return "linux"
    return "unknown"

def get_current_system():
    system = platform.system().lower()
    if system == "windows":
        return "windows"
    elif system == "darwin":
        return "mac"
    elif system == "linux":
        return "linux"
    return "unknown"


