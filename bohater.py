"""
Moduł z klasą Bohater
"""

from itertools import chain
from typing import Any

from Lokalizacje.lokalizacja import Lokalizacja
from Przedmioty.jedzenie import Jedzenie
from Przedmioty.magia import Magia, Zwoj
from Przedmioty.pismo import Pismo
from Przedmioty.pozostale import Pozostale
from Przedmioty.przedmiot import Przedmiot
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

    def podejrzyj(self, obiekt: "Khorinis", obiekt_ekwipunku: "Ekwipunek"):
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
                    self.podnies(i, obiekt_ekwipunku)
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
                self.podnies(przedmiocik, obiekt_ekwipunku)
                obiekt.zawartosc.remove(przedmiocik)
            else:
                print("Złe ID")
            if not podejrzyj_liste:
                print("\nW ekwipunku nic się nie znajduje. \n")
                break

    def podnies(self, przedmiot: Przedmiot, obiekt_ekwipunku: "Ekwipunek"):
        """
        Metoda podnieś, za pomocą której Bohater podnosi przedmioty.
        """
        obiekt_ekwipunku.dodaj(przedmiot)

    def interfejs(self, lokalizacja: Lokalizacja, obiekt_ekwipunku: "Ekwipunek"):
        """
        Metoda interfejs, która odpowiada za interfejs ekwipunku. Wyświetla ona wszystkie
        przedmioty w ekwipunku, informuje użytkownika który przedmiot jest w użyciu, umożliwia
        przeprowadzenie takich operacji jak wybranie danego przedmiotu, założenie/ściągnięcie go,
        wyrzucenie go lub tez wybranie innego przedmiotu.

        :param lokalizacja: jest to lokalizacja, w ktorej uzytkownik obecnie sie znajduje,
            dla przykladu Khorinis lub Gornicza Dolina

        """
        slownik_interfejsu: dict[int, str] = {}
        print(
            "Jeśli dany przedmiot można użyć, to przy jego ilości sztuk pojawi się kratka."
            "\nJeśli dany przedmiot znajduje się w użyciu, to znajduje sie przy nim gwiazdka. "
            "\n"
        )
        while True:
            lokalizacja: Lokalizacja = lokalizacja
            identifier: int = 0
            # slownik interfejsu zdefiniowac tylko raz - tak jak wczesniej robilismy
            # i zrobic renderowanie tylko w petli - imo DONE
            # key - Bronie
            # value - {'Szept Burzy z Gorniczej Doliny':
            # [<__main__.BronJednoreczna object at 0x104360b80>],
            # 'Mieczyk z Gorniczej Doliny': [<__main__.BronJednoreczna object at 0x104360bb0>]}
            for value in obiekt_ekwipunku.wyswietl_magazyn().values():
                # k - Gulasz Thekli
                # v - [<__main__.Jedzenie object at 0x104360d60>,
                # <__main__.Jedzenie object at 0x104360dc0>]
                # tę całą pętlę wsadzić do podmetody - prywatnej
                for k, v in value.items():
                    # sprawdzam czy zbiory sie pokrywaja - jesli tak, to dany przedmiot jest
                    # w uzyciu
                    object_list = list(
                        chain.from_iterable(list(obiekt_ekwipunku.w_uzyciu.values()))
                    )
                    if len(obiekt_ekwipunku.w_uzyciu.values()) > 0 and bool(
                        set(v) & set(object_list)
                    ):
                        print(
                            f"{identifier} * " + k + "    #" + " sztuk " + str(len(v))
                        )
                        slownik_interfejsu[identifier] = k
                        identifier += 1
                    # sprawdzam, czy dany przedmiot można użyć
                    elif v[0].efekt:
                        print(f"{identifier} " + k + "   #" + " sztuk " + str(len(v)))
                        slownik_interfejsu[identifier] = k
                        identifier += 1
                    else:
                        print(f"{identifier} " + k + " sztuk " + str(len(v)))
                        slownik_interfejsu[identifier] = k
                        identifier += 1
            identifier_przedmiotu = input(
                "Podaj ID przedmiotu, ktory chcesz wybrać, lub wpisz 'exit', by wyjść: "
            )
            if identifier_przedmiotu == "exit":
                clear()
                break
            try:
                # kontener = 'Bronie'
                # przedmioty = {'Szept Burzy':
                # [<__main__.BronJednoreczna object at 0x10233c550>,
                # <__main__.BronJednoreczna object at 0x10233c580>,
                # <__main__.BronJednoreczna object at 0x10233c5b0>],
                # 'Kij z gwoździem': [<__main__.BronJednoreczna object at 0x10233c5e0>],
                # 'Zmyślony Łuk': [<__main__.Luk object at 0x10233c610>],
                # 'Zmyślona Kusza': [<__main__.Kusza object at 0x10233c640>]}

                # TODO: Walidacje robić przed - tzn sprawdzenie - nie muszę
                # iterować następny raz po wyswietl_magazyn().items()
                # TUTAJ prosiłbym o konkret

                for kontener, przedmioty in obiekt_ekwipunku.wyswietl_magazyn().items():
                    # slownik_interfejsu[int(ID_przedmiotu)] = 'Szept Burzy'

                    # TODO: DODAĆ OBSŁUGĘ FLOAT'A - po co?

                    if (
                        przedmiot := slownik_interfejsu[
                            int(identifier_przedmiotu)
                        ]  # nazwa przedmiotu
                    ) in przedmioty:
                        # item = <__main__.BronJednoreczna object at 0x1025a8b80>
                        item: Przedmiot = obiekt_ekwipunku.wyswietl_magazyn()[kontener][
                            przedmiot
                        ][0]

                        # TODO: zmienna uzywane, ktora przechowuje informacje czy przedmiot jest w
                        # uzyciu czy nie - do przegadania czy jest to potrzebne.

                        # od tego momentu powinienem wyeksportowac wszystko co jest dalej
                        # do innej funkcji(sprawdzic czy tam byloby GIT) - DONE
                        self.podinterfejs(
                            item, lokalizacja, przedmiot, obiekt_ekwipunku
                        )
            except KeyError:
                clear()
                print("\nDanego przedmiotu nie ma w ekwipunku.\n")
            except ValueError:
                clear()
                print("\nDanego przedmiotu nie ma w ekwipunku.\n")

    def podinterfejs(
        self,
        item: Przedmiot,
        lokalizacja: Lokalizacja,
        przedmiot: str,
        obiekt_ekwipunku: "Ekwipunek",
    ):
        """
        Metoda podinterfejs odpowiadająca za podinterfejs ekwipunku - tutaj dzieją
        sie wszystkie rzeczy po "wybraniu" przedmiotu.

        :param item
        :param lokalizacja
        :param przedmiot
        """

        przedmioty_w_uzyciu: list[str, Any] = [
            obj.nazwa
            for nazwa_obj in obiekt_ekwipunku.w_uzyciu.values()
            for obj in nazwa_obj
        ]
        clear()
        print(f"Wybrany przedmiot:\n{item.nazwa}")
        # wyprintowanie statystyk
        for kk, vv in item.__dict__.items():
            if kk != "_nazwa":
                print(kk.split("_")[1], vv)
        # wybranie przedmiotu
        prompt = (
            "Co chcesz zrobić z danym przedmiotem?"
            "\n1. {warunek} \n2. Wyrzuć\n3. Wybierz inny przedmiot"
        )
        while True:
            try:
                if przedmiot not in przedmioty_w_uzyciu:
                    wybranie_przedmiotu: input = int(
                        input(prompt.format(warunek="Użyj"))
                    )
                else:
                    wybranie_przedmiotu: input = int(
                        input(prompt.format(warunek="Zdejmij"))
                    )
                if wybranie_przedmiotu == 1 and przedmiot not in przedmioty_w_uzyciu:
                    self.uzyj(item, obiekt_ekwipunku)
                    break
                if wybranie_przedmiotu == 1 and przedmiot in przedmioty_w_uzyciu:
                    self.zdejmij(item, obiekt_ekwipunku)
                    break
                if wybranie_przedmiotu == 2:
                    clear()
                    if self.wyrzuc(item, obiekt_ekwipunku) is None:
                        break
                    lokalizacja.zawartosc.append(item)
                    break
                if wybranie_przedmiotu == 3:
                    clear()
                    print("\nPrzedmiot został odłożony, wybierz inny\n")
                    break
                clear()
                print("Nie wpisano 1, 2, 3")
                break
            except ValueError:
                clear()
                print("Nie wpisano 1, 2, 3")
                break

    def wyrzuc(self, item: Przedmiot, obiekt_ekwipunku: "Ekwipunek"):
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
        for _, v in obiekt_ekwipunku.w_uzyciu.items():
            if item in v:
                print("\nNie można usunąć przedmiotu, który jest w użyciu!\n")
                return None
        for k in obiekt_ekwipunku._mapping:
            if isinstance(item, k):
                kontener = obiekt_ekwipunku._mapping[k]
                przedmioty = kontener[item.nazwa]
                if len(przedmioty) == 1:
                    del kontener[item.nazwa]
                return przedmioty.pop(0)

    def uzyj(self, item: Przedmiot, obiekt_ekwipunku: "Ekwipunek"):
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
                # w takim wypadku dobrym pomysłem byłoby zdefiniować jakies
                # statystyki bohatera - typu HP, mana, sila etc.
                # to by powodowalo ze bysmy po pierwsze walidowali te pola
                # i na przyklad danego przedmiotu nie daloby sie uzyc
                # oraz zwiekszali/zmiejszali statystki bohatera na podstawie
                # przedmiotow

                obiekt_ekwipunku._jedzenie[item.nazwa].remove(item)
                if len(obiekt_ekwipunku._jedzenie[item.nazwa]) == 0:
                    del obiekt_ekwipunku._jedzenie[item.nazwa]
            elif isinstance(item, Magia):
                if isinstance(item, Zwoj):
                    clear()
                    print("\nZwój został użyty!\n")
                    obiekt_ekwipunku._przedmioty_magiczne[item.nazwa].remove(item)
                    if len(obiekt_ekwipunku._przedmioty_magiczne[item.nazwa]) == 0:
                        del obiekt_ekwipunku._przedmioty_magiczne[item.nazwa]
                else:
                    if type(item).__name__ not in self._w_uzyciu.keys():
                        clear()
                        obiekt_ekwipunku._w_uzyciu.update({type(item).__name__: [item]})
                    else:
                        obiekt_ekwipunku._w_uzyciu[type(item).__name__] += [item]
            elif isinstance(item, Pozostale):
                pass
            else:
                obiekt_ekwipunku._w_uzyciu.update({type(item).__name__: [item]})
            clear()
            print("\nPrzedmiot został użyty!\n")
        else:
            clear()
            print("\nPrzedmiotu nie da się użyć!\n")

    def zdejmij(self, item: Przedmiot, obiekt_ekwipunku: "Ekwipunek"):

        # teoretycznie ta funkcja powinna przyjmować tylko JEDEN argument - i jest to item
        # DONE
        """
        Metoda ściąga dany przedmiot z przedmiotów w użyciu.

        :param item: obiekt klasy Przedmiot
        :param lokalizacja: jest to lokalizacja, w ktorej uzytkownik obecnie sie znajduje,
            dla przykladu Khorinis lub Gornicza Dolina
        :param przedmioty_w_uzyciu: lista, w ktorej znajduja sie nazwy przedmiotow obecnie
            znajdujących się w użyciu
        """
        for key, value in obiekt_ekwipunku.w_uzyciu.copy().items():
            #  RuntimeError: dictionary changed size during iteration, dlatego copy
            for i in value:
                if i == item:
                    obiekt_ekwipunku.w_uzyciu[key].remove(item)
                    if len(value) == 0:
                        del obiekt_ekwipunku.w_uzyciu[key]
        clear()
        print("\nPrzedmiot został zdjęty!\n")
