"""
Moduł klasy Kontener, jak i wszystkich jego podklas.
"""

# pylint: disable=missing-function-docstring


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
