"""
Moduł z klasą Bohater
"""

from ekwipunek import Ekwipunek
from przedmioty.przedmiot import Przedmiot
from clear import clear
from lokalizacje.lokalizacja import Lokalizacja

# pylint: disable=inconsistent-return-statements, missing-function-docstring


# TODO: bohater -> dorobic mu funkcjonalnosc - w jaki sposób?
class Bohater:
    """
    Nowopowstała klasa Bohater będąca pośrednikiem między Podłogą, a Ekwipunkiem,
    posiadająca metodę podejrzyj.
    """

    def __init__(
        self,
        hp: float,
        mana: float,
        sila: int,
        zrecznosc: int,
    ):
        self._hp = hp
        self._mana = mana
        self._sila = sila
        self._zrecznosc = zrecznosc
        self.aktualna_lokalizacja = None
        # nie lepiej, by metody bohatera były czymś na zasadzie type dicta lub dicta?
        self.ekwipunek = Ekwipunek(metody_bohatera=(self.uzyj, self.podnies, self.wyrzuc, self.zdejmij))

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp += value

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana += value

    @property
    def sila(self):
        return self._sila

    @sila.setter
    def sila(self, value):
        self._sila += value

    @property
    def zrecznosc(self):
        return self._zrecznosc

    @zrecznosc.setter
    def zrecznosc(self, value):
        self._zrecznosc += value

    def podejrzyj(self, obiekt: "Khorinis"):
        """
        Metoda podejrzyj, za pomocą której Bohater dogląda przedmiotów znajdujących się
        w danej lokalizacji. Możemy zdecydować, czy podnieść wszystkie przedmioty, czy
        tylko te wybrane.
        """
        podejrzyj_liste: list[str] = obiekt.spojrz().copy()
        while True:
            clear()
            for index, i in enumerate(podejrzyj_liste):
                print(index, i.nazwa)
            val: str | int = input(
                "Wpisz 'tak' by podnieść wszystkie przedmioty. Podaj ID przedmiotu, jeśli chcesz"
                " podnieść pojedynczy przedmiot."
            )
            if val == "tak":
                print("Podniesiono wszystkie przedmioty")
                for index, i in enumerate(podejrzyj_liste):
                    print(i.nazwa)
                    self.podnies(i)
                    obiekt.zawartosc.remove(i)
                podejrzyj_liste.clear()
            elif val == "exit":
                return 0
            if val.split(".")[0].isdigit():
                val = int(val.split(".")[0])
            else:
                continue
            if 0 <= val < len(podejrzyj_liste):
                przedmiocik = podejrzyj_liste.pop(val)
                print("Podniesiono " + przedmiocik.nazwa)
                self.podnies(przedmiocik)
                obiekt.zawartosc.remove(przedmiocik)
            else:
                print("Złe ID")
            if not podejrzyj_liste:
                print("\nW ekwipunku nic się nie znajduje. \n")
                break

    def podnies(self, przedmiot: Przedmiot):
        """
        Metoda podnieś, za pomocą której Bohater podnosi przedmioty.
        """
        self.ekwipunek.dodaj(przedmiot)
    def wyrzuc(self, przedmiot: Przedmiot):
        """
        Metoda wyrzuć, za pomocą której Bohater wyrzuca przedmiot.
        """
        self.ekwipunek.wyrzuc(przedmiot)

    def uzyj(self, przedmiot: Przedmiot):
        """
        Metoda użyj, za pomocą której Bohater używa przedmiotu
        """
        self.ekwipunek.uzyj(przedmiot)

    def zdejmij(self, przedmiot: Przedmiot):
        """
        Metoda zdejmij, za pomocą której Bohater zdejmuje przedmiot
        """
        self.ekwipunek.zdejmij(przedmiot)

    def zmien_lokalizacje(self, aktualna_lokalizacja: Lokalizacja):
        self.lokalizacja = aktualna_lokalizacja
        return self.lokalizacja
