"""
Moduł z klasą Bohater
"""

from ekwipunek import Ekwipunek
from przedmioty.przedmiot import Przedmiot
from clear import clear
from lokalizacje.lokalizacja import Lokalizacja

# pylint: disable=inconsistent-return-statements, missing-function-docstring
# pylint: disable=too-many-instance-attributes
# pylint: disable=not-callable


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
        self.aktualne_hp = hp
        self.aktualna_mana = mana
        # nie lepiej, by metody bohatera były czymś na zasadzie type dicta lub dicta?
        self.ekwipunek = Ekwipunek(
            metody_bohatera={
                "uzyj": self.uzyj,
                "podnies": self.podnies,
                "wyrzuc": self.wyrzuc,
                "zdejmij": self.zdejmij,
            }
        )
        self.aktualne_obrazenia = self.sila + self.zrecznosc

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

        :param obiekt: Obiekt, do którego chcemy podejrzeć :)
        """
        podejrzyj_liste: list[str] = obiekt.spojrz().copy()
        # podejrzyj_liste = self.aktualna_lokalizacja.spojrz.copy()
        while True:
            clear()
            for index, przedmiot in enumerate(podejrzyj_liste):
                print(index, przedmiot.nazwa)
            val: str | int = input(
                "Wpisz 'tak' by podnieść wszystkie przedmioty. Podaj ID przedmiotu, jeśli chcesz"
                " podnieść pojedynczy przedmiot."
            )
            if val == "tak":
                print("Podniesiono wszystkie przedmioty")
                for index, przedmiot in enumerate(podejrzyj_liste):
                    print(przedmiot.nazwa)
                    self.podnies(przedmiot)
                    obiekt.zawartosc.remove(przedmiot)
                podejrzyj_liste.clear()
            elif val == "exit":
                return
            # to jest akceptowanie float'a : )
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
                return

    def podnies(self, przedmiot: Przedmiot):
        """
        Metoda podnieś, za pomocą której Bohater podnosi przedmioty.

        :param przedmiot: Przedmiot do podniesienia
        """
        self.ekwipunek.dodaj(przedmiot)

    def wyrzuc(self, przedmiot: Przedmiot):
        """
        Metoda wyrzuć, za pomocą której Bohater wyrzuca przedmiot.

        :param wyrzuć: Przedmiot do wyrzucenia
        """
        self.ekwipunek.wyrzuc(przedmiot)
        self.aktualna_lokalizacja.zawartosc.append(przedmiot)

    def uzyj(self, przedmiot: Przedmiot):
        """
        Metoda użyj, za pomocą której Bohater używa przedmiotu oraz
        przypisuje aktualizuje swoje atrybuty

        :param przedmiot: Przedmiot do użycia
        """
        if hasattr(przedmiot, "wymagania"):
            for k, v in przedmiot.wymagania.items():
                if hasattr(self, k):
                    if getattr(self, k) < v:
                        return 1
        slownik_efektu = self.ekwipunek.uzyj(przedmiot)
        if isinstance(slownik_efektu, dict):
            for efekt, wartosc_efektu in slownik_efektu.items():
                if hasattr(self, efekt):
                    setattr(self, efekt, wartosc_efektu)
        else:
            return slownik_efektu

    def zdejmij(self, przedmiot: Przedmiot):
        """
        Metoda zdejmij, za pomocą której Bohater zdejmuje przedmiot

        :param przedmiot: Przedmiot do ściągnięcia
        """
        slownik_efektu = self.ekwipunek.zdejmij(przedmiot)
        if slownik_efektu is not None:
            for efekt, wartosc_efektu in slownik_efektu.items():
                if hasattr(self, efekt):
                    setattr(self, efekt, -wartosc_efektu)

    def zmien_lokalizacje(self, aktualna_lokalizacja: Lokalizacja):
        """
        Metoda do zmienienia lokalizacji

        :param aktualna_lokalizacja: aktualna lokalizacja
        """
        self.aktualna_lokalizacja = aktualna_lokalizacja

    def wyprintuj_swoje_atrybuty(self):
        """
        Metoda do wyprintowania swoich atrybutów
        """
        print("HP", self.hp)
        print("MANA", self.mana)
        print("SIŁA", self.sila)
        print("ZRĘCZNOŚĆ", self.zrecznosc)
        print("AKTUALNA LOKALIZACJA", self.aktualna_lokalizacja)
        print("AKTUALNE HP", self.aktualne_hp)
        print("AKTUALNA MANA", self.aktualna_mana)
        print("AKTUALNE OBRAZENIA", self.aktualne_obrazenia)
        print(
            "EFEKTY",
            [
                obiekt.efekt
                for obiekt_lista in self.ekwipunek.w_uzyciu.values()
                for obiekt in obiekt_lista
            ],
        )
