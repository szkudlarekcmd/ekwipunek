"""
Moduł zawierający klasę GorniczaDolina
"""

from Lokalizacje.lokalizacja import Lokalizacja
from Przedmioty.bron import BronJednoreczna
from Przedmioty.jedzenie import Jedzenie
from Przedmioty.magia import Runa
from Przedmioty.pancerz import Pancerz
from Przedmioty.pismo import Pismo

# pylint: disable=too-few-public-methods


class GorniczaDolina(Lokalizacja):
    """
    Klasa GorniczaDolina to zbiór wszystkich stworzonych obiektów typu Przedmiot w Gorniczej
    Dolinie. Posiada metodę spójrz.
    """

    def __init__(self):
        super().__init__()
        self.zawartosc = [
            BronJednoreczna(
                "Szept Burzy z Gorniczej Doliny",
                1360,
                {"Siła": 20},
                {"obrazenia": 50},
                2,
            ),
            BronJednoreczna(
                "Mieczyk z Gorniczej Doliny", 7, {"Siła": 5}, {"obrazenia": 11}, 2
            ),
            BronJednoreczna(
                "Mieczyk z Gorniczej Doliny", 7, {"Siła": 5}, {"obrazenia": 11}, 2
            ),
            Pancerz(
                "Zbroja z pancerzy pełzaczy z Gorniczej Doliny",
                2400,
                {
                    "Ochrona przed bronią": 80,
                    "Ochrona przed strzałami": 15,
                    "Ochrona przed ogniem": 30,
                    "Ochrona przed magia": 5,
                },
                {"Siła": 0},
            ),
            Runa("Bryła lodu z Gorniczej Doliny", 700, 3, {"obrazenia": 3}, 50),
            Pismo(
                "Dwór Irdorath z Gorniczej Doliny",
                0,
                "Mam w dupie przeznaczenie.",
            ),
            Pismo(
                "Historia Jarkendaru z Gorniczej Doliny",
                0,
                "Co robisz? Topisz złoto? Nie, siekam cebulkę.",
            ),
            Jedzenie("Gulasz Thekli", 1, {"Siła": 1, "Smak": "Zajebisty", "HP": 20}),
            Jedzenie("Gulasz Thekli", 1, {"Siła": 1, "Smak": "Zajebisty", "HP": 20}),
        ]
