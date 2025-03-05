"""
Moduł z plikiem głównym.

Konwencja -> Koncept jest taki, że w kodzie polskich znaków nie ma oprócz stringów.
Wszystko w pierdolnikach jest oficjalne
"""

from bohater import Bohater
from clear import clear
from lokalizacje.lokalizacja import Lokalizacja
from lokalizacje.gornicza_dolina import GorniczaDolina
from lokalizacje.jarkendar import Jarkendar
from lokalizacje.khorinis import Khorinis
from oselka import Oselka

khorinis = Khorinis()
gornicza_dolina = GorniczaDolina()
jarkendar = Jarkendar()
bohater = Bohater(hp=10, mana=10, sila=10, zrecznosc=10)
oselka = Oselka()
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
            match val:
                case 1:
                    aktualna_lokalizacja = khorinis
                case 2:
                    aktualna_lokalizacja = gornicza_dolina
                case 3:
                    aktualna_lokalizacja = jarkendar
                case _:
                    raise ValueError("błędna wartość elo")
            return bohater.zmien_lokalizacje(aktualna_lokalizacja)
        except ValueError:
            clear()
            print("Podaj wartość jeszcze raz")


def interfejs_glowny(lokalizacja: Lokalizacja | None = None):
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

    input_interfejs: dict[bool, list[str]] = {
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
        prompt: list[str] = [
            f"{f'Znajdujesz się w {str(lokalizacja)}.' if lokalizacja else ''} "
            f"Wybierz co chcesz zrobić. "
        ]
        try:
            zmienna: list[str] = [
                f"{x}. {y}"
                for x, y in enumerate(input_interfejs[bool(lokalizacja)], start=1)
            ]
            val = int(input("\n".join([*prompt, *zmienna]).lstrip("\n ")))
            match val:
                case 1:
                    lokalizacja = wybor_lokalizacji()
                case 2:
                    bohater.podejrzyj(lokalizacja)
                    print("\nprzedmioty zostały podniesione. \n")
                case 3:
                    bohater.ekwipunek.interfejs(lokalizacja)
                case 4:
                    oselka.naostrz(bohater.ekwipunek.bronie, bohater.ekwipunek)
                case 5:
                    bohater.ekwipunek.wyswietl_w_uzyciu()
                case 6:
                    print(vars(bohater))
                case _:
                    raise ValueError("Argh!")
        except ValueError:
            pass


interfejs_glowny(lokalizacja=bohater.aktualna_lokalizacja)

# API - ladne punkty wejscia i wyjscia

# przejscie przez restrukturyzacje kodu, tworzenie funkcji ladnych,
# zgrabnych i przyjemnych dla uzytkownika
