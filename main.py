"""
Moduł z plikiem głównym.

Konwencja -> Koncept jest taki, że w kodzie polskich znaków nie ma oprócz stringów.
Wszystko w pierdolnikach jest oficjalne
"""

from bohater import Bohater_Obiekt
from clear import clear
from Lokalizacje.gornicza_dolina import Gornicza_Dolina_Obiekt
from Lokalizacje.jarkendar import Jarkendar_Obiekt
from Lokalizacje.khorinis import Khorinis_Obiekt
from oselka import Oselka_Obiekt

from ekwipunek import Ekwipunek_Obiekt


def wybor_lokalizacji():
    """
    Metoda wybor_lokalizacja wywoływana jest, gdy nie znajdujemy się w żadnej lokalizacji
    oraz gdy chcemy wybrać daną lokalizację.
    """
    while True:
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
                lokalizacja = wybor_lokalizacji()
            elif val == 2:
                Bohater_Obiekt.podejrzyj(lokalizacja)
                print("\nPrzedmioty zostały podniesione. \n")
            elif val == 3:
                Ekwipunek_Obiekt.interfejs(lokalizacja)
            elif val == 4:
                Oselka_Obiekt.naostrz(Ekwipunek_Obiekt.bronie)
            elif val == 5:
                Ekwipunek_Obiekt.wyswietl_w_uzyciu()
        except ValueError:
            pass


interfejs_glowny(lokalizacja=None)

# API - ladne punkty wejscia i wyjscia

# przejscie przez restrukturyzacje kodu, tworzenie funkcji ladnych,
# zgrabnych i przyjemnych dla uzytkownika
