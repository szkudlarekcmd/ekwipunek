"""
Moduł z klasą ekwipunek
"""

# pylint: disable=consider-using-dict-items, missing-function-docstring,
# pylint: disable=too-many-instance-attributes, inconsistent-return-statements)
from collections import defaultdict
from typing import Any

from Kontenery.kontenery import (
    Artefakty,
    Bronie,
    Kontener,
    Pancerze,
    Pisma,
    Pozostalosci,
    PrzedmiotyMagiczne,
    Zywnosc,
)
from Przedmioty.artefakt import Artefakt
from Przedmioty.bron import Bron
from Przedmioty.jedzenie import Jedzenie
from Przedmioty.magia import Magia
from Przedmioty.pancerz import Pancerz
from Przedmioty.pismo import Pismo
from Przedmioty.pozostale import Pozostale
from Przedmioty.przedmiot import Przedmiot


class Ekwipunek:
    """
    Klasa Ekwipunek -> To w niej znajdują się Przedmioty z Podłogi dodane za pomocą
    Bohatera. Tutaj również znajduje się kontener w uzyciu (nie wiem, czy słusznie).

    ...
    Atrybuty

    ----------
    bronie: Kontener
        kontener na przedmioty klasy Broń
    pancerze: Kontener
        kontener na przedmioty klasy Pancerz
    przedmioty magiczne: Kontener
        kontener na przedmioty klasy Magia
    pisma: Kontener
        kontener na przedmioty klasy Pismo
    artefakty: Kontener
        kontener na przedmioty klasy Artefakt
    jedzenie: Kontener
        kontener na przedmioty klasy Jedzenie
    pozostale: Kontener
        kontener na przedmioty klasy Pozostale
    w_uzyciu: Kontener
        kontener zawierający przedmioty znajdujące się w danej
        chwili w użyciu
    :param magazyn: słownik zawierający wszystkie kontenery przypisane
        do odpowiedniego klucza
    """

    def __init__(self):
        self._bronie: Kontener = Bronie()
        self._pancerze: Kontener = Pancerze()
        self._przedmioty_magiczne: Kontener = PrzedmiotyMagiczne()
        self._pisma: Kontener = Pisma()
        self._artefakty: Kontener = Artefakty()
        self._jedzenie: Kontener = Zywnosc()
        self._pozostale: Kontener = Pozostalosci()
        # TODO: zamiast default dicta użyć dataclass (spróbuj), gdzie definuję
        # pola oraz ile może być przedmiotów. Zdefiniować to na sztywno
        # przełączyć na 3.13 sięęęe - 3.13 sprawia olbrzymie problemy z tym pycharmem
        # więc na ten moment go odpuszczam : - )

        self._w_uzyciu = defaultdict(list)  # eee do ogarnięcia (?)
        self._magazyn: dict[str, Kontener] = {
            str(self._bronie): self._bronie,
            str(self._pancerze): self._pancerze,
            str(self._przedmioty_magiczne): self._przedmioty_magiczne,
            str(self._pisma): self._pisma,
            str(self._artefakty): self._artefakty,
            str(self._jedzenie): self._jedzenie,
            str(self._pozostale): self._pozostale,
        }
        self._mapping: dict[Any, Any] = {
            Bron: self._bronie,
            Pancerz: self._pancerze,
            Magia: self._przedmioty_magiczne,
            Pismo: self._pisma,
            Artefakt: self._artefakty,
            Jedzenie: self._jedzenie,
            Pozostale: self._pozostale,
        }

    # Czy to jest potrzebne?

    @property
    def bronie(self):
        return self._bronie

    @property
    def pancerze(self):
        return self._pancerze

    @property
    def przedmioty_magiczne(self):
        return self._przedmioty_magiczne

    @property
    def pisma(self):
        return self._pisma

    @property
    def artefakty(self):
        return self._artefakty

    @property
    def jedzenie(self):
        return self._jedzenie

    @property
    def pozostale(self):
        return self._pozostale

    @property
    def w_uzyciu(self):
        return self._w_uzyciu

    @property
    def magazyn(self):
        return self._magazyn

    # zmienna globalna - słownik zdefiniowany jako odrębna rzecz
    # czyli tak naprawdę mapping - mapuję isinstance danego rpzedmiotu z kontenerem - DONE

    # możliwe że wyjebać tę metodę

    def wyswietl_magazyn(self):
        """
        Metoda zwracająca kontener magazyn
        """
        return self.magazyn

    def wyswietl_w_uzyciu(self):
        """
        Metoda wyświetlająca przedmioty w użyciu
        """
        for k, v in self.w_uzyciu.items():
            for var in v:
                print(k, var.nazwa)

    def dodaj(self, przedmiot: Przedmiot):
        """
        Metoda dodaj dodaje przedmioty do danego kontenera w zależności od klasy

        :param przedmiot: obiekt klasy Przedmiot
        """

        for k in self._mapping:
            if isinstance(przedmiot, k):
                kontener = self._mapping[k]
                if przedmiot.nazwa not in kontener:
                    kontener.update({przedmiot.nazwa: [przedmiot]})
                else:
                    kontener[przedmiot.nazwa].append(przedmiot)
