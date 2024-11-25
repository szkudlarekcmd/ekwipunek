"""
Moduł z klasą Bohater
"""

from clear import clear

from ekwipunek import Ekwipunek, Ekwipunek_Obiekt

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

    @property
    def hp(self):
        return self._hp

    @property
    def mana(self):
        return self._mana

    @property
    def sila(self):
        return self._sila

    @property
    def zrecznosc(self):
        return self._zrecznosc

    def podejrzyj(self, obiekt: "Khorinis"):
        """
        Metoda podejrzyj, za pomocą której Bohater dogląda przedmiotów znajdujących się
        w danej lokalizacji. Możemy zdecydować, czy podnieść wszystkie przedmioty, czy
        tylko te wybrane.
        """
        podejrzyj_liste = obiekt.spojrz().copy()
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

    def podnies(self, przedmiot):
        """
        Metoda podnieś, za pomocą której Bohater podnosi przedmioty.
        """
        Ekwipunek.dodaj(Ekwipunek_Obiekt, przedmiot)


# PRZYPAŁ Z CIRCULAR IMPORT : (
# zaproponowałbym przeniesienie tych dwóch metod do klasy ekwipunek
Bohater_Obiekt = Bohater(hp=10, mana=10, sila=0, zrecznosc=0)
