# no nie jest to najładniejszy kod w moim życiu

from abc import ABC, abstractmethod


class Przedmiot(ABC):
    """
    Base klasa, abstrakcyjna, z której dziedziczą wszystkie pozostałe klasy.
    Generalnie zastanawiam się czy nie lepiej nie robić z tego klasy abstrakcyjnej
    ponieważ niektóre metody w stylu "wyrzuć' się mocno porkywają, wystarczy formatować stringa.
    """

    def __init__(self, nazwa, wartosc, ilosc):
        # 3 pola, które dziedziczą wszystkie klasy
        self._nazwa = nazwa
        self._wartosc = wartosc
        self.ilosc = ilosc

    """
    Ekwipunek oraz lista przedmiotów w użyciu dałem jako dict - pewnie da się to zrobić
    lepiej i bardziej mądrze. 
    """
    ekwipunek = {}
    w_uzyciu = {}

    # tutaj wykorzystanie dekoratora property w tym celu, by pola były immutable.
    @property
    def nazwa(self):
        return self._nazwa

    @property
    def wartosc(self):
        return self._wartosc

    # tutaj standardowo, abstract methody bez definicji
    @abstractmethod
    def użyj(self):
        pass

    @abstractmethod
    def wyrzuć(self):
        pass

    @abstractmethod
    def dodaj(self):
        pass


# podział klas zrobiłem na podstawie rodzajów przedmiotów
class Broń(Przedmiot):
    """
    Klasa broni białej - w tym wypadku ograniczyłem się tylko do niej, jednak dodanie np. łuków, kusz
    powinno być całkiem proste. Standardowe pola to nazwa, wartość, ilość, wymagania statystyk do
    użycia broni, typ broni (jednoręczna/dwuręczna) oraz zadawane przez nią obrażenia.
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        ilosc: int,
        wymagania: dict,
        typ: str,
        obrazenia: float,
    ):
        """
        dziedziczę pola wspólne, dodaję nowe
        ta podłoga, tak wyczytałem, wskazuje na to, że pole jest immutable
        """
        super().__init__(nazwa, wartosc, ilosc)
        self._wymagania = wymagania
        self._typ = typ
        self._obrazenia = obrazenia

    @property
    def wymagania(self):
        return self._wymagania

    @property
    def typ(self):
        return self._typ

    @property
    def obrazenia(self):
        return self._obrazenia

    """
    Metoda naostrz, która jako jedyna pozwala zmieniać pole obrażenia
    nie podoba mi się za bardzo, że muszę aktualizować zarówno obiekt jak i
    element w ekwipunku. Można by za każdym razem usuwać oraz dodawać ten przedmiot
    po naostrzeniu, ale imo to dziwny update. może trzeba zmienić metodę dodaj
    która nie tworzy de facto nowego słownika, tylko dodaje sam obiekt
    """

    def naostrz(self):
        self._obrazenia += 1
        self.ekwipunek[self.nazwa]["Obrażenia"] += 1

    def użyj(self):
        if self.nazwa in self.ekwipunek:
            self.w_uzyciu.update({"Broń": self.nazwa})
        else:
            print("Broń nie znajdująca się w ekwipunku nie może być użyta.")

    def wyrzuć(self):
        if self.nazwa in self.w_uzyciu.values():
            print("Nie można wyrzucić przedmiotu w użyciu!")
        else:
            if (
                self.nazwa in self.ekwipunek
                and self.ekwipunek[self.nazwa]["Ilość"] >= 2
            ):
                self.ekwipunek[self.nazwa]["Ilość"] -= 1
                print("Broń wyrzucona!")
            elif (
                self.nazwa in self.ekwipunek
                and self.ekwipunek[self.nazwa]["Ilość"] == 1
            ):
                del self.ekwipunek[self.nazwa]
                print("Broń wyrzucona!")
            else:
                print("Przedmiot nie znajdował się w ekwipunku!")

    def dodaj(self):
        if self.nazwa not in self.ekwipunek:
            self.ekwipunek.update(
                {
                    self.nazwa: {
                        "Wartość": self.wartosc,
                        "Wymagania": self.wymagania,
                        "Typ": self.typ,
                        "Obrażenia": self.obrazenia,
                        "Klasa": self.__class__.__name__,
                        "Ilość": self.ilosc,
                    }
                }
            )
        else:
            self.ekwipunek[self.nazwa]["Ilość"] += 1


class Pancerze(Przedmiot):
    """
    Klasa pancerzy. Standardowe pola to nazwa, wartość, ilość, ochrona przed bronią, strzałami
    oraz ogniem.
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        ilosc: int,
        bron: int,
        strzaly: int,
        ogien: int,
    ):
        super().__init__(nazwa, wartosc, ilosc)
        self._bron = bron
        self._strzaly = strzaly
        self._ogien = ogien

    @property
    def bron(self):
        return self._bron

    @property
    def strzaly(self):
        return self._strzaly

    @property
    def ogien(self):
        return self._ogien

    def użyj(self):
        if self.nazwa in self.ekwipunek:
            self.w_uzyciu.update({"Pancerz": self.nazwa})
        else:
            print("Pancerz nie znajdujący się w ekwipunku nie może być użyty.")

    def wyrzuć(self):
        if self.nazwa in self.w_uzyciu.values():
            print("Nie można wyrzucić przedmiotu w użyciu!")
        else:
            if (
                self.nazwa in self.ekwipunek
                and self.ekwipunek[self.nazwa]["Ilość"] >= 2
            ):
                self.ekwipunek[self.nazwa]["Ilość"] -= 1
                print("Pancerz wyrzucony!")
            elif (
                self.nazwa in self.ekwipunek
                and self.ekwipunek[self.nazwa]["Ilość"] == 1
            ):
                del self.ekwipunek[self.nazwa]
                print("Pancerz wyrzucony!")
            else:
                print("Przedmiot nie znajdował się w ekwipunku!")

    def dodaj(self):
        if self.nazwa not in self.ekwipunek:
            self.ekwipunek.update(
                {
                    self.nazwa: {
                        "Wartość": self.wartosc,
                        "Ochrona przed bronią": self.bron,
                        "Ochrona przed strzałami": self.strzaly,
                        "Ochrona przed ogniem": self.ogien,
                        "Klasa": self.__class__.__name__,
                        "Ilość": self.ilosc,
                    }
                }
            )
        else:
            self.ekwipunek[self.nazwa]["Ilość"] += 1


class Magia(Przedmiot):
    """
    Klasa Magii - w tym wypadku ograniczyłem się tylko do run ze względu na wymagany krąg,
    jednak dodanie zwojów i podawanie kręgu jako opcjonalny argument nie powinno być trudne.
    Standardowe pola to nazwa, wartość, ilośc, krąg magii wymagany do użycia runy, koszt many
    oraz obrażenia. Też (błędnie) założyłem, że wszystkie runy w tym wypadku są ofensywne.
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        ilosc: int,
        krąg: int,
        mana: int,
        obrazenia: float,
    ):
        super().__init__(nazwa, wartosc, ilosc)
        self._krąg = krąg
        self._mana = mana
        self._obrazenia = obrazenia

    @property
    def krąg(self):
        return self._krąg

    @property
    def mana(self):
        return self._mana

    @property
    def obrazenia(self):
        return self._obrazenia

    def użyj(self):
        if self.nazwa in self.ekwipunek:
            self.w_uzyciu.update({"Magia": self.nazwa})
        else:
            print("Runa nie znajdująca się w ekwipunku nie może być użyta.")

    def wyrzuć(self):
        if self.nazwa in self.w_uzyciu.values():
            print("Nie można wyrzucić przedmiotu w użyciu!")
        else:
            if (
                self.nazwa in self.ekwipunek
                and self.ekwipunek[self.nazwa]["Ilość"] >= 2
            ):
                self.ekwipunek[self.nazwa]["Ilość"] -= 1
                print("Runa wyrzucona!")
            elif (
                self.nazwa in self.ekwipunek
                and self.ekwipunek[self.nazwa]["Ilość"] == 1
            ):
                del self.ekwipunek[self.nazwa]
                print("Runa wyrzucona!")
            else:
                print("Przedmiot nie znajdował się w ekwipunku!")

    def dodaj(self):
        if self.nazwa not in self.ekwipunek:
            self.ekwipunek.update(
                {
                    self.nazwa: {
                        "Wartość": self.wartosc,
                        "Krąg": self.krąg,
                        "Mana": self.mana,
                        "Obrażenia": self.obrazenia,
                        "Klasa": self.__class__.__name__,
                        "Ilość": self.ilosc,
                    }
                }
            )
        else:
            self.ekwipunek[self.nazwa]["Ilość"] += 1


class Pisma(Przedmiot):
    """
    Klasa Pism - wyjątkowa klasa, ponieważ pisma nie można "ubrać". Użycie danej pozycji powoduje
    wyprintowanie treści do konsoli. Standardowe pola to nazwa, wartość, ilość oraz treść.
    """

    def __init__(self, nazwa: str, wartosc: int, ilosc: int, tresc: str):
        super().__init__(nazwa, wartosc, ilosc)
        self._tresc = tresc

    @property
    def tresc(self):
        return self._tresc

    def użyj(self):
        if self.nazwa in self.ekwipunek:
            print(self.tresc)
        else:
            print("Pismo nie znajdujące się w ekwipunku nie może być użyte.")

    def wyrzuć(self):
        if self.nazwa in self.w_uzyciu.values():
            print("Nie można wyrzucić przedmiotu w użyciu!")
        else:
            if (
                self.nazwa in self.ekwipunek
                and self.ekwipunek[self.nazwa]["Ilość"] >= 2
            ):
                self.ekwipunek[self.nazwa]["Ilość"] -= 1
                print("Runa wyrzucona!")
            elif (
                self.nazwa in self.ekwipunek
                and self.ekwipunek[self.nazwa]["Ilość"] == 1
            ):
                del self.ekwipunek[self.nazwa]
                print("Runa wyrzucona!")
            else:
                print("Przedmiot nie znajdował się w ekwipunku!")

    def dodaj(self):
        if self.nazwa not in self.ekwipunek:
            self.ekwipunek.update(
                {
                    self.nazwa: {
                        "Wartość": self.wartosc,
                        "Klasa": self.__class__.__name__,
                        "Ilość": self.ilosc,
                    }
                }
            )
        else:
            self.ekwipunek[self.nazwa]["Ilość"] += 1


class Jedzenie(Przedmiot):
    """
    Klasa Jedzenie - Koeljna klasa, której nie da się ubrać. Użycie danej pozycji powoduje
    jej zjedzenie, przez co pozycja zmniejsza swoją ilość w ekwipunku o jeden, lub znika z ekwipunku.
    Standardowe pola to nazwa, wartość, ilość, przyznane HP po zjedzeniu oraz dodatkowe bonusy, których wartość
    domyślna jest pusta.
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        ilosc: int,
        HP: int,
        bonusy={"brak": 0},
    ):
        super().__init__(nazwa, wartosc, ilosc)
        self.ilosc = ilosc
        self._HP = HP
        self._bonusy = bonusy

    @property
    def HP(self):
        return self._HP

    @property
    def bonusy(self):
        return self._bonusy

    def użyj(self):
        if self.nazwa in self.ekwipunek:
            print(
                f"Zregenerowano {self.HP} punktów życia oraz przyznano bonus w postaci {self.bonusy}"
            )
            self.wyrzuć()
        else:
            print("Jedzenia nie znajdującego się w ekwipunku nie można zjeść.")

    def wyrzuć(self):
        if self.nazwa in self.ekwipunek and self.ekwipunek[self.nazwa]["Ilość"] >= 2:
            self.ekwipunek[self.nazwa]["Ilość"] -= 1
            print("Jedzenie wyrzucone!")
        elif self.nazwa in self.ekwipunek and self.ekwipunek[self.nazwa]["Ilość"] == 1:
            del self.ekwipunek[self.nazwa]
            print("Jedzenie wyrzucone!")
        else:
            print("Przedmiot nie znajdował się w ekwipunku!")

    def dodaj(self):
        if self.nazwa not in self.ekwipunek:
            self.ekwipunek.update(
                {
                    self.nazwa: {
                        "Wartość": self.wartosc,
                        "Klasa": self.__class__.__name__,
                        "Ilość": self.ilosc,
                        "HP": self.HP,
                        "Bonusy": self.bonusy,
                    }
                }
            )
        else:
            self.ekwipunek[self.nazwa]["Ilość"] += 1


class Artefakty(Przedmiot):
    """
    Klasa artefakty. Artefakty jako jedyne mają dodatkowe pole uzycie - informuje ono, czy przedmiot
    można użyć, czy tez nie. Uznałem, że wszystkie wcześniejsze klasy można użyc, więc takie pole
    jest zbędne. Standardowe pola to nazwa, wartość, ilość oraz użycie - decyduje czy przedmiot można
    użyć, czy też nie.
    """

    def __init__(self, nazwa: str, wartosc: int, ilosc: int, uzycie: str):
        super().__init__(nazwa, wartosc, ilosc)
        self._uzycie = uzycie

    @property
    def uzycie(self):
        return self._uzycie

    def użyj(self):
        if self.nazwa in self.ekwipunek and self.uzycie == "Tak":
            self.w_uzyciu.update({"Artefakty": self.nazwa})
        elif self.nazwa in self.ekwipunek and self.uzycie == "Nie":
            print("Artefaktu nie można użyć.")
        else:
            print("Artefaktu nie znajdującego się w ekwipunku nie można użyć.")

    def wyrzuć(self):
        if self.nazwa in self.ekwipunek and self.ekwipunek[self.nazwa]["Ilość"] >= 2:
            self.ekwipunek[self.nazwa]["Ilość"] -= 1
            print("Artefakt wyrzucony!")
        elif self.nazwa in self.ekwipunek and self.ekwipunek[self.nazwa]["Ilość"] == 1:
            del self.ekwipunek[self.nazwa]
            print("Artefakt wyrzucony!")
        else:
            print("Przedmiot nie znajdował się w ekwipunku!")

    def dodaj(self):
        if self.nazwa not in self.ekwipunek:
            self.ekwipunek.update(
                {
                    self.nazwa: {
                        "Wartość": self.wartosc,
                        "Klasa": self.__class__.__name__,
                        "Ilość": self.ilosc,
                        "Czy można użyć": self.uzycie,
                    }
                }
            )
        else:
            self.ekwipunek[self.nazwa]["Ilość"] += 1


class Pozostałe(Przedmiot):
    """
    Klasa Pozostałe, standardowe pola to nazwa, wartość oraz ilość.
    Ta klasa trochę nie podoba mi się ze względu na zadaną liczbę argumentów
    imo powinno to być tak, że ta klasa może mieć dowolne argumenty
    nie wiem natomiast jak to zrobić, by były dziedziczone 3 podstawowe argumenty
    oraz nieskończona liczba pozostałych
    do tego dodałbym możliwośc użycia w takim wypadku jakiegoś przedmiotu/ubrania
    np. użyj Grabi, czy piły.
    """

    def __init__(self, nazwa: str, wartosc: int, ilosc: int):
        super().__init__(nazwa, wartosc, ilosc)

    def użyj(self):
        pass

    def wyrzuć(self):
        if self.nazwa in self.ekwipunek and self.ekwipunek[self.nazwa]["Ilość"] >= 2:
            self.ekwipunek[self.nazwa]["Ilość"] -= 1
            print("Przedmiot wyrzucony!")
        elif self.nazwa in self.ekwipunek and self.ekwipunek[self.nazwa]["Ilość"] == 1:
            del self.ekwipunek[self.nazwa]
            print("Przedmiot wyrzucony!")
        else:
            print("Przedmiot nie znajdował się w ekwipunku!")

    def dodaj(self):
        if self.nazwa not in self.ekwipunek:
            self.ekwipunek.update(
                {
                    self.nazwa: {
                        "Wartość": self.wartosc,
                        "Klasa": self.__class__.__name__,
                        "Ilość": self.ilosc,
                    }
                }
            )
        else:
            self.ekwipunek[self.nazwa]["Ilość"] += 1


"""
Generalnie wszystkie obiekty są tworzone w taki sposób, to jest jakby defaultowa
lista itemów w grze, gdzie istnieje możliwość tworzenia nowych obiektów
Ograniczyłem się tylko do 2 obiektów z danej klasy, ale nic nie stoi na przeszkodzie by stworzyć ich więcej. 
Można dodać każdy nowy obiekt w taki sam sposób.
Najchętniej wywaliłbym wszystkie obiekty gdzieś na zewnątrz w taki sposób, by nie paskudzić tego kodu
Coś na zasadzie jakiegoś pliku konfiguracyjnego, wczytywanie obiektów z pliku (?)
Ale w jaki sposób to zrobić - nie wiem
"""
Miecz_1 = Broń("Szept Burzy", 1360, 1, {"Siła": 20}, "broń jednoręczna", 50)
Miecz_2 = Broń("Kij z gwoździem", 7, 1, {"Siła": 5}, "broń jednoręczna", 11)
Zbroja_1 = Pancerze("Zbroja strażnika", 1650, 1, 55, 10, 25)
Zbroja_2 = Pancerze("Zbroja z pancerzy pełzaczy", 2400, 1, 80, 15, 30)
Runa_1 = Magia("Bryła lodu", 700, 1, 3, 3, 50)
Runa_2 = Magia("Deszcz ognia", 1300, 1, 5, 13, 100)
Ksiazka_1 = Pisma(" Dwór Irdorath", 0, 1, "Mam w dupie przeznaczenie.")
Ksiazka_2 = Pisma(
    "Historia Jarkendaru", 0, 1, f"\nCo robisz? Topisz złoto? \nNie, siekam cebulkę."
)
Jedzenie_1 = Jedzenie("Gulasz Thekli", 1, 1, 20, {"Siła": 1, "Smak": "Zajebisty"})
Jedzenie_2 = Jedzenie("Zupa Rybna", 20, 1, 10)
Artefakt_1 = Artefakty("Oko Innosa", 0, 1, "Tak")
Artefakt_2 = Artefakty("Kamień ogniskujący", 0, 1, "Nie")
Pozostałe_1 = Pozostałe("Grabie", 0, 1)

"""
tutaj pewna kombinacja różnych metod, wcześniej sprawdzałem inne kombinacje w celu sprawdzenia
czy nie można korzystać z przedmiotu, ktory nie znajduje się w ekwipunku, jak z dict
w użyciu etc.
"""
Miecz_1.dodaj()
Miecz_2.dodaj()
Miecz_1.dodaj()
Miecz_1.naostrz()
Miecz_2.dodaj()
Miecz_2.użyj()
Miecz_1.użyj()
Zbroja_1.dodaj()
Zbroja_2.dodaj()
Miecz_1.wyrzuć()
Miecz_1.dodaj()
Miecz_1.dodaj()
Miecz_1.wyrzuć()
Miecz_1.wyrzuć()
Miecz_1.dodaj()
Miecz_1.dodaj()
Miecz_2.użyj()
Miecz_1.wyrzuć()
Miecz_1.wyrzuć()
Miecz_1.wyrzuć()
Miecz_1.wyrzuć()
Miecz_1.wyrzuć()
Miecz_1.wyrzuć()
Miecz_1.wyrzuć()
Miecz_1.wyrzuć()
Miecz_1.wyrzuć()
Zbroja_1.dodaj()
Miecz_1.użyj()
Miecz_1.dodaj()
Miecz_2.użyj()
Zbroja_1.użyj()
Zbroja_2.użyj()
Runa_1.dodaj()
Runa_2.dodaj()
Runa_1.użyj()
Runa_2.użyj()
Runa_2.wyrzuć()
Runa_1.użyj()
Runa_2.wyrzuć()
Runa_2.użyj()
Ksiazka_1.dodaj()
Ksiazka_2.dodaj()
Ksiazka_1.użyj()
Ksiazka_2.użyj()
Jedzenie_1.dodaj()
Jedzenie_2.dodaj()
Jedzenie_1.użyj()
Jedzenie_1.wyrzuć()
Jedzenie_1.użyj()
Jedzenie_2.użyj()
Artefakt_1.dodaj()
Artefakt_2.dodaj()
Artefakt_1.użyj()
Artefakt_2.użyj()
Pozostałe_1.dodaj()

"""
tutaj metoda, która sortuje po wartości, wyswietla ekwipunek oraz uzywane przedmioty
jeśli podamy jako argument nazwę klasy taką jak Broń, Artefakty, Pisma etc. 
to metoda wyświetli tylko elementy z danej klasy
"""


def Ekwipunek(Klasa="Brak"):
    if Klasa == "Brak":
        sorted_data = dict(
            sorted(
                Przedmiot.ekwipunek.items(),
                key=lambda item: item[1]["Wartość"],
                reverse=True,
            )
        )
        print("W Twoim ekwipunku znajdują się:")
        for i in sorted_data:
            print(i, f"\n {Przedmiot.ekwipunek[i]}")
        print("Używane przedmioty: ")
        print(Przedmiot.w_uzyciu)
    else:
        sorted_data_klasy = dict(
            sorted(
                Przedmiot.ekwipunek.items(),
                key=lambda item: item[1]["Klasa"],
                reverse=True,
            )
        )
        for i in sorted_data_klasy:
            if Przedmiot.ekwipunek[i]["Klasa"] == Klasa:
                print(i, f"\n {Przedmiot.ekwipunek[i]}")


Ekwipunek()
# Ekwipunek("Broń")
