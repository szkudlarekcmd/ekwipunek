"""
Moduł jarkendar zawierający klasę Jarkendar
"""

from lokalizacje.lokalizacja import Lokalizacja
from przedmioty.bron import BronJednoreczna
from przedmioty.jedzenie import Jedzenie
from przedmioty.magia import Runa
from przedmioty.pancerz import Pancerz
from przedmioty.pismo import Pismo


# pylint: disable=too-few-public-methods


class Jarkendar(Lokalizacja):
    """
    Klasa Jarkendar to zbiór wszystkich stworzonych obiektów typu Przedmiot w Jarkendarze.
    """

    def __init__(self):
        super().__init__()
        self.zawartosc = [
            BronJednoreczna(
                "Jaszczurzy miecz", 1360, {"sila": 40}, {"obrazenia": 100}, 3
            ),
            BronJednoreczna(
                "Miecz z Jarkendaru", 25, {"sila": 15}, {"obrazenia": 40}, 3
            ),
            BronJednoreczna(
                "Miecz z Jarkendaru", 25, {"sila": 15}, {"obrazenia": 40}, 3
            ),
            BronJednoreczna("BronDodajacaHpIChuj", 25, {"sila": 1}, {"hp": 20}, 3),
            Pancerz(
                "Zbroja z Jaszczura",
                3000,
                {
                    "Ochrona przed bronią": 40,
                    "Ochrona przed strzałami": 25,
                    "Ochrona przed ogniem": 35,
                    "Ochrona przed magia": 15,
                },
                {"sila": 15},
            ),
            Runa(
                "Bryła lodu z Jarkendaru", 700, 50, {"obrazenia": 10}, 3, {"sila": 30}
            ),
            Pismo(
                "Dwór Irdorath z Jarkendaru",
                0,
                "Mam w dupie przeznaczenie.",
            ),
            Pismo(
                "Historia Jarkendaru z Jarkendaru",
                0,
                "Co robisz? Topisz złoto? Nie, siekam cebulkę.",
            ),
            Jedzenie("Gulasz Thekli", 1, {"sila": 1, "smak": "Zajebisty", "hp": 20}),
            Jedzenie("Gulasz Thekli", 1, {"sila": 1, "smak": "Zajebisty", "hp": 20}),
            Jedzenie("Jabłko", 1, {"sila": 100}),
            Jedzenie("Maliny", 1, {"zrecznosc": 100}),
        ]
