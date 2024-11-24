from typing import Any

from Kontenery.typed_dicts import PancerzEfekt
from Przedmioty.przedmiot import Przedmiot


class Pancerz(Przedmiot):
    """
    Klasa pancerzy.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param ochrona: ochrona przed bronią
    :param wymagania: wymagane atrybuty do użycia danego przedmiotu
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        # pole efekt nie musi być tylko ochroną... może być to bonus
        # w postaci many
        # pomysł - zmergować pola ochrona oraz efekt (?) - Done
        efekt: PancerzEfekt | dict[str, Any],
        wymagania: dict[str, int] | None = None,
    ):
        super().__init__(nazwa, wartosc, efekt)
        self._wymagania = wymagania

    @property
    def wymagania(self):
        return self._wymagania
