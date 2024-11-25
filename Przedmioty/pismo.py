"""
Moduł z klasą Pismo
"""

from Kontenery.typed_dicts import PismoEfekt
from Przedmioty.przedmiot import Przedmiot

# pylint: disable=missing-function-docstring


class Pismo(Przedmiot):
    """
    Klasa Pism - wyjątkowa klasa, ponieważ pisma nie można "ubrać". Użycie danej pozycji powoduje
    wyprintowanie treści do konsoli.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param tresc: treść danego pisma
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        tresc: str,
        efekt: PismoEfekt | None = None,
        # można dodać opcjonalnie wymagania
        # czy warto przechowywać pole treść w osobnym polu?
        # można wyciągać go ze słownika efekt - teoretycznie tak, ale czy powinniśmy iść tą drogą
        # generalnie z mojego punktu widzenia najlepiej by było, by efekt defaultowo był None,
        # a dopiero wewnątrz innita nadpisywali jego wartość poprzez to, co podajemy w treści.
        # Efekt nie NONE, gdy na przykład po przeczytaniu czegoś dostajemy jakieś bonusy.
        # I tak dalej.
    ):
        self._tresc = tresc
        if efekt is None:
            efekt = {"Treść": tresc}
        super().__init__(nazwa, wartosc, efekt)

    @property
    def tresc(self):
        return self._tresc
