"""
Moduł z klasą Bohater
"""


from ekwipunek import Ekwipunek
from przedmioty.jedzenie import Jedzenie
from przedmioty.magia import Magia, Zwoj
from przedmioty.pismo import Pismo
from przedmioty.pozostale import Pozostale
from przedmioty.przedmiot import Przedmiot
from clear import clear


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
        self.ekwipunek = Ekwipunek()


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


    def wyrzuc(self, item: Przedmiot):
        """
        Metoda wyrzuć wyrzucająca dany przedmiot z obiektu klasy Ekwipunek i zwracająca go
        do obiektu klasy lokalizacja.

        :param item: obiekt klasy Przedmiot
        :param lokalizacja: jest to lokalizacja, w ktorej uzytkownik obecnie sie znajduje,
            dla przykladu Khorinis lub Gornicza Dolina
        """

        # itertools,chain.from iterable
        # ujednolicenie wartości w użyciu -> Każdy z tych kontenerów ma zawierać w sobie
        # listę obiektów (nawet jeśli jest jeden), a nie sam obiekt
        # np żeby móc używać dwóch run naraz - bo przecież tak mozna - DONE
        # TODO: defaultdict, trochę potrzebuje przykładu
        # TO JEST DO ZROBIENIA...
        # powinienem móc odnieść się do konkretnego kontenera w uzyciu z racji mappingu powyzej
        # i wtedy interesuja nas przedmioty/przedmiot znajdujace sie tylko w tym danym kontenerze
        # optymalizacja - DONE!!!!!
        for _, v in self.ekwipunek.w_uzyciu.items():
            if item in v:
                print("\nNie można usunąć przedmiotu, który jest w użyciu!\n")
                return None
        for k in self.ekwipunek._mapping:
            if isinstance(item, k):
                kontener = self.ekwipunek._mapping[k]
                przedmioty = kontener[item.nazwa]
                if len(przedmioty) == 1:
                    del kontener[item.nazwa]
                return przedmioty.pop(0)

    def uzyj(self, item: Przedmiot):
        """
        Metoda użyj działa inaczej w zależności od klasy danego przedmiotu.
        Dla klasy Pismo:
            zwraca zawartość Pisma
        Dla klasy Jedzenie:
            zwraca efekt, jaki jedzenie spowodowało po spożyciu, a następnie
            usuwa obiekt z ekwipunku
        Dla klasy Zwój:
            informuje, iż zwój został zużyty, a następnie usuwa obiekt z ekwipunku
        Dla reszty klas:
            dodaje referencję z obiektu klasy Ekwipunek do kontenera w_uzyciu

        :param item: obiekt klasy Przedmiot
        :param lokalizacja: jest to lokalizacja, w ktorej uzytkownik obecnie sie znajduje,
            dla przykladu Khorinis lub Gornicza Dolina
        """
        if item.efekt:
            if isinstance(item, Pismo):
                clear()
                print(item.efekt)

            elif isinstance(item, Jedzenie):
                clear()
                print(item.efekt)
                for k, v in item.efekt.items():
                    if hasattr(self, k):
                        setattr(self, k, getattr(self, k) + v)



                self.ekwipunek._jedzenie[item.nazwa].remove(item)
                if len(self.ekwipunek._jedzenie[item.nazwa]) == 0:
                    del self.ekwipunek._jedzenie[item.nazwa]
            elif isinstance(item, Magia):
                if isinstance(item, Zwoj):
                    clear()
                    print("\nZwój został użyty!\n")
                    self.ekwipunek._przedmioty_magiczne[item.nazwa].remove(item)
                    if len(self.ekwipunek._przedmioty_magiczne[item.nazwa]) == 0:
                        del self.ekwipunek._przedmioty_magiczne[item.nazwa]
                else:
                    if type(item).__name__ not in self._w_uzyciu.keys():
                        clear()
                        self.ekwipunek._w_uzyciu.update({type(item).__name__: [item]})
                    else:
                        self.ekwipunek._w_uzyciu[type(item).__name__] += [item]
            elif isinstance(item, Pozostale):
                pass
            else:
                self.ekwipunek._w_uzyciu.update({type(item).__name__: [item]})
            clear()
            print("\nPrzedmiot został użyty!\n")
        else:
            clear()
            print("\nPrzedmiotu nie da się użyć!\n")

    def zdejmij(self, item: Przedmiot):
        """
        Metoda ściąga dany przedmiot z przedmiotów w użyciu.

        :param item: obiekt klasy Przedmiot
        :param lokalizacja: jest to lokalizacja, w ktorej uzytkownik obecnie sie znajduje,
            dla przykladu Khorinis lub Gornicza Dolina
        :param przedmioty_w_uzyciu: lista, w ktorej znajduja sie nazwy przedmiotow obecnie
            znajdujących się w użyciu
        """
        for key, value in self.ekwipunek.w_uzyciu.copy().items():
            #  RuntimeError: dictionary changed size during iteration, dlatego copy
            for i in value:
                if i == item:
                    self.ekwipunek.w_uzyciu[key].remove(item)
                    if len(value) == 0:
                        del self.ekwipunek.w_uzyciu[key]
        clear()
        print("\nPrzedmiot został zdjęty!\n")

    def zmien_lokalizacje(self, lokalizacja):
        return lokalizacja