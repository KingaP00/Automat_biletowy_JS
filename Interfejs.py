from tkinter import *
from Automat import *

class Interfejs:
    def __init__(self):
        pass

    def mojInterfejs(self):

        # okno interfejsu
        widok = Tk()
        widok.geometry('500x500')

        # potrzebne zmienne
        suma = Automat()
        self.suma = suma
        dodawanie = Monety()
        self.monety = dodawanie
        self.twojepieniadze = 0

        # napisy
        tekst1 = Label(widok, text='Witaj!')
        tekst1.place(x=200, y=1)
        tekst2 = Label(widok, text='Wybierz bilet dla siebie!')
        tekst2.place(x=150, y=20)
        tekst3 = Label(widok, text='Dostępne rodzaje biletów:')
        tekst3.place(x=1, y=40)
        tekst4 = Label(widok, text='Do automatu możesz wrzucić:')
        tekst4.place(x=1, y=170)
        tekst5 = Label(widok, text='Grosze:')
        tekst5.place(x=1, y=190)
        tekst6 = Label(widok, text='Monety:')
        tekst6.place(x=100, y=190)
        tekst7 = Label(widok, text='Banknoty:')
        tekst7.place(x=200, y=190)
        tekst8 = Label(widok, text='Suma: 0')
        tekst8.place(x=1, y=410)
        tekst9 = Label(widok, text='Twoje pieniadze : 0')
        tekst9.place(x=1, y=440)
        tekst10 = Label(widok, text='Kończymy!')
        tekst10.place(x=400, y=450)
        tekst11 = Label(widok, text='')
        tekst11.place(x=200, y=450)
        self.komunikat = tekst11
        self.komunikat_suma = tekst8

        # rodzaje biletów

        # bilet 20-minutowy ulgowy
        bilet20u = Label(widok, text='20-minutowy ulgowy')
        bilet20u.place(x=1, y=70)
        bilet20u_tekst = Label(widok, text="0")
        bilet20u_tekst.place(x=135, y=70)
        bilet20u_dodaj = Button(widok, text='+',
                                command=lambda: [self.dodaj_bilet(self.bilety['bilet20u'], bilet20u_tekst, tekst8)])
        bilet20u_dodaj.place(x=180, y=70)
        bilet20u_odejmij = Button(widok, text='-',
                                  command=lambda: [self.usun_bilet(self.bilety['bilet20u'], bilet20u_tekst, tekst8)])
        bilet20u_odejmij.place(x=160, y=70)

        # bilet 40-minutowy ulgowy
        bilet40u = Label(widok, text='40-minutowy ulgowy')
        bilet40u.place(x=1, y=100)
        bilet40u_tekst = Label(widok, text="0")
        bilet40u_tekst.place(x=135, y=100)
        bilet40u_dodaj = Button(widok, text='+',
                                command=lambda: [self.dodaj_bilet(self.bilety['bilet40u'], bilet40u_tekst, tekst8)])
        bilet40u_dodaj.place(x=180, y=100)
        bilet40u_odejmij = Button(widok, text='-',
                                  command=lambda: [self.usun_bilet(self.bilety['bilet40u'], bilet40u_tekst, tekst8)])
        bilet40u_odejmij.place(x=160, y=100)

        # 60-minutowy ulgowy
        bilet60u = Label(widok, text='60-minutowy ulgowy')
        bilet60u.place(x=1, y=130)
        bilet60u_tekst = Label(widok, text="0")
        bilet60u_tekst.place(x=135, y=130)
        bilet60u_dodaj = Button(widok, text='+',
                                command=lambda: [self.dodaj_bilet(self.bilety['bilet60u'], bilet60u_tekst, tekst8)])
        bilet60u_dodaj.place(x=180, y=130)
        bilet60u_odejmij = Button(widok, text='-',
                                  command=lambda: [self.usun_bilet(self.bilety['bilet60u'], bilet60u_tekst, tekst8)])
        bilet60u_odejmij.place(x=160, y=130)

        # 20-minutowy normalny
        bilet20n = Label(widok, text='20-minutowy normalny')
        bilet20n.place(x=240, y=70)
        bilet20n_tekst = Label(widok, text="0")
        bilet20n_tekst.place(x=380, y=70)
        bilet20n_dodaj = Button(widok, text='+',
                                command=lambda: [self.dodaj_bilet(self.bilety['bilet20n'], bilet20n_tekst, tekst8)])
        bilet20n_dodaj.place(x=420, y=70)
        bilet20n_odejmij = Button(widok, text='-',
                                  command=lambda: [self.usun_bilet(self.bilety['bilet20n'], bilet20n_tekst, tekst8)])
        bilet20n_odejmij.place(x=400, y=70)
        # 40-minutowy normalny
        bilet40n = Label(widok, text='40-minutowy normalny')
        bilet40n.place(x=240, y=100)
        bilet40n_tekst = Label(widok, text="0")
        bilet40n_tekst.place(x=380, y=100)
        bilet40n_dodaj = Button(widok, text='+',
                                command=lambda: [self.dodaj_bilet(self.bilety['bilet40n'], bilet40n_tekst, tekst8)])
        bilet40n_dodaj.place(x=420, y=100)
        bilet40n_odejmij = Button(widok, text='-',
                                  command=lambda: [self.usun_bilet(self.bilety['bilet40n'], bilet40n_tekst, tekst8)])
        bilet40n_odejmij.place(x=400, y=100)
        # 60-minutowy normalny
        bilet60n = Label(widok, text='60-minutowy normalny')
        bilet60n.place(x=240, y=130)
        bilet60n_tekst = Label(widok, text="0")
        bilet60n_tekst.place(x=380, y=130)
        bilet60n_dodaj = Button(widok, text='+',
                                command=lambda: [self.dodaj_bilet(self.bilety['bilet60n'], bilet60n_tekst, tekst8)])
        bilet60n_dodaj.place(x=420, y=130)
        bilet60n_odejmij = Button(widok, text='-',
                                  command=lambda: [self.usun_bilet(self.bilety['bilet60n'], bilet60n_tekst, tekst8)])
        bilet60n_odejmij.place(x=400, y=130)

        # monety -> grosze ( dostępne : 1,2,5,10,20,50 )
        grosz1 = Button(widok, text='1 gr', width=10,
                        command=lambda: [self.wrzucone(1), dodawanie.dodaj(1), tekst9.configure(text='Twoje pieniądze : ' + self.pobierz_twojepieniadze())])
        grosz1.place(x=1, y=220)
        grosz2 = Button(widok, text='2 gr', width=10,
                        command=lambda: [self.wrzucone(2), dodawanie.dodaj(2), tekst9.configure(text='Twoje pieniądze : ' + self.pobierz_twojepieniadze())])
        grosz2.place(x=1, y=250)
        grosz5 = Button(widok, text='5 gr', width=10,
                        command=lambda: [self.wrzucone(5), dodawanie.dodaj(5), tekst9.configure(text='Twoje pieniądze : ' + self.pobierz_twojepieniadze())])
        grosz5.place(x=1, y=280)
        grosz10 = Button(widok, text='10 gr', width=10,
                         command=lambda: [self.wrzucone(10), dodawanie.dodaj(10), tekst9.configure(text='Twoje pieniądze : ' + self.pobierz_twojepieniadze())])
        grosz10.place(x=1, y=310)
        grosz20 = Button(widok, text='20 gr', width=10,
                         command=lambda: [self.wrzucone(20), dodawanie.dodaj(20), tekst9.configure(text='Twoje pieniądze : ' + self.pobierz_twojepieniadze())])
        grosz20.place(x=1, y=340)
        grosz50 = Button(widok, text='50 gr', width=10,
                         command=lambda: [self.wrzucone(50), dodawanie.dodaj(50), tekst9.configure(text='Twoje pieniądze : ' + self.pobierz_twojepieniadze())])
        grosz50.place(x=1, y=370)

        # monety ( dostępne : 1,2,5 )
        moneta1 = Button(widok, text='1 zł', width=10,
                         command=lambda: [self.wrzucone(100), dodawanie.dodaj(100), tekst9.configure(text='Twoje pieniądze :' + self.pobierz_twojepieniadze())])
        moneta1.place(x=100, y=220)
        moneta2 = Button(widok, text='2 zł', width=10,
                         command=lambda: [self.wrzucone(200), dodawanie.dodaj(200), tekst9.configure(text='Twoje pieniądze : ' + self.pobierz_twojepieniadze())])
        moneta2.place(x=100, y=250)
        moneta5 = Button(widok, text='5 zł', width=10,
                         command=lambda: [self.wrzucone(500), dodawanie.dodaj(500), tekst9.configure(text='Twoje pieniądze : ' + self.pobierz_twojepieniadze())])
        moneta5.place(x=100, y=280)

        # banknoty ( dostępne : 10,20,50 )
        banknot10 = Button(widok, text='10 zł', width=10,
                           command=lambda: [self.wrzucone(1000), dodawanie.dodaj(1000), tekst9.configure(text='Twoje pieniądze : ' + self.pobierz_twojepieniadze())])
        banknot10.place(x=200, y=220)
        banknot20 = Button(widok, text='20 zł', width=10,
                           command=lambda: [self.wrzucone(2000), dodawanie.dodaj(2000), tekst9.configure(text='Twoje pieniądze : ' + self.pobierz_twojepieniadze())])
        banknot20.place(x=200, y=250)
        banknot50 = Button(widok, text='50 zł', width=10,
                           command=lambda: [self.wrzucone(5000), dodawanie.dodaj(5000), tekst9.configure(text='Twoje pieniądze : ' + self.pobierz_twojepieniadze())])
        banknot50.place(x=200, y=280)

        # koniec
        koniec = Button(widok, text='Zakończ', width=10,
                        command=lambda: [self.koncz(), tekst9.configure(text='Twoje pieniądze : ' + self.pobierz_twojepieniadze())])
        koniec.place(x=400, y=470)

        self.komunikat_bilet20u_tekst = bilet20u_tekst
        self.komunikat_bilet40u_tekst = bilet40u_tekst
        self.komunikat_bilet60u_tekst = bilet60u_tekst
        self.komunikat_bilet20n_tekst = bilet20n_tekst
        self.komunikat_bilet40n_tekst = bilet40n_tekst
        self.komunikat_bilet60n_tekst = bilet60n_tekst


        widok.mainloop()

    # bilety
    bilety = {
        "bilet20u": {
            "cena": 150,
            "ilosc": 0,
        },
        "bilet40u": {
            "cena": 250,
            "ilosc": 0,
        },
        "bilet60u": {
            "cena": 350,
            "ilosc": 0,
        },
        "bilet20n": {
            "cena": 300,
            "ilosc": 0,
        },
        "bilet40n": {
            "cena": 500,
            "ilosc": 0,
        },
        "bilet60n": {
            "cena": 700,
            "ilosc": 0,
        }
    }

    def dodaj_bilet(self, bilet, tekst, suma):
        bilet['ilosc'] += 1
        tekst.configure(text=bilet['ilosc'])
        self.suma.dodajBilet(bilet['cena'])
        suma.configure(text='Suma' + self.suma.pobierz_suma())

    def usun_bilet(self, bilet, tekst, suma):
        if bilet['ilosc'] > 0:
            bilet['ilosc'] -= 1
            tekst.configure(text=bilet['ilosc'])
            self.suma.odejmijBilet(bilet['cena'])
            suma.configure(text='Suma' + self.suma.pobierz_suma())

    def wrzucone(self, wartosc):
        self.twojepieniadze += wartosc

    def koncz(self):
        """
        PLAN
            1. Czy użytkownik wrzucił więcej pieniędzy lub tyle co trzeba - DONE
            2. Jeśli tyle co trzeba to :  - DONE
                - dodaj pieniądze do wartości w maszynie
                - wyzeruj licznik klienta
            3. Jeśli mniej:   - DONE
                - Informacja - za mało pieniędzy

            4. Jeśli więcej:
                - Algorytm sprawdzania czy jest dostępna reszta

                Jeśli tak:
                    Wydaj resztę
                    Dodaj dostępne pieniądze do wartości w maszynie
                    Wyzeruj licznik klienta
                jeśli nie:
                    Informacja że nie mamy jak wydać
                    wyzeruj licznik klienta
        """
        suma = self.suma.suma
        monety = self.monety

        if suma == 0:
            self.komunikat.configure(text='Nie wybrałeś biletu')
            self.twojepieniadze = 0
        else:
            if self.twojepieniadze == suma:
                self.komunikat.configure(text='Dziękujemy za zakup')
                monety.zaakceptuj_monety()
                self.twojepieniadze = 0
                self.komunikat_suma.configure(text='Suma : 0.0')
                self.komunikat_bilet20u_tekst.configure(text='0')
                self.komunikat_bilet40u_tekst.configure(text='0')
                self.komunikat_bilet60u_tekst.configure(text='0')
                self.komunikat_bilet20n_tekst.configure(text='0')
                self.komunikat_bilet40n_tekst.configure(text='0')
                self.komunikat_bilet60n_tekst.configure(text='0')

            elif self.twojepieniadze > suma:
                try:
                    monety.oblicz_reszte(self.suma.suma, self.twojepieniadze)
                    monety.zaakceptuj_monety()
                    self.komunikat.configure(text='Dziękujemy za zakup')
                    self.twojepieniadze = 0
                    self.komunikat_suma.configure(text='Suma : 0.0')
                    self.komunikat_bilet20u_tekst.configure(text='0')
                    self.komunikat_bilet40u_tekst.configure(text='0')
                    self.komunikat_bilet60u_tekst.configure(text='0')
                    self.komunikat_bilet20n_tekst.configure(text='0')
                    self.komunikat_bilet40n_tekst.configure(text='0')
                    self.komunikat_bilet60n_tekst.configure(text='0')

                except ValueError:
                    self.komunikat.configure(text='Prosimy o dokładną kwotę')
                    self.twojepieniadze = 0

            else:
                self.komunikat.configure(text='Za mało pieniędzy')


    def pobierz_twojepieniadze(self):
        return str(self.twojepieniadze/100)

Interfejs = Interfejs()
Interfejs.mojInterfejs()
