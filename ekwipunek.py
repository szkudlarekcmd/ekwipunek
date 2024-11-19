"""
Konwencja -> Koncept jest taki, że w kodzie polskich znaków nie ma oprócz stringów.
Wszystko w pierdolnikach jest oficjalne
"""

import platform
from abc import ABC
from collections import defaultdict
from typing import Any
import os
from itertools import chain
from typed_dicts import *

# pylint: disable=missing-function-docstring, too-many-arguments, unnecessary-pass
# pylint: disable=too-many-positional-arguments
# pylint: disable=too-few-public-methods, protected-access, too-many-branches
# pylint: disable=too-many-nested-blocks, too-many-instance-attributes
# pylint: disable=useless-parent-delegation, too-many-lines, too-many-locals
# pylint: disable=too-many-statements, inconsistent-return-statements
# podziel cały ekwipunek na podpliki, podziel klasy gdzie trzeba
# wydziel plik ekwipunek
# wydziel plik bohater
# w mainie TYLKO pętla główna.


def clear():
    """
    Czyści terminal.
    (emulate terminal in output console)
    """
    if platform.system() == "Windows":
        return os.system("cls")
    else:
        return os.system("clear")


class Przedmiot(ABC):
    """
    Base klasa, abstrakcyjna.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    """

    def __init__(self, nazwa: str, wartosc: int, efekt: dict[str, Any] | None):
        self._nazwa = nazwa
        self._wartosc = wartosc
        self._efekt = efekt

    @property
    def nazwa(self):
        return self._nazwa

    @property
    def wartosc(self):
        return self._wartosc

    @property
    def efekt(self):
        return self._efekt


class Bron(Przedmiot):
    """
    Klasa broni.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param wymagania: wymagane atrybuty do użycia danego przedmiotu
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    :param zasieg: zasieg broni
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        wymagania: dict[str, int],
        efekt: BronEfekt,
        zasieg: int | None = None,
    ):
        super().__init__(nazwa, wartosc, efekt)
        self._wymagania = wymagania
        self._zasieg = zasieg

    @property
    def wymagania(self):
        return self._wymagania

    @property
    def zasieg(self):
        return self._zasieg


class BronBiala(Bron):
    """
    Klasa broni białej.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param wymagania: wymagane atrybuty do użycia danego przedmiotu
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    :param zasieg: zasieg broni
    :param naostrzony: informuje, czy dany przedmiot zostal naostrzony
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        wymagania: dict[str, int],
        efekt: dict[str, int],
        # każdy obiekt powinien posiadać własny, niekoniecznie unikalny
        # zasięg, czyli lepiej nie traktować tego jako default
        # można obsłużyć default - None -> dla broni zasięgowej
        # jeśli None to zasięg bbbb duży - DONE
        zasieg: int,
        naostrzony: bool = False,
    ):
        super().__init__(nazwa, wartosc, wymagania, efekt, zasieg)
        self._naostrzony = naostrzony

    @property
    def naostrzony(self):
        return self._naostrzony


class BronDystansowa(Bron):
    """
    Klasa broni dystansowej.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param wymagania: wymagane atrybuty do użycia danego przedmiotu
    :param zasieg: zasieg broni
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        wymagania: dict[str, int],
        efekt: dict[str, int],
        zasieg: int | None = None,
    ):
        super().__init__(nazwa, wartosc, wymagania, efekt, zasieg)


class Luk(BronDystansowa):
    """
    Klasa Łuk -> nie dzieje się tu zbyt wiele.
    """

    pass


class Kusza(BronDystansowa):
    """
    Klasa Kusza -> nie dzieje się tu zbyt wiele.
    """

    pass


class BronJednoreczna(BronBiala):
    """
    Klasa Broń Jednoręczna -> nie dzieje się tu zbyt wiele.
    """

    pass


class BronDwureczna(BronBiala):
    """
    Klasa Broń Dwuręczna - nie dzieje się tu zbyt wiele.
    """

    pass


class Pancerz(Przedmiot):
    """
    Klasa pancerzy.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param ochrona: ochrona przed bronią
    :param wymagania: wymagane atrybuty do użycia danego przedmiotu
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        # pole efekt nie musi być tylko ochroną... może być to bonus
        # w postaci many
        # pomysł - zmergować pola ochrona oraz efekt (?) - Done
        efekt: PancerzEfekt | dict[str, Any],
        wymagania: dict[str, int] | None = None,
    ):
        super().__init__(nazwa, wartosc, efekt)
        self._wymagania = wymagania

    @property
    def wymagania(self):
        return self._wymagania


class Magia(Przedmiot):
    """
    Klasa Magii.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param mana: koszt many
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        mana: int,
        efekt: dict[str, Any],
        wymagania: dict[str, int] | None = None,
    ):
        def_dict: dict[str, Any] = {"Koszt many": mana}
        super().__init__(nazwa, wartosc, efekt)
        self._wymagania = wymagania
        # nie warunkować w ten sposób wymagań - a co jeśli zrobię else?
        # wymagania zrobić jako default pole, w którym ZAWSZE przechowywany jest koszt many
        # ale mogą być dodane dodatkowe parametry w postaci ni etylko kosztu many, ale też np
        # punkty życia - DONE
        if wymagania is None:
            self._wymagania = def_dict
        else:
            self._wymagania.update(def_dict)
        # self._wymagania.update(wymagania)
        # typed dict
        # mozna usunac pole mana z 259 i tylko zostawic je w wymaganiach - DONE

    @property
    def wymagania(self):
        return self._wymagania

    @property
    def mana(self):
        return self._wymagania["Koszt many"]


class Zwoj(Magia):
    """
    Klasa Zwój dziedzicząca z klasy Magia.
    """

    pass


class Runa(Magia):
    """
    Klasa Runa dziedzicząca z klasy Magia.

    :param krag: wymagany krąg magii, znajduje się on wtedy gdy mamy do
    czynienia z runą i jest to jedyny sposób na ich rozróżnienie
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        mana: int,
        efekt: dict[str, Any],
        # krąg mozna zastąpić wymaganiami lub dodawać krąg do wymagań
        # w ten sam sposób, w którym robiliśmy z maną
        # OVERALL -> zostajemy przy konwencji, że wymagania są z definicji None
        # a później bezpośrednio w klasie nadpisujemy je jako dict, w którym jest mana oraz krąg
        # natomiast jeśli przy tworzeniu obiektu my zdefiniujemy wymagania, to mamy dodatkowy
        # klucz w tymże dictie - imo DONE.
        krag: int,
        wymagania: dict[str, Any] | None = None,
    ):
        def_dict: dict[str, Any] = {"Koszt many": mana, "Krąg": krag}
        super().__init__(nazwa, wartosc, mana, efekt)
        self._wymagania = wymagania
        if wymagania is None:
            self._wymagania = def_dict
        else:
            self._wymagania.update(def_dict)

    @property
    def krag(self):
        return self._wymagania["Krąg"]


class Pismo(Przedmiot):
    """
    Klasa Pism - wyjątkowa klasa, ponieważ pisma nie można "ubrać". Użycie danej pozycji powoduje
    wyprintowanie treści do konsoli.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param tresc: treść danego pisma
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        tresc: str,
        efekt: dict[str, int] | None | str = None,
        # można dodać opcjonalnie wymagania
        # czy warto przechowywać pole treść w osobnym polu?
        # można wyciągać go ze słownika efekt - teoretycznie tak, ale czy powinniśmy iść tą drogą
        # generalnie z mojego punktu widzenia najlepiej by było, by efekt defaultowo był None,
        # a dopiero wewnątrz innita nadpisywali jego wartość poprzez to, co podajemy w treści.
        # Efekt nie NONE, gdy na przykład po przeczytaniu czegoś dostajemy jakieś bonusy. I tak dalej.
    ):
        self._tresc = tresc
        if efekt is None:
            efekt = {"Treść": tresc}
        super().__init__(nazwa, wartosc, efekt)

    @property
    def tresc(self):
        return self._tresc


class Jedzenie(Przedmiot):
    """
    Klasa Jedzenie - Kolejna klasa, której nie da się ubrać. Użycie danej pozycji powoduje
    jej zjedzenie, przez co pozycja zmniejsza swoją ilość w ekwipunku o jeden, lub znika z
    ekwipunku.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        efekt: dict[str, int],
    ):
        super().__init__(nazwa, wartosc, efekt)


class Artefakt(Przedmiot):
    """
    Klasa artefakty.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    """

    # dodaj wymagania tu :)
    # dodaj pasy
    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        efekt: dict[str, int] | None | list,
        wymagania: dict[str, Any] | None = None,
    ):
        super().__init__(nazwa, wartosc, efekt)

        self._wymagania = wymagania

    @property
    def wymagania(self):
        return self._wymagania


class Pierscien(Artefakt):
    """
    Klasa Pierścien dziedzicząca z klasy Artefakt
    """

    pass


class Amulet(Artefakt):
    """
    Klasa Amulet dziedzicząca z klasy Artefakt
    """

    pass


class Pas(Artefakt):
    """
    Klasa Pas dziedzicząca z klasy Artefakt
    """


class Tablica(Artefakt):
    """
    Klasa Tablica dziedzicząca z klasy Artefakt
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        wymagania: dict[str, int],
        efekt: dict[str, int] | None = None,
    ):
        super().__init__(nazwa, wartosc, efekt)
        self._wymagania = wymagania

    @property
    def wymagania(self):
        return self._wymagania


class Pozostale(Przedmiot):
    """
    Klasa Pozostałe, standardowe pola to nazwa, wartość oraz efefkt.
    Ta klasa trochę nie podoba mi się ze względu na zadaną liczbę argumentów
    imo powinno to być tak, że ta klasa może mieć dowolne argumenty
    nie wiem natomiast jak to zrobić, by były dziedziczone 3 podstawowe argumenty
    oraz nieskończona liczba pozostałych
    do tego dodałbym możliwośc użycia w takim wypadku jakiegoś przedmiotu/ubrania
    np. użyj Grabi, czy piły.

    :param nazwa: nazwa przedmiotu
    :param wartosc: nazwa przedmiotu wyrażana w sztukach złota
    :param efekt: efekt to zamiennik pola uzycie/bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi - to zrobić jako default argument w postaci NONE.
    """

    pass


class Kontener(dict):
    """
    Klasa bazowa kontener, ktora dziedziczy po dict i implementuje metode wyswietl
    """

    def wyswietl(self):
        return self

    def __str__(self):
        return type(self).__name__


class Bronie(Kontener):
    """
    Kontener na przedmioty klasy Broń posiadający metodę wyświetl
    """


class Pancerze(Kontener):
    """
    Kontener na przedmioty klasy Pancerz posiadający metodę wyświetl
    """


class PrzedmiotyMagiczne(Kontener):
    """
    Kontener na przedmioty klasy Magia posiadający metodę wyświetl
    """


class Pisma(Kontener):
    """
    Kontener na przedmioty klasy Pisma posiadający metodę wyświetl
    """


class Artefakty(Kontener):
    """
    Kontener na przedmioty klasy Artefakt posiadający metodę wyświetl
    """


class Zywnosc(Kontener):
    """
    Kontener na przedmioty klasy Jedzenie posiadający metodę wyświetl
    """


class Pozostalosci(Kontener):
    """
    Kontener na przedmioty klasy Pozostale posiadający metodę wyświetl
    """


class Ekwipunek:
    """
    Klasa Ekwipunek -> To w niej znajdują się Przedmioty z Podłogi dodane za pomocą
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
        # przełączyć na 3.13 sięęęe.

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
    def wyrzuc(self, item):
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
        for _, v in self.w_uzyciu.items():
            if item in v:
                print("\nNie można usunąć przedmiotu, który jest w użyciu!\n")
                return None
        for k, v in self._mapping.items():
            if isinstance(item, k):
                kontener = self._mapping[k]
                przedmioty = kontener[item.nazwa]
                if len(przedmioty) == 1:
                    del kontener[item.nazwa]
                return przedmioty.pop(0)

    def uzyj(self, item):
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

                self._jedzenie[item.nazwa].remove(item)
                if len(self._jedzenie[item.nazwa]) == 0:
                    del self._jedzenie[item.nazwa]
            elif isinstance(item, Magia):
                if isinstance(item, Zwoj):
                    clear()
                    print("\nZwój został użyty!\n")
                    self._przedmioty_magiczne[item.nazwa].remove(item)
                    if len(self._przedmioty_magiczne[item.nazwa]) == 0:
                        del self._przedmioty_magiczne[item.nazwa]
                else:
                    if type(item).__name__ not in self._w_uzyciu.keys():
                        clear()
                        self._w_uzyciu.update({type(item).__name__: [item]})
                    else:
                        self._w_uzyciu[type(item).__name__] += [item]
            elif isinstance(item, Pozostale):
                pass
            else:
                self._w_uzyciu.update({type(item).__name__: [item]})
            clear()
            print("\nPrzedmiot został użyty!\n")
        else:
            clear()
            print("\nPrzedmiotu nie da się użyć!\n")

    def zdejmij(self, item):

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
        for key, value in self.w_uzyciu.items():
            for i in value:
                if i == item:
                    self.w_uzyciu[key].remove(item)
                    if len(value) == 1:
                        del self.w_uzyciu[key]
        clear()
        print("\nPrzedmiot został zdjęty!\n")

    def dodaj(self, przedmiot):
        """
        Metoda dodaj dodaje przedmioty do danego kontenera w zależności od klasy

        :param przedmiot: obiekt klasy Przedmiot
        """

        for k, v in self._mapping.items():
            if isinstance(przedmiot, k):
                kontener = self._mapping[k]
                if przedmiot.nazwa not in kontener:
                    kontener.update({przedmiot.nazwa: [przedmiot]})
                else:
                    kontener[przedmiot.nazwa].append(przedmiot)

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
            for v in v:
                print(k, v.nazwa)

    def interfejs(self, lokalizacja: object):
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
                        przedmiot := slownik_interfejsu[int(identifier_przedmiotu)]
                    ) in przedmioty:
                        # item = <__main__.BronJednoreczna object at 0x1025a8b80>
                        item: Przedmiot = self.wyswietl_magazyn()[kontener][przedmiot][
                            0
                        ]

                        # TODO: zmienna uzywane, ktora przechowuje informacje czy przedmiot jest w
                        # uzyciu czy nie - do przegadania czy jest to potrzebne.

                        # od tego momentu powinienem wyeksportowac wszystko co jest dalej
                        # do innej funkcji(sprawdzic czy tam byloby GIT) - DONE
                        self.podinterfejs(item, lokalizacja, przedmiot)
            except KeyError:
                clear()
                print("\nDanego przedmiotu nie ma w ekwipunku.\n")
            except ValueError:
                clear()
                print("\nDanego przedmiotu nie ma w ekwipunku.\n")

    def podinterfejs(self, item, lokalizacja, przedmiot):
        """
        Metoda podinterfejs odpowiadająca za podinterfejs ekwipunku - tutaj dzieją
        sie wszystkie rzeczy po "wybraniu" przedmiotu.

        :param item
        :param lokalizacja
        :param przedmiot
        """

        przedmioty_w_uzyciu: list[str, Any] = [
            obj.nazwa for nazwa_obj in self.w_uzyciu.values() for obj in nazwa_obj
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
                    self.uzyj(item)
                    break
                if wybranie_przedmiotu == 1 and przedmiot in przedmioty_w_uzyciu:
                    self.zdejmij(item)
                    break
                if wybranie_przedmiotu == 2:
                    clear()
                    if self.wyrzuc(item) is None:
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


class Oselka:
    """
    Klasa Osełka posiadająca metodę naostrz
    """

    @staticmethod
    def naostrz(kontener: dict):
        """
        Metoda naostrz przyjmuje kontener jako argument, a następnie wyświetla przedmioty
        możliwe do naostrzenia znajdujące się w tym kontenerze. W tym momencie jedyny
        kontener posiadający przedmioty możliwe do naostrzenia to kontener broni.
        Metoda podnosi statystyki obrażeń przedmiotu o 10% oraz zmienia jego nazwę oraz
        pole 'naostrzony'
        :param kontener: kontener danego przedmiotu, np. bronie
        """
        slownik_oselki = {}
        przedmioty_w_uzyciu: list[str, Any] = [
            obj.nazwa
            for nazwa_obj in Ekwipunek_Obiekt.w_uzyciu.values()
            for obj in nazwa_obj
        ]
        identifier = 0
        print("Oto wszystkie przedmioty w ekwipunku, które możesz naostrzyć:")
        for key, value in kontener.wyswietl().items():
            if isinstance(value[0], (BronJednoreczna, BronDwureczna)):
                for i in value:
                    if not i.naostrzony:
                        if i.nazwa not in przedmioty_w_uzyciu:
                            # tu zalozenie ze wszystkie przedmioty z listy maja dany atrybut
                            print(identifier, key, "sztuk " + str(len(value)))
                            slownik_oselki[identifier] = i.nazwa
                            identifier += 1
                            break
                        print(identifier, key, "w użyciu")
                        slownik_oselki[identifier] = i.nazwa + " w użyciu"
                        identifier += 1
                        if len(value) - 1 == 0:
                            break
                        print(identifier, key, "sztuk " + str(len(value) - 1))
                        slownik_oselki[identifier] = i.nazwa
                        identifier += 1
                        break
        val = input(
            "Podaj ID przedmiotu, który chciałbyś naostrzyć lub wpisz 'exit' by wyjść: "
        )
        if val == "exit":
            clear()
            return 0
        try:
            if (
                slownik_oselki[int(val)].partition(" w użyciu")[0]
                in kontener.wyswietl()
            ):
                if "w użyciu" in slownik_oselki[int(val)]:
                    item = kontener[slownik_oselki[int(val)].partition(" w użyciu")[0]][
                        0
                    ]
                    item._efekt["obrazenia"] = round(item._efekt["obrazenia"] * 1.10)
                    round(item._efekt["obrazenia"])
                    del kontener[slownik_oselki[int(val)].partition(" w użyciu")[0]][0]
                    if (
                        kontener[slownik_oselki[int(val)].partition(" w użyciu")[0]]
                        == []
                    ):
                        del kontener[slownik_oselki[int(val)].partition(" w użyciu")[0]]
                    item._nazwa = (
                        "Naostrzony "
                        + slownik_oselki[int(val)].partition(" w użyciu")[0]
                    )
                    item._naostrzony = True
                    kontener.update({item._nazwa: [item]})
                    print("Przedmiot naostrzono")
                    Oselka.naostrz(kontener)
                else:
                    item = kontener[slownik_oselki[int(val)]][-1]
                    item._efekt["obrazenia"] = round(item._efekt["obrazenia"] * 1.10)
                    del kontener[slownik_oselki[int(val)]][-1]
                    if kontener[slownik_oselki[int(val)]] == []:
                        del kontener[slownik_oselki[int(val)]]
                    item._nazwa = "Naostrzony " + slownik_oselki[int(val)]
                    item._naostrzony = True
                    if item._nazwa not in kontener:
                        kontener.update({item._nazwa: [item]})
                    else:
                        kontener[item._nazwa].append(item)
                    print("Przedmiot naostrzono")
                    Oselka.naostrz(kontener)
            else:
                print("Danego przedmiotu nie ma w ekwipunku!")
                Oselka.naostrz(kontener)
        except KeyError:
            print("Przedmiot z danym ID nie istnieje")
            Oselka.naostrz(kontener)


class Bohater:
    """
    Nowopowstała klasa Bohater będąca pośrednikiem między Podłogą, a Ekwipunkiem,
    posiadająca metodę podejrzyj.
    """

    def podejrzyj(self, obiekt: "Khorinis"):
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
        Ekwipunek.dodaj(Ekwipunek_Obiekt, przedmiot)


class Lokalizacja:
    """
    Klasa Lokalizacja.
    """

    def __str__(self):
        return type(self).__name__

    def spojrz(self):
        """
        Metoda zwracająca listę zawartość
        """
        # odpowiednik wyswietl, aka spojrz na podloge
        return self.zawartosc


class Khorinis(Lokalizacja):
    """
    Klasa Khorinis to zbiór wszystkich stworzonych obiektów typu Przedmiot w Khorinis.
    Posiada metodę spójrz.
    """

    def __init__(self):
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
            Jedzenie("Gulasz Thekli", 1, {"Siła": 1, "Smak": "Zajebisty", "HP": 20}),
            Jedzenie("Gulasz Thekli", 1, {"Siła": 1, "Smak": "Zajebisty", "HP": 20}),
            Jedzenie("Zupa Rybna", 20, {"HP": 10}),
            Amulet("Oko Innosa", 0, ["Możliwość rozmowy ze smokami"]),
            Artefakt("Kamień ogniskujący", 0, None),
            Pozostale("Grabie", 0, None),
        ]


class GorniczaDolina(Lokalizacja):
    """
    Klasa GorniczaDolina to zbiór wszystkich stworzonych obiektów typu Przedmiot w Gorniczej
    Dolinie. Posiada metodę spójrz.
    """

    def __init__(self):
        self.zawartosc = [
            BronJednoreczna(
                "Szept Burzy z Gorniczej Doliny",
                1360,
                {"Siła": 20},
                {"obrazenia": 50},
                2,
            ),
            BronJednoreczna(
                "Mieczyk z Gorniczej Doliny", 7, {"Siła": 5}, {"obrazenia": 11}, 2
            ),
            BronJednoreczna(
                "Mieczyk z Gorniczej Doliny", 7, {"Siła": 5}, {"obrazenia": 11}, 2
            ),
            Pancerz(
                "Zbroja z pancerzy pełzaczy z Gorniczej Doliny",
                2400,
                {
                    "Ochrona przed bronią": 80,
                    "Ochrona przed strzałami": 15,
                    "Ochrona przed ogniem": 30,
                    "Ochrona przed magia": 5,
                },
                {"Siła": 0},
            ),
            Runa("Bryła lodu z Gorniczej Doliny", 700, 3, {"obrazenia": 3}, 50),
            Pismo(
                "Dwór Irdorath z Gorniczej Doliny",
                0,
                "Mam w dupie przeznaczenie.",
            ),
            Pismo(
                "Historia Jarkendaru z Gorniczej Doliny",
                0,
                "Co robisz? Topisz złoto? Nie, siekam cebulkę.",
            ),
            Jedzenie("Gulasz Thekli", 1, {"Siła": 1, "Smak": "Zajebisty", "HP": 20}),
            Jedzenie("Gulasz Thekli", 1, {"Siła": 1, "Smak": "Zajebisty", "HP": 20}),
        ]


class Jarkendar(Lokalizacja):
    """
    Klasa Jarkendar to zbiór wszystkich stworzonych obiektów typu Przedmiot w Gorniczej Dolinie.
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


Ekwipunek_Obiekt = Ekwipunek()
Oselka_Obiekt = Oselka()
Bohater_Obiekt = Bohater()
Khorinis_Obiekt = Khorinis()
Gornicza_Dolina_Obiekt = GorniczaDolina()
Jarkendar_Obiekt = Jarkendar()


def modul():
    while True:
        # clear()
        try:
            val = int(
                input(
                    "\nWybierz lokalizacje\n1. Khorinis \n2. Gornicza Dolina \n3. Jarkendar"
                )
            )
            if val == 1:
                aktualna_lokalizacja = Khorinis_Obiekt
                return aktualna_lokalizacja
            if val == 2:
                aktualna_lokalizacja = Gornicza_Dolina_Obiekt
                return aktualna_lokalizacja
            if val == 3:
                aktualna_lokalizacja = Jarkendar_Obiekt
                return aktualna_lokalizacja
            raise ValueError("błędna wartość elo")
        except ValueError:
            clear()
            print("Podaj wartość jeszcze raz")


def interfejs_glowny(lokalizacja=None):
    """
    Interfejs główny modułu. Za jego pomocą wywoływane są metody.

    :param lokalizacja: jest to lokalizacja, w ktorej uzytkownik obecnie sie znajduje,
            dla przykladu Khorinis lub Gornicza Dolina
    """

    # DONE wymodulowanie tego
    # DONE dorobienie 3 lokalizacji - Jarkendar
    # przerobic caly interfejs ekwipunku - DONE
    # nie podawac lokalizacji do metody wyrzuc, tylko podawac jej kontener, a metoda wyrzuc
    # zwracala wyrzucany obiekt - DONE, ale jakim kosztem ->
    # przekazywanie do lokalizacji znajduje się poza funkcją.
    # TODO: bohater -> dorobic mu funkcjonalnosc - w jaki sposób?
    # while lokalizacja is None:
    #    lokalizacja = modul()

    input_interfejs = {
        True: [
            "Zmień lokalizację. ",
            "Zbierz przedmioty znajdujace sie w danej lokacji, ",
            "Odpal interfejs ekwipunku, ",
            "Odpal interfejs Osełki, ",
            "Wyświetl przedmioty w użyciu bohatera",
        ],
        False: ["Wybierz lokalizację początkową."],
    }
    while True:
        prompt = [
            f"{f'Znajdujesz się w {str(lokalizacja)}.' if lokalizacja else ''} "
            f"Wybierz co chcesz zrobić. "
        ]
        try:
            zmienna = [
                f"{x}. {y}"
                for x, y in enumerate(input_interfejs[bool(lokalizacja)], start=1)
            ]
            val = int(input("\n".join([*prompt, *zmienna]).lstrip("\n ")))
            if val > len(zmienna) or val < 1:
                raise ValueError("Argh!")
            if val == 1:
                lokalizacja = modul()
            elif val == 2:
                Bohater_Obiekt.podejrzyj(lokalizacja)
                print("\nPrzedmioty zostały podniesione. \n")
            elif val == 3:
                Ekwipunek_Obiekt.interfejs(lokalizacja)
            elif val == 4:
                Oselka_Obiekt.naostrz(Ekwipunek_Obiekt._bronie)
            elif val == 5:
                Ekwipunek_Obiekt.wyswietl_w_uzyciu()
        except ValueError:
            pass


interfejs_glowny(lokalizacja=None)

# API - ladne punkty wejscia i wyjscia

# przejscie przez restrukturyzacje kodu, tworzenie funkcji ladnych,
# zgrabnych i przyjemnych dla uzytkownika
