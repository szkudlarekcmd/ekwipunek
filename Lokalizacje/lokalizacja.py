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
