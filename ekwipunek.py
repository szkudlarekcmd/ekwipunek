"""
Moduł z klasą ekwipunek
"""

# pylint: disable=consider-using-dict-items, missing-function-docstring,
# pylint: disable=too-many-instance-attributes, inconsistent-return-statements)
from collections import defaultdict
from itertools import chain
from typing import Any

from kontenery.kontenery import (
    Artefakty,
    Bronie,
    Kontener,
    Pancerze,
    Pisma,
    Pozostalosci,
    PrzedmiotyMagiczne,
    Zywnosc,
)
from lokalizacje.lokalizacja import Lokalizacja
from przedmioty.artefakt import Artefakt
from przedmioty.bron import Bron
from przedmioty.jedzenie import Jedzenie
from przedmioty.magia import Magia, Zwoj
from przedmioty.pancerz import Pancerz
from przedmioty.pismo import Pismo
from przedmioty.pozostale import Pozostale
from przedmioty.przedmiot import Przedmiot
from clear import clear


class Ekwipunek:
    """
    Klasa Ekwipunek -> To w niej znajdują się przedmioty z Podłogi dodane za pomocą
    Bohatera. Tutaj również znajduje się kontener w uzyciu (nie wiem, czy słusznie).

    ...
    Atrybuty

    ----------
    bronie: Kontener
        kontener na przedmioty klasy Broń
    pancerze: Kontener
        kontener na przedmioty klasy Pancerz
    przedmioty magiczne: Kontener
        kontener na przedmioty klasy Magia
    pisma: Kontener
        kontener na przedmioty klasy Pismo
    artefakty: Kontener
        kontener na przedmioty klasy Artefakt
    jedzenie: Kontener
        kontener na przedmioty klasy Jedzenie
    pozostale: Kontener
        kontener na przedmioty klasy Pozostale
    w_uzyciu: Kontener
        kontener zawierający przedmioty znajdujące się w danej
        chwili w użyciu
    :param magazyn: słownik zawierający wszystkie kontenery przypisane
        do odpowiedniego klucza
    """

    def __init__(self, metody_bohatera):
        self._bronie: Kontener = Bronie()
        self._pancerze: Kontener = Pancerze()
        self._przedmioty_magiczne: Kontener = PrzedmiotyMagiczne()
        self._pisma: Kontener = Pisma()
        self._artefakty: Kontener = Artefakty()
        self._jedzenie: Kontener = Zywnosc()
        self._pozostale: Kontener = Pozostalosci()
        self.metody_bohatera = metody_bohatera
        # TODO: zamiast default dicta użyć dataclass (spróbuj), gdzie definuję
        # pola oraz ile może być przedmiotów. Zdefiniować to na sztywno
        # przełączyć na 3.13 sięęęe - 3.13 sprawia olbrzymie problemy z tym pycharmem
        # więc na ten moment go odpuszczam : - )

        self._w_uzyciu = defaultdict(list)  # eee do ogarnięcia (?)
        self._magazyn: dict[str, Kontener] = {
            str(self._bronie): self._bronie,
            str(self._pancerze): self._pancerze,
            str(self._przedmioty_magiczne): self._przedmioty_magiczne,
            str(self._pisma): self._pisma,
            str(self._artefakty): self._artefakty,
            str(self._jedzenie): self._jedzenie,
            str(self._pozostale): self._pozostale,
        }
        self._mapping: dict[Any, Any] = {
            Bron: self._bronie,
            Pancerz: self._pancerze,
            Magia: self._przedmioty_magiczne,
            Pismo: self._pisma,
            Artefakt: self._artefakty,
            Jedzenie: self._jedzenie,
            Pozostale: self._pozostale,
        }
        # mapping istnieje ze względu na konwencję kontenerów z małej litery
        # oraz nazw klas z dużej.

    # Czy to jest potrzebne?

    @property
    def bronie(self):
        return self._bronie

    @property
    def pancerze(self):
        return self._pancerze

    @property
    def przedmioty_magiczne(self):
        return self._przedmioty_magiczne

    @property
    def pisma(self):
        return self._pisma

    @property
    def artefakty(self):
        return self._artefakty

    @property
    def jedzenie(self):
        return self._jedzenie

    @property
    def pozostale(self):
        return self._pozostale

    @property
    def w_uzyciu(self):
        return self._w_uzyciu

    @property
    def magazyn(self):
        return self._magazyn

    # zmienna globalna - słownik zdefiniowany jako odrębna rzecz
    # czyli tak naprawdę mapping - mapuję isinstance danego rpzedmiotu z kontenerem - DONE

    # możliwe że wyjebać tę metodę

    def wyswietl_magazyn(self):
        """
        Metoda zwracająca kontener magazyn
        """
        return self.magazyn

    def wyswietl_w_uzyciu(self):
        """
        Metoda wyświetlająca przedmioty w użyciu
        """
        for typ, lista_przedmiotów in self.w_uzyciu.items():
            for przedmiot in lista_przedmiotów:
                print(typ, przedmiot.nazwa)

    def dodaj(self, przedmiot: Przedmiot):
        """
        Metoda dodaj dodaje przedmioty do danego kontenera w zależności od klasy

        :param przedmiot: obiekt klasy Przedmiot
        """

        for klasa in self._mapping:
            if isinstance(przedmiot, klasa):
                kontener = self._mapping[klasa]
                if przedmiot.nazwa not in kontener:
                    kontener.update({przedmiot.nazwa: [przedmiot]})
                else:
                    kontener[przedmiot.nazwa].append(przedmiot)
                break

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
        for typ, lista_przedmiotów in self.w_uzyciu.items():
            if item in lista_przedmiotów:
                print("\nNie można usunąć przedmiotu, który jest w użyciu!\n")
                return None
        for klasa in self._mapping:
            if isinstance(item, klasa):
                kontener = self._mapping[klasa]
                przedmioty = kontener[item.nazwa]
                do_wyjebania = przedmioty.pop(0)
                if not przedmioty:
                    del kontener[item.nazwa]
                return do_wyjebania

    def _wyjeb_po_zjedzeniu(self, item: Przedmiot):
        """
        Wyjebuje po jedzeniu

        :param item: Przedmiocik
        """
        self._jedzenie[item.nazwa].remove(item)
        if not self._jedzenie[item.nazwa]:
            del self._jedzenie[item.nazwa]


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
                print("Przyznano" + item.efekt)
                return item.efekt
            elif isinstance(item, Jedzenie):
                clear()
                print(item.efekt)
                self._wyjeb_po_zjedzeniu(item)
                return item.efekt
            elif isinstance(item, Magia):
                if isinstance(item, Zwoj):
                    clear()
                    print("\nZwój został użyty!\n")
                    self._przedmioty_magiczne[item.nazwa].remove(item)
                    if len(self._przedmioty_magiczne[item.nazwa]) == 0:
                        del self._przedmioty_magiczne[item.nazwa]
                else:
                    if type(item).__name__ not in self._w_uzyciu:
                        clear()
                        self._w_uzyciu.update({type(item).__name__: [item]})
                    else:
                        self._w_uzyciu[type(item).__name__] += [item]
            elif isinstance(item, Pozostale):
                pass
            else:
                self._w_uzyciu.update({type(item).__name__: [item]})
                clear()
            # clear()
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
        to_remove_key = None
        for typ_przedmiotu, przedmioty in self.w_uzyciu.copy().items():
            #  RuntimeError: dictionary changed size during iteration, dlatego copy
            for przedmiot in przedmioty:
                if przedmiot == item:
                    to_remove_key = typ_przedmiotu
                    break
            if to_remove_key:
                self.w_uzyciu[to_remove_key].remove(item)
                if not self.w_uzyciu[to_remove_key]:
                    del self.w_uzyciu[to_remove_key]

    def interfejs(self, lokalizacja: Lokalizacja):
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
            for kontener in self.wyswietl_magazyn().values():
                # k - Gulasz Thekli
                # v - [<__main__.Jedzenie object at 0x104360d60>,
                # <__main__.Jedzenie object at 0x104360dc0>]
                # tę całą pętlę wsadzić do podmetody - prywatnej
                for nazwa_przedmiotów, przedmioty in kontener.items():
                    # sprawdzam czy zbiory sie pokrywaja - jesli tak, to dany przedmiot jest
                    # w uzyciu
                    object_list = list(
                        chain.from_iterable(list(self.w_uzyciu.values()))
                    )
                    if len(self.w_uzyciu.values()) > 0 and bool(
                        set(przedmioty) & set(object_list)
                    ):
                        print(
                            f"{identifier} * " + nazwa_przedmiotów + "    #" + " sztuk " + str(len(przedmioty))
                        )
                        slownik_interfejsu[identifier] = nazwa_przedmiotów
                        identifier += 1
                    # sprawdzam, czy dany przedmiot można użyć
                    elif przedmioty[0].efekt:
                        print(f"{identifier} " + nazwa_przedmiotów + "   #" + " sztuk " + str(len(przedmioty)))
                        slownik_interfejsu[identifier] = nazwa_przedmiotów
                        identifier += 1
                    else:
                        print(f"{identifier} " + nazwa_przedmiotów + " sztuk " + str(len(przedmioty)))
                        slownik_interfejsu[identifier] = nazwa_przedmiotów
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

                for kontener, przedmioty in self.wyswietl_magazyn().items():
                    # slownik_interfejsu[int(ID_przedmiotu)] = 'Szept Burzy'

                    # TODO: DODAĆ OBSŁUGĘ FLOAT'A - po co?

                    if (
                        przedmiot := slownik_interfejsu[
                            int(identifier_przedmiotu)
                        ]  # nazwa przedmiotu
                    ) in przedmioty:
                        # item = <__main__.BronJednoreczna object at 0x1025a8b80>
                        item: Przedmiot = self.wyswietl_magazyn()[kontener][
                            przedmiot
                        ][0]

                        # TODO: zmienna uzywane, ktora przechowuje informacje czy przedmiot jest w
                        # uzyciu czy nie - do przegadania czy jest to potrzebne.

                        # od tego momentu powinienem wyeksportowac wszystko co jest dalej
                        # do innej funkcji(sprawdzic czy tam byloby GIT) - DONE
                        self.podinterfejs(
                            item, lokalizacja, przedmiot,
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
            for nazwa_obj in self.w_uzyciu.values()
            for obj in nazwa_obj
        ]
        clear()
        print(f"Wybrany przedmiot:\n{item.nazwa}")
        # wyprintowanie statystyk
        for _naostrzony, czy_naostrzony in item.__dict__.items():
            if _naostrzony != "_nazwa":
                print(_naostrzony.split("_")[1], czy_naostrzony)
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
                    self.metody_bohatera[0](item)
                    break
                if wybranie_przedmiotu == 1 and przedmiot in przedmioty_w_uzyciu:
                    self.metody_bohatera[3](item)
                    clear() # pod indexem 0
                    print("\nPrzedmiot został zdjęty!\n")
                    break
                if wybranie_przedmiotu == 2:
                    clear()
                    if self.metody_bohatera[2](item) is None: # pod indexem 0 is None:
                        break
                    lokalizacja.zawartosc.append(item)
                    print("\nPrzedmiot został wyrzucony!16")
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
