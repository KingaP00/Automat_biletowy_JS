from Monety import *
from decimal import *

class Automat(Monety):
    suma = 0

    def init(self):
        super().init()

    def kupBilet(self, cena):
        self.suma += Decimal(str(cena))
        print('Chcesz kupić bilet o wartości' + str(cena))

    def sumuj(self):
        return self.suma

    def zakoncz(self):
        self.suma = 0
        print('Dziękujemy za zakup biletu')





