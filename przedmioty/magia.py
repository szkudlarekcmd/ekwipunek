"""
Moduł z klasą Magia.
"""

from typing import Any

from kontenery.typed_dicts import MagiaEfekt
from przedmioty.przedmiot import Przedmiot

# pylint: disable=too-many-arguments, too-many-positional-arguments
# pylint: disable=missing-function-docstring


class Magia(Przedmiot):
    """
    Klasa Magii.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param mana: koszt many
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        mana: int,
        efekt: MagiaEfekt,
        wymagania: dict[str, int] | None = None,
    ):
        def_dict: dict[str, Any] = {"Koszt many": mana}
        super().__init__(nazwa, wartosc, efekt)
        self._wymagania = wymagania
        # nie warunkować w ten sposób wymagań - a co jeśli zrobię else?
        # wymagania zrobić jako default pole, w którym ZAWSZE przechowywany jest koszt many
        # ale mogą być dodane dodatkowe parametry w postaci ni etylko kosztu many, ale też np
        # punkty życia - DONE
        if wymagania is None:
            self._wymagania = def_dict
        else:
            self._wymagania.update(def_dict)
        # self._wymagania.update(wymagania)
        # typed dict
        # mozna usunac pole mana z 259 i tylko zostawic je w wymaganiach - DONE

    @property
    def wymagania(self):
        return self._wymagania

    @property
    def mana(self):
        return self._wymagania["Koszt many"]


class Zwoj(Magia):
    """
    Klasa Zwój dziedzicząca z klasy Magia.
    """


class Runa(Magia):
    """
    Klasa Runa dziedzicząca z klasy Magia.

    :param krag: wymagany krąg magii, znajduje się on wtedy gdy mamy do
    czynienia z runą i jest to jedyny sposób na ich rozróżnienie
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        mana: int,
        efekt: MagiaEfekt,
        # krąg mozna zastąpić wymaganiami lub dodawać krąg do wymagań
        # w ten sam sposób, w którym robiliśmy z maną
        # OVERALL -> zostajemy przy konwencji, że wymagania są z definicji None
        # a później bezpośrednio w klasie nadpisujemy je jako dict, w którym jest mana oraz krąg
        # natomiast jeśli przy tworzeniu obiektu my zdefiniujemy wymagania, to mamy dodatkowy
        # klucz w tymże dictie - imo DONE.
        krag: int,
        wymagania: dict[str, Any] | None = None,
    ):
        def_dict: dict[str, Any] = {"Koszt many": mana, "Krąg": krag}
        super().__init__(nazwa, wartosc, mana, efekt)
        self._wymagania = wymagania
        if wymagania is None:
            self._wymagania = def_dict
        else:
            self._wymagania.update(def_dict)

    @property
    def krag(self):
        return self._wymagania["Krąg"]
