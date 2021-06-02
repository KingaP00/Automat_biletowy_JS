from Monety import *
from decimal import *

class Automat(Monety):
    suma = 0

    def init(self):
        super().init()

    def sprzedajBilet(self, cena):
        self.suma -= cena
        print('Chcesz sprzedać bilet o wartości : ' + str(cena/100))

    def kupBilet(self, cena):
        self.suma += cena
        print('Chcesz kupić bilet o wartości : ' + str(cena/100))

    def sumuj(self):
        return self.suma

    def zakoncz(self):
        self.suma = 0

        print('Dziękujemy za zakup biletu')

    def pobierz_suma(self):
        return str(self.suma/100)
