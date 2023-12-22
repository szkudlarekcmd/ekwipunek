"""
Koncept jest taki, że w kodzie polskich znaków nie ma oprócz stringów.
"""
from abc import ABC


class Przedmiot(ABC):
    """
    Base klasa, abstrakcyjna, z której dziedziczą wszystkie pozostałe klasy oprócz Ekwipunku.
    """

    def __init__(self, nazwa, wartosc, ilosc):
        # 3 pola, które dziedziczą wszystkie klasy
        self._nazwa = nazwa
        self._wartosc = wartosc
        self.ilosc = ilosc # Generalna uwaga. Ilość nie powinna pochodzic z góry, jako że gdy dodaje przedmiot do ekwipunku to nie wiem jaka jest jego ilość.
        # Ta wartość powinna się internalnie inkrementować i dekrementować, ale nie powinienem móc jest zmienić z zewnątrz

    # tutaj wykorzystanie dekoratora property w tym celu, by pola były immutable.
    @property
    def nazwa(self):
        return self._nazwa

    @property
    def wartosc(self):
        return self._wartosc


# podział klas zrobiłem na podstawie rodzajów przedmiotów
class Bron(Przedmiot): # stworz subklasy luk, kusza, bron jednoreczna, bron dwureczna itd
    """
    Klasa broni - Standardowe pola to nazwa, wartość, ilość, wymagania statystyk do
    użycia broni, typ broni (jednoręczna/dwuręczna/kusza/łuki - nie ma podziału na broń
    jednoręczną, dwuręczną, gdyż posiadają te same pola) oraz zadawane przez nią obrażenia.
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        ilosc: int,
        wymagania: dict, # typing. Opisz czym są wymagania
        typ: str,
        obrazenia: float,
    ):
        """
        dziedziczę pola wspólne, dodaję nowe
        ta podłoga, tak wyczytałem, wskazuje na to, że pole jest immutable <- nie do końca, to jest tylko oznaczenie że pole jest prywatne. 
        Ale nie ma rzeczywistego przełożenia, gdyż python nie ma konceptu prywatności i publiczności. Ustawienie tylko gettera sprawia że pole staje 
        sie read-only. To samo można uzyskać przy pomocy __setattribute__ a dekorator robi to za Ciebie
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


class Pancerze(Przedmiot): # Pancerz, bo jest to klasa Pancerza, a nie kontener który zawiera wszystkie Pancerze
    """
    Klasa pancerzy. Standardowe pola to nazwa, wartosc, ilosc, ochrona przed bronia, magia,2 strzalami
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
        magia: int,
    ):
        super().__init__(nazwa, wartosc, ilosc)
        self._bron = bron
        self._strzaly = strzaly
        self._ogien = ogien
        self._magia = magia

    @property
    def bron(self):
        return self._bron

    @property
    def strzaly(self):
        return self._strzaly

    @property
    def ogien(self):
        return self._ogien

    @property
    def magia(self):
        return self._magia



class Magia(Przedmiot): # stworz subklasy runa i zwój
    """
    Klasa Magii - w tym wypadku ograniczyłem się tylko do run ze względu na wymagany krąg,
    jednak dodanie zwojów i podawanie kręgu jako opcjonalny argument nie powinno być trudne.
    Standardowe pola to nazwa, wartość, ilość, koszt many, działanie oraz wymagany krąg magii
    jeśli mamy do czynienia z runą.
    """

    def __init__(
        self,
        nazwa: str,
        wartosc: int,
        ilosc: int,
        mana: int,
        dzialanie: dict, # typing, opisz co znaczy działanie
        krag: int = None,
    ):
        super().__init__(nazwa, wartosc, ilosc)
        self._mana = mana
        self._dzialanie = dzialanie # Pole działanie powinno byc dla innych klas również
        self._krag = krag

    @property
    def mana(self):
        return self._mana

    @property
    def dzialanie(self):
        return self._dzialanie

    @property
    def krag(self):
        return self._krag


class Pisma(Przedmiot): # Pismo, bo jest to klasa Pisma, a nie kontener który zawiera wszystkie Pisma
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


class Jedzenie(Przedmiot):
    """
    Klasa Jedzenie - Kolejna klasa, której nie da się ubrać. Użycie danej pozycji powoduje
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
        bonusy={"brak": 0}, # None, i ustaw typing 
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


class Artefakty(Przedmiot): # Artefakt, a nie Artefakty. Zrób dodatkową subklasę "PrzedmiotUzywalny" który dodaje metodę "użyj". Nowe subklasy 
    # Pierścień, amulet, tablica, i jesli uznasz że coś jeszcze to stwórz.
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


class Pozostale(Przedmiot): 
    """
    # Najtrudniejsza klasa, bo dośc generyczna. Powinna przyjmować parametr używalności, tak samo jak ta powyżej. Dodaj jej kwargs, ale powinna ona obsłużyć tylko konkretne kwargsy, a nie cokolwiek
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

# Generalna sprawa. Ekwipunek powinien mieć kontenery: Bronie, Magiczne etc. do nich na podstawie typu dodajesz odpowiedni przedmio.
# Używaj isinstance! Możesz użyć danej klasy kontenera jako klucz słownika w_użyciu ( generalny koncept, pomyśl jak to dobrze zrobić )
class Ekwipunek:
    magazyn = {} # to powinny być wewnętrzne pola klasy i edytowalne tylko za pomocą metod ekwipunku
    w_uzyciu = {} 

    def uzyj(self, przedmiot):
        # powinna być walidacja wymagań
        if przedmiot.nazwa in self.magazyn: # To nie powinno być potrzebne, jako że logicznym jest że nie będziesz próbował założyć czegoś czego nie masz. 
            # Załóż że przedmiot musi być w ekwipunku. 
            if przedmiot.__class__.__name__ == "Bron": # do takich rzeczy polecam jednak isinstance
                if (
                    przedmiot.typ == "broń jednoręczna"# tak samo tutaj. Dlatego zdefiniuj te subklasy. To ułatwi sprawę
                    or przedmiot.typ == "broń dwuręczna"
                ):
                    self.w_uzyciu.update({"Broń biała": przedmiot.nazwa})
                elif przedmiot.typ == "łuk" or przedmiot.typ == "kusza":
                    self.w_uzyciu.update({"Broń dystansowa": przedmiot.nazwa})
            elif przedmiot.__class__.__name__ == "Pancerze":
                self.w_uzyciu.update({"Pancerz": przedmiot.nazwa})
            elif przedmiot.__class__.__name__ == "Magia":
                if przedmiot.krag == None: # if not przemiot.krag
                    print("Zwój został użyty!")
                    self.wyrzuc_bez_printowania(przedmiot) # jeśli wyrzucasz, to znaczy że mogę go znowu podnieść i znowu użyć ;)
                else:
                    self.w_uzyciu.update({"Magia": przedmiot.nazwa})
            elif przedmiot.__class__.__name__ == "Pisma":
                print(przedmiot.tresc)
            elif przedmiot.__class__.__name__ == "Jedzenie":
                print(
                    f"Zregenerowano {przedmiot.HP} punktów życia oraz przyznano bonus w postaci {przedmiot.bonusy}"
                )
                self.wyrzuc_bez_printowania(przedmiot)
            elif przedmiot.__class__.__name__ == "Artefakty":
                if przedmiot.uzycie == "Tak":
                    self.w_uzyciu.update({"Artefakty": przedmiot.nazwa})
                elif przedmiot.nazwa in self.magazyn and przedmiot.uzycie == "Nie":
                    print("Artefaktu nie można użyć.")
        else:
            print("Przedmiotu nie znajdującego się w ekwipunku nie można użyć!")

    def wyrzuc(self, przedmiot):
        if przedmiot.nazwa in self.w_uzyciu.values():
            print("Nie można wyrzucić przedmiotu w użyciu!")
        else:
            if (
                przedmiot.nazwa in self.magazyn
                and self.magazyn[przedmiot.nazwa]["Ilość"] >= 2
            ):
                self.magazyn[przedmiot.nazwa]["Ilość"] -= 1
                print("Przedmiot wyrzucony")
            elif (
                przedmiot.nazwa in self.magazyn
                and self.magazyn[przedmiot.nazwa]["Ilość"] == 1
            ):
                del self.magazyn[przedmiot.nazwa]
                print("Przedmiot wyrzucony i nie znajduje się już w ekwipunku!")
            else:
                print("Przedmiot nie znajdował się w ekwipunku!")

    def wyrzuc_bez_printowania(self, przedmiot):
        if (
            przedmiot.nazwa in self.magazyn
            and self.magazyn[przedmiot.nazwa]["Ilość"] >= 2
        ):
            self.magazyn[przedmiot.nazwa]["Ilość"] -= 1
        elif (
            przedmiot.nazwa in self.magazyn
            and self.magazyn[przedmiot.nazwa]["Ilość"] == 1
        ):
            del self.magazyn[przedmiot.nazwa]
        else:
            print("Przedmiot nie znajdował się w ekwipunku!")

    def dodaj(self, przedmiot): # typing, tu i wszędzie
        if przedmiot.nazwa not in self.magazyn:
            if przedmiot.__class__.__name__ == "Bron": # isinstance, tu i wszędzie
                self.magazyn.update(
                    {
                        przedmiot.nazwa: {
                            "Wartość": przedmiot.wartosc,
                            "Wymagania": przedmiot.wymagania,
                            "Typ": przedmiot.typ,
                            "Obrażenia": przedmiot.obrazenia,
                            "Klasa": przedmiot.__class__.__name__,
                            "Ilość": przedmiot.ilosc,
                        }
                    }
                )

            elif przedmiot.__class__.__name__ == "Pancerze":
                self.magazyn.update(
                    {
                        przedmiot.nazwa: {
                            "Wartość": przedmiot.wartosc,
                            "Ochrona przed bronią": przedmiot.bron,
                            "Ochrona przed strzałami": przedmiot.strzaly,
                            "Ochrona przed ogniem": przedmiot.ogien,
                            "Ochrona przed magią": przedmiot.magia,
                            "Klasa": przedmiot.__class__.__name__,
                            "Ilość": przedmiot.ilosc,
                        }
                    }
                )
            elif przedmiot.__class__.__name__ == "Magia":
                self.magazyn.update(
                    {
                        przedmiot.nazwa: {
                            "Wartość": przedmiot.wartosc,
                            "Krąg": przedmiot.krag,
                            "Mana": przedmiot.mana,
                            "Działanie": przedmiot.dzialanie,
                            "Klasa": przedmiot.__class__.__name__,
                            "Ilość": przedmiot.ilosc,
                        }
                    }
                )
            elif przedmiot.__class__.__name__ == "Pisma":
                self.magazyn.update(
                    {
                        przedmiot.nazwa: {
                            "Wartość": przedmiot.wartosc,
                            "Klasa": przedmiot.__class__.__name__,
                            "Ilość": przedmiot.ilosc,
                        }
                    }
                )
            elif przedmiot.__class__.__name__ == "Jedzenie":
                self.magazyn.update(
                    {
                        przedmiot.nazwa: {
                            "Wartość": przedmiot.wartosc,
                            "Klasa": przedmiot.__class__.__name__,
                            "Ilość": przedmiot.ilosc,
                            "HP": przedmiot.HP,
                            "Bonusy": przedmiot.bonusy,
                        }
                    }
                )
            elif przedmiot.__class__.__name__ == "Artefakty":
                self.magazyn.update(
                    {
                        przedmiot.nazwa: {
                            "Wartość": przedmiot.wartosc,
                            "Klasa": przedmiot.__class__.__name__,
                            "Ilość": przedmiot.ilosc,
                        }
                    }
                )
            elif przedmiot.__class__.__name__ == "Pozostałe":
                self.magazyn.update(
                    {
                        przedmiot.nazwa: {
                            "Wartość": przedmiot.wartosc,
                            "Klasa": przedmiot.__class__.__name__,
                            "Ilość": przedmiot.ilosc,
                        }
                    }
                )
        else:
            self.magazyn[przedmiot.nazwa]["Ilość"] += 1

    def wyswietl(self, Klasa="Brak"): # typ = None zamiast Klasa
        if Klasa == "Brak":
            sorted_data = dict(
                sorted(
                    self.magazyn.items(),
                    key=lambda item: item[1]["Wartość"], # sortowanie w sumie mogłoby być zależne od parametru
                    reverse=True,
                )
            )
            print("W Twoim ekwipunku znajdują się:")
            for i in sorted_data:
                print(i, f"\n {self.magazyn[i]}")
            print("Używane przedmioty: ")
            print(self.w_uzyciu)
        else:
            sorted_data_klasy = dict(
                sorted(
                    self.magazyn.items(),
                    key=lambda item: item[1]["Klasa"],
                    reverse=True,
                )
            )
            for i in sorted_data_klasy: # redundante względem tego wyżej
                if self.magazyn[i]["Klasa"] == Klasa: 
                    print(i, f"\n {self.magazyn[i]}") 

    """
    Metoda naostrz, która jako jedyna pozwala zmieniać pole obrażenia
    nie podoba mi się za bardzo, że muszę aktualizować zarówno obiekt jak i
    element w ekwipunku. Można by za każdym razem usuwać oraz dodawać ten przedmiot
    po naostrzeniu, ale imo to dziwny update. może trzeba zmienić metodę dodaj
    która nie tworzy de facto nowego słownika, tylko dodaje sam obiekt
    """

    def naostrz(self, przedmiot):
        if przedmiot.__class__.__name__ == "Bron" and (
            przedmiot.typ == "broń jednoręczna" or przedmiot.typ == "broń dwuręczna"
        ):
            # to mi sie nie podoba, ale wyjaśniłem to wyżej ( komentarz ogólny do Ekwipunek )
            self.magazyn[przedmiot.nazwa]["Obrażenia"] += 1
        else:
            print("Danego przedmiotu nie da się naostrzyć")


"""
Generalnie wszystkie obiekty są tworzone w taki sposób, to jest jakby defaultowa
lista itemów w grze, gdzie istnieje możliwość tworzenia nowych obiektów
Ograniczyłem się tylko do 2 obiektów z danej klasy, ale nic nie stoi na przeszkodzie by stworzyć ich więcej. 
Można dodać każdy nowy obiekt w taki sam sposób.
Najchętniej wywaliłbym wszystkie obiekty gdzieś na zewnątrz w taki sposób, by nie paskudzić tego kodu
Coś na zasadzie jakiegoś pliku konfiguracyjnego, wczytywanie obiektów z pliku (?)
Ale w jaki sposób to zrobić - nie wiem
"""
Miecz_1 = Bron("Szept Burzy", 1360, 1, {"Siła": 20}, "broń jednoręczna", 50)
Miecz_2 = Bron("Kij z gwoździem", 7, 1, {"Siła": 5}, "broń jednoręczna", 11)
Luk_1 = Bron("Zmyślony Łuk", 20, 1, {"Zręczność": 20}, "łuk", 100)
Kusza_1 = Bron("Zmyślona Kusza", 30, 1, {"Zręczność": 50}, "kusza", 80)
Zbroja_1 = Pancerze("Zbroja strażnika", 1650, 1, 55, 10, 25, 10)
Zbroja_2 = Pancerze("Zbroja z pancerzy pełzaczy", 2400, 1, 80, 15, 30, 10)
Runa_1 = Magia("Bryła lodu", 700, 1, 3, {"Obrażenia": 3}, 50)
Runa_2 = Magia("Deszcz ognia", 1300, 1, 5, {"Obrażenia": 13}, 100)
Zwoj_1 = Magia("Wymyślony Zwój", 20, 1, 5, {"Leczenie": 15})
Ksiazka_1 = Pisma(" Dwór Irdorath", 0, 1, "Mam w dupie przeznaczenie.")
Ksiazka_2 = Pisma(
    "Historia Jarkendaru", 0, 1, f"\nCo robisz? Topisz złoto? \nNie, siekam cebulkę."
)
Jedzenie_1 = Jedzenie("Gulasz Thekli", 1, 1, 20, {"Siła": 1, "Smak": "Zajebisty"})
Jedzenie_2 = Jedzenie("Zupa Rybna", 20, 1, 10)
Artefakt_1 = Artefakty("Oko Innosa", 0, 1, "Tak")
Artefakt_2 = Artefakty("Kamień ogniskujący", 0, 1, "Nie")
Pozostale_1 = Pozostale("Grabie", 0, 1)

Ekwipunek_Obiekt = Ekwipunek()
# wszystkie te operacje rób na obiekcie a nie na klasie, po to go stworzyłes
Ekwipunek.dodaj(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.naostrz(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.wyrzuc(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Zwoj_1)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Zwoj_1)
Ekwipunek.wyrzuc(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.wyrzuc(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.wyrzuc(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Miecz_2)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Zbroja_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Zbroja_2)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Runa_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Runa_2)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Ksiazka_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Ksiazka_2)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Jedzenie_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Jedzenie_2)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Artefakt_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Artefakt_2)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Pozostale_1)
Ekwipunek.wyrzuc(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.wyrzuc(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Miecz_2)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Miecz_2)
Ekwipunek.wyrzuc(Ekwipunek_Obiekt, Miecz_2)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Zbroja_1)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Zbroja_2)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Runa_1)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Runa_2)
Ekwipunek.wyrzuc(Ekwipunek_Obiekt, Runa_2)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Runa_2)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Runa_1)
Ekwipunek.wyrzuc(Ekwipunek_Obiekt, Runa_1)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Ksiazka_1)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Ksiazka_2)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Jedzenie_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Jedzenie_2)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Jedzenie_1)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Jedzenie_1)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Jedzenie_1)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Jedzenie_1)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Jedzenie_1)
Ekwipunek.wyrzuc(Ekwipunek_Obiekt, Jedzenie_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Jedzenie_2)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Artefakt_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Artefakt_2)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Artefakt_1)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Artefakt_2)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Pozostale_1)
Ekwipunek.wyrzuc(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.wyrzuc(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.wyrzuc(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.wyrzuc(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Kusza_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Luk_1)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Luk_1)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Kusza_1)
Ekwipunek.uzyj(Ekwipunek_Obiekt, Luk_1)
Ekwipunek.naostrz(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.wyrzuc(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.dodaj(Ekwipunek_Obiekt, Miecz_1)
Ekwipunek.naostrz(Ekwipunek_Obiekt, Luk_1)
Ekwipunek.wyswietl(Ekwipunek_Obiekt)
