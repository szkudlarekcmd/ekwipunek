"""
Moduł zawierający klasę GorniczaDolina
"""

from lokalizacje.lokalizacja import Lokalizacja
from przedmioty.bron import BronJednoreczna
from przedmioty.jedzenie import Jedzenie
from przedmioty.magia import Runa
from przedmioty.pancerz import Pancerz
from przedmioty.pismo import Pismo

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
                {"sila": 20},
                {"obrazenia": 50},
                2,
            ),
            BronJednoreczna(
                "Mieczyk z Gorniczej Doliny", 7, {"sila": 5}, {"obrazenia": 11}, 2
            ),
            BronJednoreczna(
                "Mieczyk z Gorniczej Doliny", 7, {"sila": 5}, {"obrazenia": 11}, 2
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
                {"sila": 0},
            ),
            Runa("Bryła lodu z Gorniczej Doliny", 700, 3, {"obrazenia": 3}, 50),
            Runa("Bryła lodu z Gorniczej Doliny 1", 700, 3, {"obrazenia": 3}, 50),
            Runa("Bryła lodu z Gorniczej Doliny 2", 700, 3, {"obrazenia": 3}, 50),
            Runa("Bryła lodu z Gorniczej Doliny 3", 700, 3, {"obrazenia": 3}, 50),
            Runa("Bryła lodu z Gorniczej Doliny 4", 700, 3, {"obrazenia": 3}, 50),
            Runa("Bryła lodu z Gorniczej Doliny 5", 700, 3, {"obrazenia": 3}, 50),
            Runa("Bryła lodu z Gorniczej Doliny 6", 700, 3, {"obrazenia": 3}, 50),
            Runa("Bryła lodu z Gorniczej Doliny 7", 700, 3, {"obrazenia": 3}, 50),
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
            Jedzenie("Gulasz Thekli", 1, {"sila": 1, "Smak": "Zajebisty", "hp": 20}),
            Jedzenie("Gulasz Thekli", 1, {"sila": 1, "Smak": "Zajebisty", "hp": 20}),
            Jedzenie("Jabłko", 1, {"sila": 100}),
            Jedzenie("Maliny", 1, {"zrecznosc": 100}),
        ]
