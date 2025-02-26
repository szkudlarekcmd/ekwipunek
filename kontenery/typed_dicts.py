"""
Moduł ze wszystkim typed dictsami.
"""

# pylint: disable=missing-function-docstring

# pytanie czy wszystko odgórnie definiować dla każdego przedmiotu?????
from typing import TypedDict


class PrzedmiotEfekt(TypedDict, total=False):
    """
    Typed Dict dla efektu klasy Przedmiot
    """

    hp: int
    mana: int
    sila: int
    zrecznosc: int


class BronEfekt(TypedDict):
    """
    Typed Dict dla efektu klasy Bron
    """

    obrazenia: float


class PancerzEfekt(TypedDict, total=False):
    """
    Typed Dict dla efektu klasy Pancerz
    """

    ochrona_przed_bronia: int
    ochrona_przed_strzalami: int
    ochrona_przed_magia: int
    ochrona_przed_ogniem: int
    hp: int
    mana: int
    sila: int
    zrecznosc: int


class MagiaEfekt(TypedDict, total=False):
    """
    Typed Dict dla efektu klasy Magia
    """

    obrazenia: float
    hp: int
    mana: int


class ArtefaktEfekt(TypedDict, total=False):
    """
    Typed Dict dla efektu klasy Artefakt
    """

    hp: int
    mana: int
    sila: int
    zrecznosc: int


class JedzenieEfekt(TypedDict, total=False):
    """
    Typed Dict dla efektu klasy Jedzenie
    """

    hp: int
    mana: int
    sila: int
    zrecznosc: int


class PismoEfekt(TypedDict, total=False):
    """
    Typed Dict dla efektu klasy Pismo
    """

    hp: int
    mana: int
    sila: int
    zrecznosc: int
