"""
Moduł z klasą Khorinis
"""

from lokalizacje.lokalizacja import Lokalizacja
from przedmioty.artefakt import Amulet, Artefakt
from przedmioty.bron import BronJednoreczna, Kusza, Luk
from przedmioty.jedzenie import Jedzenie
from przedmioty.magia import Runa, Zwoj
from przedmioty.pancerz import Pancerz
from przedmioty.pismo import Pismo
from przedmioty.pozostale import Pozostale

# pylint: disable = too-few-public-methods


class Khorinis(Lokalizacja):
    """
    Klasa Khorinis to zbiór wszystkich stworzonych obiektów typu Przedmiot w Khorinis.
    Posiada metodę spójrz.
    """

    def __init__(self):
        super().__init__()
        self.zawartosc: list = [
            BronJednoreczna("Szept Burzy", 1360, {"Siła": 20}, {"obrazenia": 50}, 2),
            BronJednoreczna("Szept Burzy", 1360, {"Siła": 20}, {"obrazenia": 50}, 2),
            BronJednoreczna("Szept Burzy", 1360, {"Siła": 20}, {"obrazenia": 50}, 2),
            BronJednoreczna("Kij z gwoździem", 7, {"Siła": 5}, {"obrazenia": 11}, 1),
            BronJednoreczna("Mieczyk", 7, {"Siła": 5}, {"obrazenia": 11}, 2),
            BronJednoreczna("Mieczyk", 7, {"Siła": 5}, {"obrazenia": 11}, 2),
            Luk("Zmyślony Łuk", 20, {"Zręczność": 20}, {"obrazenia": 100}),
            Kusza("Zmyślona Kusza", 30, {"Zręczność": 50}, {"obrazenia": 80}),
            Pancerz(
                "Zbroja strażnika",
                1650,
                {
                    "Ochrona przed bronią": 55,
                    "Ochrona przed strzałami": 10,
                    "Ochrona przed ogniem": 25,
                },
                {"Siła": 5},
            ),
            Pancerz(
                "Zbroja z pancerzy pełzaczy",
                2400,
                {
                    "Ochrona przed bronią": 80,
                    "Ochrona przed strzałami": 15,
                    "Ochrona przed ogniem": 30,
                    "Ochrona przed magia": 5,
                },
                {"Siła": 0},
            ),
            Runa(
                "Bryła lodu",
                700,
                10,
                {"Obrażenia": 50},
                3,
            ),
            Runa("Deszcz ognia", 1300, 100, {"Obrażenia": 15}, 5),
            Zwoj("Wymyślony Zwój", 20, 5, {"Leczenie": 15}),
            Pismo(
                "Dwór Irdorath",
                0,
                "Mam w dupie przeznaczenie.",
            ),
            Pismo(
                "Historia Jarkendaru",
                0,
                "Co robisz? Topisz złoto? Nie, siekam cebulkę.",
            ),
            Jedzenie("Gulasz Thekli", 1, {"sila": 1, "Smak": "Zajebisty", "hp": 20}),
            Jedzenie("Gulasz Thekli", 1, {"sila": 1, "Smak": "Zajebisty", "hp": 20}),
            Jedzenie("Zupa Rybna", 20, {"hp": 10}),
            Amulet("Oko Innosa", 0, ["Możliwość rozmowy ze smokami"]),
            Artefakt("Kamień ogniskujący", 0, None),
            Pozostale("Grabie", 0, None),
        ]
