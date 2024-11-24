from Lokalizacje.lokalizacja import Lokalizacja
from Przedmioty.bron import BronJednoreczna
from Przedmioty.jedzenie import Jedzenie
from Przedmioty.magia import Runa
from Przedmioty.pancerz import Pancerz
from Przedmioty.pismo import Pismo


class Jarkendar(Lokalizacja):
    """
    Klasa Jarkendar to zbiór wszystkich stworzonych obiektów typu Przedmiot w Jarkendarze.
    """

    def __init__(self):
        self.zawartosc = [
            BronJednoreczna(
                "Jaszczurzy miecz", 1360, {"Siła": 40}, {"obrazenia": 100}, 3
            ),
            BronJednoreczna(
                "Miecz z Jarkendaru", 25, {"Siła": 15}, {"obrazenia": 40}, 3
            ),
            BronJednoreczna(
                "Miecz z Jarkendaru", 25, {"Siła": 15}, {"obrazenia": 40}, 3
            ),
            Pancerz(
                "Zbroja z Jaszczura",
                3000,
                {
                    "Ochrona przed bronią": 40,
                    "Ochrona przed strzałami": 25,
                    "Ochrona przed ogniem": 35,
                    "Ochrona przed magia": 15,
                },
                {"Siła": 15},
            ),
            Runa(
                "Bryła lodu z Jarkendaru", 700, 50, {"obrazenia": 10}, 3, {"Siła": 30}
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
            Jedzenie("Gulasz Thekli", 1, {"Siła": 1, "Smak": "Zajebisty", "HP": 20}),
            Jedzenie("Gulasz Thekli", 1, {"Siła": 1, "Smak": "Zajebisty", "HP": 20}),
        ]


Jarkendar_Obiekt = Jarkendar()
