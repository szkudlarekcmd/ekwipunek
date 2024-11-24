"""
Moduł z klasą Przedmiot
"""

# pylint: disable=missing-function-docstring

from abc import ABC

from Kontenery.typed_dicts import PrzedmiotEfekt


class Przedmiot(ABC):
    """
    Base klasa, abstrakcyjna.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    """

    def __init__(self, nazwa: str, wartosc: int, efekt: PrzedmiotEfekt | None):
        self._nazwa = nazwa
        self._wartosc = wartosc
        self._efekt = efekt

    @property
    def nazwa(self):
        return self._nazwa

    @property
    def wartosc(self):
        return self._wartosc

    @property
    def efekt(self):
        return self._efekt
