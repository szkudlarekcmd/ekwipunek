"""
Moduł z klasą Jedzenie.
"""

from Kontenery.typed_dicts import JedzenieEfekt
from Przedmioty.przedmiot import Przedmiot


class Jedzenie(Przedmiot):
    """
    Klasa Jedzenie - Kolejna klasa, której nie da się ubrać. Użycie danej pozycji powoduje
    jej zjedzenie, przez co pozycja zmniejsza swoją ilość w ekwipunku o jeden, lub znika z
    ekwipunku.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        efekt: JedzenieEfekt,
    ):
        super().__init__(nazwa, wartosc, efekt)
