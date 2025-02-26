"""
Moduł z klasą Osełka
"""

from typing import Any

from clear import clear
from przedmioty.bron import BronDwureczna, BronJednoreczna

# pylint: disable=protected-access, too-many-branches, too-many-statements
# pylint: disable=inconsistent-return-statements
# pylint: disable=too-few-public-methods


class Oselka:
    """
    Klasa Osełka posiadająca metodę naostrz
    """

    @staticmethod
    def naostrz(kontener: dict, obiekt_ekwipunku: "Ekwipunek"):
        """
        Metoda naostrz przyjmuje kontener jako argument, a następnie wyświetla przedmioty
        możliwe do naostrzenia znajdujące się w tym kontenerze. W tym momencie jedyny
        kontener posiadający przedmioty możliwe do naostrzenia to kontener broni.
        Metoda podnosi statystyki obrażeń przedmiotu o 10% oraz zmienia jego nazwę oraz
        pole 'naostrzony'
        :param kontener: kontener danego przedmiotu, np. bronie
        """
        slownik_oselki: dict[int, str] = {}
        przedmioty_w_uzyciu: list[str, Any] = [
            obj.nazwa
            for nazwa_obj in obiekt_ekwipunku.w_uzyciu.values()
            for obj in nazwa_obj
        ]
        identifier: int = 0
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
        val: input = input(
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
                    Oselka.naostrz(kontener, obiekt_ekwipunku)
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
                    Oselka.naostrz(kontener, obiekt_ekwipunku)
            else:
                print("Danego przedmiotu nie ma w ekwipunku!")
                Oselka.naostrz(kontener, obiekt_ekwipunku)
        except KeyError:
            print("Przedmiot z danym ID nie istnieje")
            Oselka.naostrz(kontener, obiekt_ekwipunku)
