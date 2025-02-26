"""
Moduł z klasą artefakt
"""

from typing import Any

from kontenery.typed_dicts import ArtefaktEfekt
from przedmioty.przedmiot import Przedmiot


# pylint: disable=missing-function-docstring
class Artefakt(Przedmiot):
    """
    Klasa artefakty.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    """

    # dodaj wymagania tu :)
    # dodaj pasy
    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        efekt: ArtefaktEfekt,
        wymagania: dict[str, Any] | None = None,
    ):
        super().__init__(nazwa, wartosc, efekt)

        self._wymagania = wymagania

    @property
    def wymagania(self):
        return self._wymagania


class Pierscien(Artefakt):
    """
    Klasa Pierścien dziedzicząca z klasy Artefakt
    """


class Amulet(Artefakt):
    """
    Klasa Amulet dziedzicząca z klasy Artefakt
    """


class Pas(Artefakt):
    """
    Klasa Pas dziedzicząca z klasy Artefakt
    """


class Tablica(Artefakt):
    """
    Klasa Tablica dziedzicząca z klasy Artefakt
    """
