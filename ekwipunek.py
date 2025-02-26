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

    def __init__(self):
        self._bronie: Kontener = Bronie()
        self._pancerze: Kontener = Pancerze()
        self._przedmioty_magiczne: Kontener = PrzedmiotyMagiczne()
        self._pisma: Kontener = Pisma()
        self._artefakty: Kontener = Artefakty()
        self._jedzenie: Kontener = Zywnosc()
        self._pozostale: Kontener = Pozostalosci()
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
        for k, v in self.w_uzyciu.items():
            for var in v:
                print(k, var.nazwa)

    def dodaj(self, przedmiot: Przedmiot):
        """
        Metoda dodaj dodaje przedmioty do danego kontenera w zależności od klasy

        :param przedmiot: obiekt klasy Przedmiot
        """

        for k in self._mapping:
            if isinstance(przedmiot, k):
                kontener = self._mapping[k]
                if przedmiot.nazwa not in kontener:
                    kontener.update({przedmiot.nazwa: [przedmiot]})
                else:
                    kontener[przedmiot.nazwa].append(przedmiot)

    def interfejs(self, lokalizacja: Lokalizacja, obiekt_bohatera: "Bohater"):
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
            for value in self.wyswietl_magazyn().values():
                # k - Gulasz Thekli
                # v - [<__main__.Jedzenie object at 0x104360d60>,
                # <__main__.Jedzenie object at 0x104360dc0>]
                # tę całą pętlę wsadzić do podmetody - prywatnej
                for k, v in value.items():
                    # sprawdzam czy zbiory sie pokrywaja - jesli tak, to dany przedmiot jest
                    # w uzyciu
                    object_list = list(
                        chain.from_iterable(list(self.w_uzyciu.values()))
                    )
                    if len(self.w_uzyciu.values()) > 0 and bool(
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
                            item, lokalizacja, przedmiot, obiekt_bohatera
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
        obiekt_bohatera,
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
                    obiekt_bohatera.uzyj(item)
                    break
                if wybranie_przedmiotu == 1 and przedmiot in przedmioty_w_uzyciu:
                    obiekt_bohatera.zdejmij(item)
                    break
                if wybranie_przedmiotu == 2:
                    clear()
                    if obiekt_bohatera.wyrzuc(item) is None:
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
