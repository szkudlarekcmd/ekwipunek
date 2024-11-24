import os
import platform


def clear():
    """
    Czyści terminal.
    (emulate terminal in output console)
    """
    if platform.system() == "Windows":
        return os.system("cls")
    else:
        return os.system("clear")
