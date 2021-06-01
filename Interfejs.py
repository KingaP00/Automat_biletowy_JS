from decimal import *
from tkinter import *
from Monety import *
from Automat import *


class Interfejs:
    def __init__(self):
        pass

    def mojInterfejs(self):
        widok = Tk()
        widok.geometry('500x500')
        suma = Automat()
        dodawanie = Monety()
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
        tekst8 = Label(widok, text='Suma:')
        tekst8.place(x=1, y=410)
        tekst9 = Label(widok, text='Twoje pieniadze:')
        tekst9.place(x=1, y=440)
        tekst10 = Label(widok, text='Kończymy!')
        tekst10.place(x=400, y=450)

        # przyciski

        # rodzaje biletow

        # bilety ulgowe
        bilet20u = Button(widok, text='20-minutowy ulgowy',
                          command=lambda: [suma.kupBilet(1.50), tekst8.configure(text='Suma' + str(suma.suma))])
        bilet20u.place(x=1, y=70)
        bilet40u = Button(widok, text='40-minutowy ulgowy',
                          command=lambda: [suma.kupBilet(2.50), tekst8.configure(text='Suma' + str(suma.suma))])
        bilet40u.place(x=1, y=100)
        bilet60u = Button(widok, text='60-minutowy ulgowy',
                          command=lambda: [suma.kupBilet(3), tekst8.configure(text='Suma' + str(suma.suma))])
        bilet60u.place(x=1, y=130)

        # normalne
        bilet20n = Button(widok, text='20-minutowy normalny',
                          command=lambda: [suma.kupBilet(3), tekst8.configure(text='Suma' + str(suma.suma))])
        bilet20n.place(x=140, y=70)
        bilet40n = Button(widok, text='40-minutowy normalny',
                          command=lambda: [suma.kupBilet(5), tekst8.configure(text='Suma' + str(suma.suma))])
        bilet40n.place(x=140, y=100)
        bilet60n = Button(widok, text='60-minutowy normalny',
                          command=lambda: [suma.kupBilet(6), tekst8.configure(text='Suma' + str(suma.suma))])
        bilet60n.place(x=140, y=130)

        # monety -> grosze ( dostępne : 1,2,5,10,20,50 )

        grosz1 = Button(widok, text='1 gr', width=10,
                        command=lambda: [self.wrzucone(0.01), dodawanie.dodaj(0.01), tekst9.configure(text='Twoje pieniadze' + str(self.twojepieniadze))])
        grosz1.place(x=1, y=220)
        grosz2 = Button(widok, text='2 gr', width=10,
                        command=lambda: [self.wrzucone(0.02), dodawanie.dodaj(0.02), tekst9.configure(text='Twoje pieniadze' + str(self.twojepieniadze))])
        grosz2.place(x=1, y=250)
        grosz5 = Button(widok, text='5 gr', width=10,
                        command=lambda: [self.wrzucone(0.05), dodawanie.dodaj(0.05), tekst9.configure(text='Twoje pieniadze' + str(self.twojepieniadze))])
        grosz5.place(x=1, y=280)
        grosz10 = Button(widok, text='10 gr', width=10,
                         command=lambda: [self.wrzucone(0.1), dodawanie.dodaj(0.1), tekst9.configure(text='Twoje pieniadze' + str(self.twojepieniadze))])
        grosz10.place(x=1, y=310)
        grosz20 = Button(widok, text='20 gr', width=10,
                         command=lambda: [self.wrzucone(0.2), dodawanie.dodaj(0.2), tekst9.configure(text='Twoje pieniadze' + str(self.twojepieniadze))])
        grosz20.place(x=1, y=340)
        grosz50 = Button(widok, text='50 gr', width=10,
                         command=lambda: [self.wrzucone(0.5), dodawanie.dodaj(0.5), tekst9.configure(text='Twoje pieniadze' + str(self.twojepieniadze))])
        grosz50.place(x=1, y=370)

        # monety ( dostępne : 1,2,5 )

        moneta1 = Button(widok, text='1 zł', width=10,
                         command=lambda: [self.wrzucone(1), dodawanie.dodaj(1), tekst9.configure(text='Twoje pieniadze' + str(self.twojepieniadze))])
        moneta1.place(x=100, y=220)
        moneta2 = Button(widok, text='2 zł', width=10,
                         command=lambda: [self.wrzucone(2), dodawanie.dodaj(2), tekst9.configure(text='Twoje pieniadze' + str(self.twojepieniadze))])
        moneta2.place(x=100, y=250)
        moneta5 = Button(widok, text='5 zł', width=10,
                         command=lambda: [self.wrzucone(5), dodawanie.dodaj(5), tekst9.configure(text='Twoje pieniadze' + str(self.twojepieniadze))])
        moneta5.place(x=100, y=280)

        # banknoty ( dostępne : 10,20,50 )

        banknot10 = Button(widok, text='10 zł', width=10,
                           command=lambda: [self.wrzucone(10), dodawanie.dodaj(10), tekst9.configure(text='Twoje pieniadze' + str(self.twojepieniadze))])
        banknot10.place(x=200, y=220)
        banknot20 = Button(widok, text='20 zł', width=10,
                           command=lambda: [self.wrzucone(20), dodawanie.dodaj(20), tekst9.configure(text='Twoje pieniadze' + str(self.twojepieniadze))])
        banknot20.place(x=200, y=250)
        banknot50 = Button(widok, text='50 zł', width=10,
                           command=lambda: [self.wrzucone(50), dodawanie.dodaj(50), tekst9.configure(text='Twoje pieniadze' + str(self.twojepieniadze))])
        banknot50.place(x=200, y=280)

        # suma

        # koniec

        koniec = Button(widok, text='Zakończ', width=10,
                        command=lambda: [self.koncz(), tekst9.configure(text='Twoje pieniadze : ' + str(self.twojepieniadze) )])
        koniec.place(x=400, y=470)

        widok.mainloop()

    def wrzucone(self, wartosc):
        self.twojepieniadze += wartosc
        self.twojepieniadze = round(self.twojepieniadze, 2)

    def koncz(self):
        self.twojepieniadze = 0


Interfejs = Interfejs()
Interfejs.mojInterfejs()
