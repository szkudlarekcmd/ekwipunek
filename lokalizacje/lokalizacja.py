"""
Moduł z klasą Lokalizacja.
"""

from abc import ABC


class Lokalizacja(ABC):
    """
    Klasa Lokalizacja.
    """

    def __init__(self):
        self.zawartosc = None

    def __str__(self):
        return type(self).__name__

    def spojrz(self):
        """
        Metoda zwracająca listę zawartość
        """
        # odpowiednik wyswietl, aka spojrz na podloge
        return self.zawartosc
