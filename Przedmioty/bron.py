from Kontenery.typed_dicts import BronEfekt
from Przedmioty.przedmiot import Przedmiot


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
