"""
Moduł z klasą Pozostale
"""

from Przedmioty.przedmiot import Przedmiot


# pylint: disable=too-few-public-methods
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
