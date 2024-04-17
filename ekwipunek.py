"""
Konwencja -> Koncept jest taki, że w kodzie polskich znaków nie ma oprócz stringów.
Wszystko w pierdolnikach jest oficjalne
"""
from abc import ABC
from typing import Any
import math

# pylint: disable=missing-function-docstring, too-many-arguments, unnecessary-pass
# pylint: disable=too-few-public-methods, protected-access, too-many-branches
# pylint: disable=too-many-nested-blokalizacjaks, too-many-instance-attributes
# pylint: disable=useless-parent-delegation
class Przedmiot(ABC):
    """
    Base klasa, abstrakcyjna.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param efekt: efekt to zamiennik pola uzycie, jak rowniez bonusy ->
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
    :param obrazenia: wartość zadawanych przez przedmiot obrażeń
    :param efekt: efekt to zamiennik pola uzycie, jak rowniez bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    :param zasieg: zasieg broni
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        wymagania: dict[str, int],
        obrazenia: int | None = None,
        efekt: dict[str, int] | None = None,
        zasieg: int | None = None
    ):
        if efekt is None:
            efekt = {"obrażenia": obrazenia}
        elif efekt is dict and obrazenia is None:
            efekt["obrażenia"] = obrazenia
        super().__init__(nazwa, wartosc, efekt)
        self._wymagania = wymagania
        self._obrazenia = obrazenia
        self._zasieg = zasieg

    @property
    def wymagania(self):
        return self._wymagania

    @property
    def obrazenia(self):
        return self._obrazenia

    @property
    def zasieg(self):
        return self._zasieg


class BronBiala(Bron):
    """
    Klasa broni białej.

    :param nazwa: nazwa przedmiotu
    :param wartosc: wartość przedmiotu wyrażana w sztukach złota
    :param wymagania: wymagane atrybuty do użycia danego przedmiotu
    :param obrazenia: wartość zadawanych przez przedmiot obrażeń
    :param naostrzony: informuje, czy dany przedmiot zostal naostrzony
    :param efekt: efekt to zamiennik pola uzycie, jak rowniez bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    :param zasieg: zasieg broni
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        wymagania: dict[str, int],
        obrazenia: int,
        naostrzony: bool,
        zasieg: int = 1,
        efekt: dict[str, int] | None = None,
    ):
        if efekt is None:
            efekt = {"obrażenia": obrazenia}
        super().__init__(nazwa, wartosc, wymagania, obrazenia, efekt, zasieg)
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
        :param obrazenia: wartość zadawanych przez przedmiot obrażeń
        :param zasieg: zasieg broni
        :param efekt: efekt to zamiennik pola uzycie, jak rowniez bonusy ->
            jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
            o tym co przedmiot robi
        """
    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        wymagania: dict[str, int],
        obrazenia: int,
        zasieg: int = 1,
        efekt: dict[str, int] | None = None,
    ):
        if efekt is None:
            efekt = {"obrażenia": obrazenia}
        super().__init__(nazwa, wartosc, wymagania, obrazenia, efekt, zasieg)


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
    :param efekt: efekt to zamiennik pola uzycie, jak rowniez bonusy ->
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
    :param efekt: efekt to zamiennik pola uzycie, jak rowniez bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        mana: int,
        efekt: dict[str, Any],
        wymagania: dict[str, int] = None,
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
    :param efekt: efekt to zamiennik pola uzycie, jak rowniez bonusy ->
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
    :param efekt: efekt to zamiennik pola uzycie, jak rowniez bonusy ->
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
    :param efekt: efekt to zamiennik pola uzycie, jak rowniez bonusy ->
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
    :param efekt: efekt to zamiennik pola uzycie, jak rowniez bonusy ->
        jego obecnosc informuje iz przedmiot mozna uzyc, a sam efekt informuje
        o tym co przedmiot robi
    """

    pass


class Bronie(dict):
    """
    Kontener na przedmioty klasy Broń posiadający metodę wyświetl
    """

    def wyswietl(self):
        return self


class Pancerze(dict):
    """
    Kontener na przedmioty klasy Pancerz posiadający metodę wyświetl
    """

    def wyswietl(self):
        return self


class PrzedmiotyMagiczne(dict):
    """
    Kontener na przedmioty klasy Magia posiadający metodę wyświetl
    """

    def wyswietl(self):
        return self


class Pisma(dict):
    """
    Kontener na przedmioty klasy Pisma posiadający metodę wyświetl
    """

    def wyswietl(self):
        return self


class Artefakty(dict):
    """
    Kontener na przedmioty klasy Artefakt posiadający metodę wyświetl
    """

    def wyswietl(self):
        return self


class Zywnosc(dict):
    """
    Kontener na przedmioty klasy Jedzenie posiadający metodę wyświetl
    """

    def wyswietl(self):
        return self


class Pozostalosci(dict):
    """
    Kontener na przedmioty klasy Pozostale posiadający metodę wyświetl
    """

    def wyswietl(self):
        return self


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
        self._w_uzyciu = {}

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

    def wyrzuc(self, item, lokalizacja):
        """
        Metoda wyrzuć wyrzucająca dany przedmiot z obiektu klasy Ekwipunek i zwracająca go
        do obiektu klasy Podłoga.

        :param item: obiekt klasy Przedmiot
        :param lokalizacja: jest to lokalizacja, w ktorej uzytkownik obecnie sie znajduje,
            dla przykladu Khorinis lub Gornicza Dolina
        """

        lokalizacja.zawartosc.append(item)
        for k, v in self.w_uzyciu.copy().items():
            if item == v:
                print(
                    "\nNie można usunąć przedmiotu, który jest w użyciu!\n"
                )
                self.interfejs(lokalizacja, init=True)
        if isinstance(item, Bron):
            self._bronie[item.nazwa].remove(item)
            if len(self._bronie[item.nazwa]) == 0:
                del self._bronie[item.nazwa]
        elif isinstance(item, Pancerz):
            self._pancerze[item.nazwa].remove(item)
            if len(self._pancerze[item.nazwa]) == 0:
                del self._pancerze[item.nazwa]
        elif isinstance(item, Magia):
            self._przedmioty_magiczne[item.nazwa].remove(item)
            if len(self._przedmioty_magiczne[item.nazwa]) == 0:
                del self._przedmioty_magiczne[item.nazwa]
        elif isinstance(item, Pismo):
            self._pisma[item.nazwa].remove(item)
            if len(self._pisma[item.nazwa]) == 0:
                del self._pisma[item.nazwa]
        elif isinstance(item, Artefakt):
            self._artefakty[item.nazwa].remove(item)
            if len(self._artefakty[item.nazwa]) == 0:
                del self._artefakty[item.nazwa]
        elif isinstance(item, Jedzenie):
            self._jedzenie[item.nazwa].remove(item)
            if len(self._jedzenie[item.nazwa]) == 0:
                del self._jedzenie[item.nazwa]
        elif isinstance(item, Pozostale):
            self._pozostale[item.nazwa].remove(item)
            if len(self._pozostale[item.nazwa]) == 0:
                del self._pozostale[item.nazwa]
        self.interfejs(lokalizacja, init=True)

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
                print(item.efekt)
            elif isinstance(item, Jedzenie):
                print(item.efekt)
                self._jedzenie[item.nazwa].remove(item)
                if len(self._jedzenie[item.nazwa]) == 0:
                    del self._jedzenie[item.nazwa]
            elif isinstance(item, Magia):
                if not item.krag:
                    print("\nZwój został użyty!\n")
                    self._przedmioty_magiczne[item.nazwa].remove(
                        item
                    )
                    if (
                            len(self._przedmioty_magiczne[item.nazwa])
                            == 0
                    ):
                        del self._przedmioty_magiczne[item.nazwa]
                else:
                    self._w_uzyciu.update(
                        {
                            str(type(item)).split(sep=".")[
                                1
                            ]: item
                        }
                    )
            elif isinstance(item, Pozostale):
                pass
            else:
                self._w_uzyciu.update(
                    {str(type(item)).split(sep=".")[1]: item}
                )
            print("\nPrzedmiot został użyty!\n")
            self.interfejs(lokalizacja, init=True)
        else:
            print("\nPrzedmiotu nie da się użyć!\n")
            self.interfejs(lokalizacja, init=True)

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
            if value == item:
                del Ekwipunek_Obiekt.w_uzyciu[key]
                przedmioty_w_uzyciu.remove(item.nazwa)
        print("\nPrzedmiot został zdjęty!\n")
        self.interfejs(lokalizacja, init=True)

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

    # różne warianty metody wyświetl -> jestem otwarty na dyskusję
    '''
    def wyswietl_sztuki(self):
        """
        Defaultowe wyświetl, zmieniona nazwa ze względu na kilka wariantów:
        Metoda ta wyświetla przedmioty w konwencji
        kontener -> nazwa przedmiotu -> ilość sztuk w ekwipunku
        """
        stan = {}
        for category, items in self.wyswietl_magazyn().items():
            category_dict = {}
            for item, item_list in items.items():
                category_dict[item] = len(item_list)
            stan[category] = category_dict
        print(stan)
        return stan
    '''

    def wyswietl_magazyn(self):
        """
        Metoda zwracająca kontener magazyn
        """
        self._magazyn = {
            "Bronie": self._bronie,
            "Pancerze": self._pancerze,
            "Przemioty Magiczne": self._przedmioty_magiczne,
            "Pisma": self._pisma,
            "Artefakty": self._artefakty,
            "Jedzenie": self._jedzenie,
            "Pozostałe": self._pozostale,
        }
        return self.magazyn

    def wyswietl_w_uzyciu(self):
        """
        Metoda wyświetlająca przedmioty w użyciu
        """
        for k, v in self.w_uzyciu.items():
            print(k, v.nazwa)

    def interfejs(self, lokalizacja: object, init: bool = False):
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
        lokalizacja: Khorinis | Gornicza_Dolina = lokalizacja
        # slownik_interfejsu - {0: 'Szept Burzy z Gorniczej Doliny', 1: 'Mieczyk z Gorniczej Doliny',...}
        slownik_interfejsu: dict[int, str] = {}
        ID: int = 0
        if init is False:
            print(
                "\nJeśli dany przedmiot można użyć, to przy jego ilości sztuk pojawi się kratka."
                "\nJeśli dany przedmiot znajduje się w użyciu, to znajduje sie przy nim gwiazdka. "
            )

        # key - Bronie
        # value - {'Szept Burzy z Gorniczej Doliny': [<__main__.BronJednoreczna object at 0x104360b80>],
        # 'Mieczyk z Gorniczej Doliny': [<__main__.BronJednoreczna object at 0x104360bb0>]}
        for key, value in self.wyswietl_magazyn().items():
            # k - Gulasz Thekli
            # v - [<__main__.Jedzenie object at 0x104360d60>, <__main__.Jedzenie object at 0x104360dc0>]
            for k, v in value.items():
                # sprawdzam czy zbiory sie pokrywaja - jesli tak, to dany przedmiot jest w uzyciu
                if bool(set(v) & set(self.w_uzyciu.values())):
                    print(f"{ID} * " + k + "    #" + " sztuk " + str(len(v)))
                    slownik_interfejsu[ID] = k
                    ID += 1
                # sprawdzam, czy dany przedmiot można użyć
                elif v[0].efekt:
                    print(f"{ID} " + k + "   #" + " sztuk " + str(len(v)))
                    slownik_interfejsu[ID] = k
                    ID += 1
                else:
                    print(f"{ID} " + k + " sztuk " + str(len(v)))
                    slownik_interfejsu[ID] = k
                    ID += 1
        ID_przedmiotu = input(
            "Podaj ID przedmiotu, ktory chcesz wybrać, lub wpisz 'exit', by wyjść: "
        )
        if ID_przedmiotu == "exit":
            return 0
        else:
            try:
                # kontener = 'Bronie'
                # przedmioty = {'Szept Burzy': [<__main__.BronJednoreczna object at 0x10233c550>,
                # <__main__.BronJednoreczna object at 0x10233c580>, <__main__.BronJednoreczna object at 0x10233c5b0>],
                # 'Kij z gwoździem': [<__main__.BronJednoreczna object at 0x10233c5e0>],
                # 'Zmyślony Łuk': [<__main__.Luk object at 0x10233c610>],
                # 'Zmyślona Kusza': [<__main__.Kusza object at 0x10233c640>]}
                for kontener, przedmioty in self.wyswietl_magazyn().items():
                    # slownik_interfejsu[int(ID_przedmiotu)] = 'Szept Burzy'
                    if slownik_interfejsu[int(ID_przedmiotu)] in przedmioty:
                        # item = <__main__.BronJednoreczna object at 0x1025a8b80>
                        item: Przedmiot = self.wyswietl_magazyn()[kontener][slownik_interfejsu[int(ID_przedmiotu)]][
                            0
                        ]
                        przedmioty_w_uzyciu: list[str] = [
                            Ekwipunek_Obiekt.w_uzyciu[key].nazwa
                            for key in Ekwipunek_Obiekt.w_uzyciu
                        ]
                        print(f"Wybrany przedmiot:\n{item.nazwa}")
                        # wyprintowanie statystyk
                        for kk, vv in item.__dict__.items():
                            if kk != "_nazwa":
                                print(kk.split("_")[1], vv)
                        # wybranie przedmiotu
                        if slownik_interfejsu[int(ID_przedmiotu)] not in przedmioty_w_uzyciu:
                            wybranie_przedmiotu: input = input(
                                "Co chcesz zrobić z danym przedmiotem?\n1. Użyj\n2. Wyrzuć\n3. Wybierz inny przedmiot"
                            )
                        elif slownik_interfejsu[int(ID_przedmiotu)] in przedmioty_w_uzyciu:
                            wybranie_przedmiotu: input = input(
                                "Co chcesz zrobić z danym przedmiotem?\n1. Zdejmij\n2. Wyrzuć\n3. Wybierz inny przedmiot"
                            )
                        if (
                                wybranie_przedmiotu == str(1)
                                and slownik_interfejsu[int(ID_przedmiotu)] not in przedmioty_w_uzyciu
                        ):
                            self.uzyj(item, lokalizacja)
                        elif (
                                wybranie_przedmiotu == str(1)
                                and slownik_interfejsu[int(ID_przedmiotu)] in przedmioty_w_uzyciu
                        ):
                            self.zdejmij(item, lokalizacja, przedmioty_w_uzyciu)
                        elif wybranie_przedmiotu == str(2):
                            self.wyrzuc(item, lokalizacja)
                        elif wybranie_przedmiotu == str(3):
                            print("\nPrzedmiot został odłożony, wybierz inny\n")
                            self.interfejs(lokalizacja, init=True)
                        else:
                            print("\nNie wybrano 1, 2, lub 3. Wychodzenie do menu...\n")
                            self.interfejs(lokalizacja, init=True)
            except KeyError:
                print("\nDanego przedmiotu nie ma w ekwipunku.\n")
                self.interfejs(lokalizacja, init=True)
            except ValueError:
                print("\nDanego przedmiotu nie ma w ekwipunku.\n")
                self.interfejs(lokalizacja, init=True)


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
        przedmioty_w_uzyciu = [
            Ekwipunek_Obiekt.w_uzyciu[key].nazwa for key in Ekwipunek_Obiekt.w_uzyciu
        ]
        ID = 0
        print("Oto wszystkie przedmioty w ekwipunku, które możesz naostrzyć:")
        for key, value in kontener.wyswietl().items():
            if isinstance(value[0], (BronJednoreczna, BronDwureczna)):
                for i in value:
                    if not i.naostrzony:
                        if i.nazwa not in przedmioty_w_uzyciu:
                            # tu zalozenie ze wszystkie przedmioty z listy maja dany atrybut
                            print(ID, key, "sztuk " + str(len(value)))
                            slownik_oselki[ID] = i.nazwa
                            ID += 1
                            break
                        else:
                            print(ID, key, "w użyciu")
                            slownik_oselki[ID] = i.nazwa + " w użyciu"
                            ID += 1
                            if len(value) - 1 == 0:
                                break
                            else:
                                print(ID, key, "sztuk " + str(len(value) - 1))
                                slownik_oselki[ID] = i.nazwa
                                ID += 1
                                break
        val = input(
            "Podaj ID przedmiotu, który chciałbyś naostrzyć lub wpisz 'exit' by wyjść: "
        )
        if val == "exit":
            pass
        else:
            if (
                slownik_oselki[int(val)].partition(" w użyciu")[0]
                in kontener.wyswietl()
            ):
                if "w użyciu" in slownik_oselki[int(val)]:
                    item = kontener[
                        slownik_oselki[int(val)].partition(" w użyciu")[0]
                    ][0]
                    item._obrazenia *= 1.10
                    math.ceil(item._obrazenia)
                    del kontener[slownik_oselki[int(val)].partition(" w użyciu")[0]][0]
                    if (
                        kontener[slownik_oselki[int(val)].partition(" w użyciu")[0]]
                        == []
                    ):
                        del kontener[
                            slownik_oselki[int(val)].partition(" w użyciu")[0]
                        ]
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
                    item._obrazenia *= 1.10
                    math.ceil(item._obrazenia)
                    del kontener[slownik_oselki[int(val)]][-1]
                    if kontener[slownik_oselki[int(val)]] == []:
                        del kontener[slownik_oselki[int(val)]]
                    item._nazwa = "Naostrzony " + slownik_oselki[int(val)]
                    item._naostrzony = True
                    kontener.update({item._nazwa: [item]})
                    print("Przedmiot naostrzono")
                    Oselka.naostrz(kontener)
            else:
                print("Danego przedmiotu nie ma w ekwipunku!")
                Oselka.naostrz(kontener)


class Bohater:
    """
    Nowopowstała klasa Bohater będąca pośrednikiem między Podłogą, a Ekwipunkiem,
    posiadająca metodę podejrzyj.
    """

    def podejrzyj(self, obiekt):
        przedmioty = obiekt.spojrz()
        a = przedmioty.copy()
        print("Podniesiono:")
        for i in a:
            self.podnies(i)
            print(i.nazwa)
            obiekt.zawartosc.remove(i)

    def podnies(self, przedmiot):
        Ekwipunek.dodaj(Ekwipunek_Obiekt, przedmiot)


class Khorinis:
    """
    Klasa Khorinis to zbiór wszystkich stworzonych obiektów typu Przedmiot w Khorinis.
    Posiada metodę spójrz.
    """

    def __init__(self):
        self.zawartosc = [
            BronJednoreczna("Szept Burzy", 1360, {"Siła": 20}, 50, False),
            BronJednoreczna("Szept Burzy", 1360, {"Siła": 20}, 50, False),
            BronJednoreczna("Szept Burzy", 1360, {"Siła": 20}, 50, False),
            BronJednoreczna("Kij z gwoździem", 7, {"Siła": 5}, 11, False),
            BronJednoreczna("Mieczyk", 7, {"Siła": 5}, 11, False),
            BronJednoreczna("Mieczyk", 7, {"Siła": 5}, 11, False),
            Luk("Zmyślony Łuk", 20, {"Zręczność": 20}, 100),
            Kusza("Zmyślona Kusza", 30, {"Zręczność": 50}, 80),
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

    def spojrz(self):
        """
        Metoda zwracająca listę zawartość
        """
        # odpowiednik wyswietl, aka spojrz na podloge
        return self.zawartosc


class Gornicza_Dolina:
    """
    Klasa Gornicza_Dolina to zbiór wszystkich stworzonych obiektów typu Przedmiot w Gorniczej Dolinie.
    Posiada metodę spójrz.
    """

    def __init__(self):
        self.zawartosc = [
            BronJednoreczna(
                "Szept Burzy z Gorniczej Doliny", 1360, {"Siła": 20}, 50, False
            ),
            BronJednoreczna("Mieczyk z Gorniczej Doliny", 7, {"Siła": 5}, 11, False),
            BronJednoreczna("Mieczyk z Gorniczej Doliny", 7, {"Siła": 5}, 11, False),
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
            Runa("Bryła lodu z Gorniczej Doliny", 700, 3, {"Obrażenia": 3}, 50),
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

    def spojrz(self):
        """
        Metoda zwracająca listę zawartość
        """
        # odpowiednik wyswietl, aka spojrz na podloge
        return self.zawartosc


Ekwipunek_Obiekt = Ekwipunek()
Oselka_Obiekt = Oselka()
Bohater_Obiekt = Bohater()
Khorinis_Obiekt = Khorinis()
Gornicza_Dolina_Obiekt = Gornicza_Dolina()


def interfejs_glowny(lokalizacja=None):
    """
    Interfejs główny modułu. Za jego pomocą wywoływane są metody.

    :param lokalizacja: jest to lokalizacja, w ktorej uzytkownik obecnie sie znajduje,
            dla przykladu Khorinis lub Gornicza Dolina
    """
    if lokalizacja is None:
        val = input("\nWybierz lokalizacje\n1. Khorinis \n2. Gornicza Dolina")
        if val == str(1):
            lokalizacja = Khorinis_Obiekt
            interfejs_glowny(lokalizacja)
        elif val == str(2):
            lokalizacja = Gornicza_Dolina_Obiekt
            interfejs_glowny(lokalizacja)
        else:
            print("Wybierz jeszcze raz")
            interfejs_glowny(lokalizacja)
    val = input(
        f"Znajdujesz się w {type(lokalizacja).__name__}. "
        f"Wybierz co chcesz zrobić. "
        f"\n 1. Zmień lokalizacje. "
        f"\n 2. Zbierz przedmioty znajdujace sie w danej lokacji, "
        f"\n 3. Odpal interfejs ekwipunku, "
        f"\n 4. Odpal interfejs Osełki, "
        f"\n 5. Wyświetl przedmioty w użyciu bohatera"
    )
    if val == str(1):
        if lokalizacja == Khorinis_Obiekt:
            lokalizacja = Gornicza_Dolina_Obiekt
            interfejs_glowny(lokalizacja)
        else:
            lokalizacja = Khorinis_Obiekt
            interfejs_glowny(lokalizacja)
    if val == str(2):
        Bohater_Obiekt.podejrzyj(lokalizacja)
        print("\nPrzedmioty zostały podniesione. \n")
        interfejs_glowny(lokalizacja)
    if val == str(3):
        Ekwipunek_Obiekt.interfejs(lokalizacja)
        interfejs_glowny(lokalizacja)
    if val == str(4):
        Oselka_Obiekt.naostrz(Ekwipunek_Obiekt._bronie)
        interfejs_glowny(lokalizacja)
    if val == str(5):
        Ekwipunek_Obiekt.wyswietl_w_uzyciu()
        interfejs_glowny(lokalizacja)


interfejs_glowny()

# API - ladne punkty wejscia i wyjscia

# przejscie przez restrukturyzacje kodu, tworzenie funkcji ladnych, zgrabnych i przyjemnych dla uzytkownika
