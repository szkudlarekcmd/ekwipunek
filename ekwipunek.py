"""
Konwencja -> Koncept jest taki, że w kodzie polskich znaków nie ma oprócz stringów.
Wszystko w pierdolnikach jest oficjalne
"""

from abc import ABC
from collections import defaultdict
from typing import Any
import os
from itertools import chain


# pylint: disable=missing-function-docstring, too-many-arguments, unnecessary-pass
# pylint: disable=too-many-positional-arguments
# pylint: disable=too-few-public-methods, protected-access, too-many-branches
# pylint: disable=too-many-nested-blocks, too-many-instance-attributes
# pylint: disable=useless-parent-delegation, too-many-lines, too-many-locals
# pylint: disable=too-many-statements, inconsistent-return-statements


def clear():
    """
    Czyści terminal, macos/linux only.
    (emulate terminal in output console)
    """
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
        efekt: dict[str, int],
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
        zasieg: int = 1,
        naostrzony: bool = False,
    ):
        super().__init__(nazwa, wartosc, wymagania, efekt, zasieg)
        self._naostrzony = naostrzony

    @property
    def naostrzony(self):
        return self._naostrzony


class BronDystansowa(Bron):
    """
    Klasa broni białej.

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
        zasieg: int = 1,
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
        ochrona: dict[str, int],
        wymagania: dict[str, int],
        efekt: dict[str, int] | None = None,
    ):
        if efekt is None:
            efekt = ochrona
        super().__init__(nazwa, wartosc, efekt)
        default_ochrona: dict[str, int] = {
            "Ochrona przed bronią": 0,
            "Ochrona przed strzałami": 0,
            "Ochrona przed magią": 0,
            "Ochrona przed ogniem": 0,
        }
        default_ochrona.update(ochrona)
        # to jest najprawdopodobniej niepotrzebne.
        self._ochrona = ochrona
        self._ochrona = default_ochrona
        self._wymagania = wymagania

    @property
    def ochrona(self):
        return self._ochrona

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
        super().__init__(nazwa, wartosc, efekt)
        self._mana = mana
        if wymagania is None:
            self._wymagania = {"Koszt many": self.mana}

    @property
    def mana(self):
        return self._mana

    @property
    def wymagania(self):
        return self._wymagania


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
        krag: int,
    ):
        super().__init__(nazwa, wartosc, mana, efekt)
        self._krag = krag

    @property
    def krag(self):
        return self._krag


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
        efekt: dict[str, int] | list,
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

    def __init__(self, nazwa: str, wartosc: int, efekt: dict[str, int] | None | list):
        super().__init__(nazwa, wartosc, efekt)


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
    Klasa Pozostałe, standardowe pola to nazwa, wartość oraz ilość.
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
        o tym co przedmiot robi
    """

    pass


class Kontener(dict):
    """
    Klasa bazowa kontener, ktora dziedziczy po dict i implementuje metode wyswietl
    """

    def wyswietl(self):
        return self


class Bronie(Kontener):
    """
    Kontener na przedmioty klasy Broń posiadający metodę wyświetl
    """

    def __str__(self):
        return type(self).__name__


class Pancerze(Kontener):
    """
    Kontener na przedmioty klasy Pancerz posiadający metodę wyświetl
    """

    def __str__(self):
        return type(self).__name__


class PrzedmiotyMagiczne(Kontener):
    """
    Kontener na przedmioty klasy Magia posiadający metodę wyświetl
    """

    def __str__(self):
        return type(self).__name__


class Pisma(Kontener):
    """
    Kontener na przedmioty klasy Pisma posiadający metodę wyświetl
    """

    def __str__(self):
        return type(self).__name__


class Artefakty(Kontener):
    """
    Kontener na przedmioty klasy Artefakt posiadający metodę wyświetl
    """

    def __str__(self):
        return type(self).__name__


class Zywnosc(Kontener):
    """
    Kontener na przedmioty klasy Jedzenie posiadający metodę wyświetl
    """

    def __str__(self):
        return type(self).__name__


class Pozostalosci(Kontener):
    """
    Kontener na przedmioty klasy Pozostale posiadający metodę wyświetl
    """

    def __str__(self):
        return type(self).__name__


class Ekwipunek:
    """
    Klasa Ekwipunek -> To w niej znajdują się Przedmioty z Podłogi dodane za pomocą
    Bohatera. Tutaj również znajduje się kontener w uzyciu (nie wiem, czy słusznie).
    :param bronie: kontener na przedmioty klasy Broń
    :param pancerze: kontener na przedmioty klasy Pancerz
    :param przedmioty magiczne: kontener na przedmioty klasy Magia
    :param pisma: kontener na przedmioty klasy Pismo
    :param artefakty: kontener na przedmioty klasy Artefakt
    :param jedzenie: kontener na przedmioty klasy Jedzenie
    :param pozostale: kontener na przedmioty klasy Pozostale
    :param magazyn: słownik zawierający wszystkie kontenery przypisane
        do odpowiedniego klucza
    :param w_uzyciu: kontener zawierający przedmioty znajdujące się w danej
        chwili w użyciu
    """

    def __init__(self):
        self._bronie = Bronie()
        self._pancerze = Pancerze()
        self._przedmioty_magiczne = PrzedmiotyMagiczne()
        self._pisma = Pisma()
        self._artefakty = Artefakty()
        self._jedzenie = Zywnosc()
        self._pozostale = Pozostalosci()
        self._w_uzyciu = defaultdict(list)
        # trochę słaby ten mapping, ale na ten moment nie mam lepszego pomysłu
        self._mapping = {
            str(self._bronie): "bronie",
            str(self._pancerze): "pancerze",
            str(self._przedmioty_magiczne): "przedmioty_magiczne",
            str(self._pisma): "pisma",
            str(self._artefakty): "artefakty",
            str(self._jedzenie): "jedzenie",
            str(self._pozostale): "pozostale",
        }
        self._magazyn = {
            str(self._bronie): self._bronie,
            str(self._pancerze): self._pancerze,
            str(self._przedmioty_magiczne): self._przedmioty_magiczne,
            str(self._pisma): self._pisma,
            str(self._artefakty): self._artefakty,
            str(self._jedzenie): self._jedzenie,
            str(self._pozostale): self._pozostale,
        }

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

    def wyrzuc(self, item, nazwa_kontenera):
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
        # np żeby móc używać dwóch run naraz - bo przecież tak mozna - DONE, nie lista a tupla
        #TODO: defaultdict

        # TO JEST DO ZROBIENIA...
        for _, v in self.w_uzyciu.items():
            if item == v:
                print("\nNie można usunąć przedmiotu, który jest w użyciu!\n")
                return None
        kontener = getattr(self, self._mapping[nazwa_kontenera])
        przedmioty = kontener[item.nazwa]
        if len(przedmioty) == 1:
            del kontener[item.nazwa]
        return przedmioty.pop(0)

    def uzyj(self, item, lokalizacja):
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
                        self._w_uzyciu.update({type(item).__name__: (item,)})
                    else:
                        self._w_uzyciu[type(item).__name__] += (item,)
            elif isinstance(item, Pozostale):
                pass
            else:
                self._w_uzyciu.update({type(item).__name__: (item,)})
            clear()
            print("\nPrzedmiot został użyty!\n")
            self.interfejs(lokalizacja)
        else:
            clear()
            print("\nPrzedmiotu nie da się użyć!\n")
            self.interfejs(lokalizacja)

    def zdejmij(self, item, lokalizacja, przedmioty_w_uzyciu):
        """
        Metoda ściąga dany przedmiot z przedmiotów w użyciu.

        :param item: obiekt klasy Przedmiot
        :param lokalizacja: jest to lokalizacja, w ktorej uzytkownik obecnie sie znajduje,
            dla przykladu Khorinis lub Gornicza Dolina
        :param przedmioty_w_uzyciu: lista, w ktorej znajduja sie nazwy przedmiotow obecnie
            znajdujących się w użyciu
        """
        for key, value in Ekwipunek_Obiekt.w_uzyciu.copy().items():
            for i in value:
                if i == item:
                    Ekwipunek_Obiekt.w_uzyciu[key] = list(
                        Ekwipunek_Obiekt.w_uzyciu[key]
                    )
                    Ekwipunek_Obiekt.w_uzyciu[key].remove(item)
                    tuple(Ekwipunek_Obiekt.w_uzyciu[key])
                    if len(value) == 1:
                        del Ekwipunek_Obiekt.w_uzyciu[key]
                    przedmioty_w_uzyciu.remove(item.nazwa)
        clear()
        print("\nPrzedmiot został zdjęty!\n")
        self.interfejs(lokalizacja)

    def dodaj(self, przedmiot):
        """
        Metoda dodaj dodaje przedmioty do danego kontenera w zależności od klasy

        :param przedmiot: obiekt klasy Przedmiot
        """
        if isinstance(przedmiot, Bron):
            if przedmiot.nazwa not in self.bronie:
                self._bronie.update({przedmiot.nazwa: [przedmiot]})
            else:
                self._bronie[przedmiot.nazwa].append(przedmiot)
        elif isinstance(przedmiot, Pancerz):
            if przedmiot.nazwa not in self.pancerze:
                self._pancerze.update({przedmiot.nazwa: [przedmiot]})
            else:
                self._pancerze[przedmiot.nazwa].append(przedmiot)
        elif isinstance(przedmiot, Magia):
            if przedmiot.nazwa not in self.przedmioty_magiczne:
                self._przedmioty_magiczne.update({przedmiot.nazwa: [przedmiot]})
            else:
                self._przedmioty_magiczne[przedmiot.nazwa].append(przedmiot)
        elif isinstance(przedmiot, Pismo):
            if przedmiot.nazwa not in self.pisma:
                self._pisma.update({przedmiot.nazwa: [przedmiot]})
            else:
                self._pisma[przedmiot.nazwa].append(przedmiot)
        elif isinstance(przedmiot, Artefakt):
            if przedmiot.nazwa not in self.artefakty:
                self._artefakty.update({przedmiot.nazwa: [przedmiot]})
            else:
                self._artefakty[przedmiot.nazwa].append(przedmiot)
        elif isinstance(przedmiot, Jedzenie):
            if przedmiot.nazwa not in self.jedzenie:
                self._jedzenie.update({przedmiot.nazwa: [przedmiot]})
            else:
                self._jedzenie[przedmiot.nazwa].append(przedmiot)
        elif isinstance(przedmiot, Pozostale):
            if przedmiot.nazwa not in self.pozostale:
                self._pozostale.update({przedmiot.nazwa: [przedmiot]})
            else:
                self._pozostale[przedmiot.nazwa].append(przedmiot)

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
        :param init = bool, okresla czy dana metoda zostala wywolana w module po raz pierwszy
            Ma to na celu wyprintowanie informacji na temat symboli wykorzystywanych przez
            metode. Nie chcemy wywoływać tych informacji za każdym razem, gdy wywolujemy
            metode.

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

                #TODO: Walidacje robić przed - tzn sprawdzenie - nie muszę
                # iterować następny raz po wyswietl_magazyn().items()

                for kontener, przedmioty in self.wyswietl_magazyn().items():
                    # slownik_interfejsu[int(ID_przedmiotu)] = 'Szept Burzy'

                    #TODO: DODAĆ OBSŁUGĘ FLOAT'A - po co?

                    if (
                        przedmiot := slownik_interfejsu[int(identifier_przedmiotu)]
                    ) in przedmioty:
                        # item = <__main__.BronJednoreczna object at 0x1025a8b80>
                        item: Przedmiot = self.wyswietl_magazyn()[kontener][przedmiot][
                            0
                        ]

                        #TODO: zmienna uzywane, ktora przechowuje informacje czy przedmiot jest w
                        # uzyciu czy nie - do przegadania czy jest to potrzebne.


                        # od tego momentu powinienem wyeksportowac wszystko co jest dalej
                        # do innej funkcji(sprawdzic czy tam byloby GIT) - DONE
                        self.podinterfejs(item, lokalizacja, przedmiot, kontener)
                        return 0
            except KeyError:
                clear()
                print("\nDanego przedmiotu nie ma w ekwipunku.\n")
            except ValueError:
                clear()
                print("\nDanego przedmiotu nie ma w ekwipunku.\n")

    def podinterfejs(self, item, lokalizacja, przedmiot, kontener):

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
                    self.uzyj(item, lokalizacja)
                    break
                if wybranie_przedmiotu == 1 and przedmiot in przedmioty_w_uzyciu:
                    self.zdejmij(item, lokalizacja, przedmioty_w_uzyciu)
                    break
                if wybranie_przedmiotu == 2:
                    clear()
                    self.wyrzuc(item, kontener)
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
            BronJednoreczna("Szept Burzy", 1360, {"Siła": 20}, {"obrazenia": 50}),
            BronJednoreczna("Szept Burzy", 1360, {"Siła": 20}, {"obrazenia": 50}),
            BronJednoreczna("Szept Burzy", 1360, {"Siła": 20}, {"obrazenia": 50}),
            BronJednoreczna("Kij z gwoździem", 7, {"Siła": 5}, {"obrazenia": 11}),
            BronJednoreczna("Mieczyk", 7, {"Siła": 5}, {"obrazenia": 11}),
            BronJednoreczna("Mieczyk", 7, {"Siła": 5}, {"obrazenia": 11}),
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
            Runa("Bryła lodu", 700, 3, {"Obrażenia": 3}, 50),
            Runa("Deszcz ognia", 1300, 5, {"Obrażenia": 13}, 100),
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
            ),
            BronJednoreczna(
                "Mieczyk z Gorniczej Doliny", 7, {"Siła": 5}, {"obrazenia": 11}
            ),
            BronJednoreczna(
                "Mieczyk z Gorniczej Doliny", 7, {"Siła": 5}, {"obrazenia": 11}
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
            BronJednoreczna("Jaszczurzy miecz", 1360, {"Siła": 40}, {"obrazenia": 100}),
            BronJednoreczna("Miecz z Jarkendaru", 25, {"Siła": 15}, {"obrazenia": 40}),
            BronJednoreczna("Miecz z Jarkendaru", 25, {"Siła": 15}, {"obrazenia": 40}),
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
            Runa("Bryła lodu z Jarkendaru", 700, 3, {"obrazenia": 3}, 50),
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
    #TODO: bohater -> dorobic mu funkcjonalnosc - w jaki sposób?
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
